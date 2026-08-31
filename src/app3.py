import streamlit as st
import boto3
from botocore.exceptions import NoCredentialsError
import os
from io import BytesIO
from pydub import AudioSegment
import torchaudio
import tempfile
import time
from transformers import WhisperProcessor, WhisperForConditionalGeneration, MarianMTModel, MarianTokenizer
from langdetect import detect
import numpy as np
import requests
import io
import torch

ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

# Initialize the S3 client
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

def convert_to_mp3(file_stream):
    """Convert the file to MP3 format locally using pydub."""
    try:
        audio = AudioSegment.from_file(file_stream)
        mp3_io = BytesIO()
        audio.export(mp3_io, format="mp3")
        mp3_io.seek(0)
        return mp3_io
    except Exception as e:
        st.error(f"Conversion to MP3 failed: {e}")
        return None

def convert_to_wav(file_stream):
    """Convert the file to WAV format for cloud upload using pydub."""
    try:
        audio = AudioSegment.from_file(file_stream)
        wav_io = BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)
        return wav_io
    except Exception as e:
        st.error(f"Conversion to WAV failed: {e}")
        return None

def upload_file_to_s3_in_memory(file_stream, bucket_name, object_name):
    """Upload a file to an S3 bucket from an in-memory stream and return the object URL."""
    try:
        s3.upload_fileobj(file_stream, bucket_name, object_name)
        st.success(f"File uploaded to {bucket_name}/{object_name}")
        
        # Construct the object URL
        url = f"https://{bucket_name}.s3.amazonaws.com/{object_name}"
        return url
    except NoCredentialsError:
        st.error("Credentials not available")
        return None

def split_audio(waveform, chunk_length_s=30, sample_rate=16000):
    """Split the audio into smaller chunks."""
    chunk_length = chunk_length_s * sample_rate
    total_length = waveform.size(0)
    chunks = []
    
    for i in range(0, total_length, chunk_length):
        end = i + chunk_length if (i + chunk_length) < total_length else total_length
        chunks.append(waveform[i:end])
    
    return chunks

def transcribe_chunks(audio_chunks, processor, model):
    """Transcribe a list of audio chunks using the Whisper model."""
    full_transcription = []
    
    for chunk in audio_chunks:
        # Ensure chunk has the correct shape (mono, and resampled to 16000 Hz)
        if len(chunk.shape) > 1 and chunk.shape[0] > 1:
            chunk = torch.mean(chunk, dim=0, keepdim=True)
        
        # Convert chunk to numpy and pass it to Whisper processor
        chunk_np = chunk.numpy()
        input_features = processor(chunk_np, sampling_rate=16000, return_tensors="pt").input_features
        
        # Generate transcription for the chunk
        predicted_ids = model.generate(input_features)
        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
        full_transcription.append(transcription)
    
    return " ".join(full_transcription)

def process_audio_locally_as_mp3(file_stream):
    """Process the audio file locally, convert to 16 kHz mono, and return a PyTorch tensor."""
    try:
        audio = AudioSegment.from_file(file_stream)

        # Convert to mono and 16 kHz
        audio = audio.set_frame_rate(16000).set_channels(1)

        # Convert audio samples to NumPy array
        samples = np.array(audio.get_array_of_samples(), dtype=np.float32)

        # Normalize audio samples to approximately -1.0 to 1.0
        samples /= 2 ** (8 * audio.sample_width - 1)

        # Convert NumPy array to PyTorch tensor
        waveform = torch.from_numpy(samples)

        return waveform, 16000

    except Exception as e:
        st.error(f"Error processing the audio locally: {e}")
        return None, None

def detect_language(text):
    """Detect the language of the transcription using langdetect."""
    return detect(text)

def translate_text(text, src_lang, tgt_lang='en'):
    """Translate the given text using MarianMT."""
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    
    encoded_text = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    translated_tokens = model.generate(**encoded_text, max_length=512, num_beams=5, early_stopping=True)
    translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    
    return translated_text

def process_audio_s3(url):
    """Process the audio file from S3, transcribe and translate if needed."""
    processor = WhisperProcessor.from_pretrained("openai/whisper-large")
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large")

    try:
        response = requests.get(url)
        response.raise_for_status()

        audio_bytes = io.BytesIO(response.content)

        # Load audio using Pydub/FFmpeg
        audio = AudioSegment.from_file(audio_bytes)

        # Convert to mono and 16 kHz
        audio = audio.set_frame_rate(16000).set_channels(1)

        # Convert audio samples to NumPy
        samples = np.array(audio.get_array_of_samples(), dtype=np.float32)

        # Normalize audio samples
        samples /= 2 ** (8 * audio.sample_width - 1)

        # Convert to PyTorch tensor
        waveform = torch.from_numpy(samples)

        # Split into 30-second chunks
        chunks = split_audio(waveform, sample_rate=16000)

        # Transcribe
        full_transcription = transcribe_chunks(
            chunks,
            processor,
            model
        )

        # Detect language
        detected_lang = detect_language(full_transcription)

        # Translate if necessary
        if detected_lang != "en":
            st.write(
                f"Detected language: {detected_lang}. Translating to English..."
            )
            translated_text = translate_text(
                full_transcription,
                detected_lang
            )
            return full_transcription, translated_text

        return full_transcription, None

    except Exception as e:
        st.error(f"Error processing the audio from S3: {e}")
        return None, None
    
def process_local_transcription_and_translation(file_stream):
    """Handle local MP3 processing, transcription, and translation (if needed)."""
    waveform, sample_rate = process_audio_locally_as_mp3(file_stream)
    
    if waveform is None:
        return None, None
    
    processor = WhisperProcessor.from_pretrained("openai/whisper-large")
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large")
    
    # Split audio into chunks for transcription
    chunks = split_audio(waveform, sample_rate=16000)
    
    # Transcribe the chunks
    full_transcription = transcribe_chunks(chunks, processor, model)
    
    # Detect language and translate if necessary
    detected_lang = detect_language(full_transcription)
    
    if detected_lang != 'en':
        st.write(f"Detected language: {detected_lang}. Translating to English...")
        translated_text = translate_text(full_transcription, detected_lang)
        return full_transcription, translated_text
    else:
        return full_transcription, None

def main():
    st.title("Automated Transcription and Translation App")
    
    # Ask user explicitly if they want to upload the file to S3 using radio buttons
    user_choice = st.radio("Do you want to upload the file to S3 for processing?", ("Yes", "No"))
    
    # File uploader
    uploaded_file = st.file_uploader("Upload an Audio File", type=["mp3", "wav", "aac", "flac", "ogg", "wma", "m4a", "aiff", "opus"])
    
    if uploaded_file is not None:
        if user_choice == "Yes":
            # Convert to WAV and upload to S3 if the user chooses Yes
            wav_file_stream = convert_to_wav(uploaded_file)
            
            if wav_file_stream:
                file_path = uploaded_file.name
                object_name = os.path.basename(os.path.splitext(file_path)[0] + ".wav")
                s3_url = upload_file_to_s3_in_memory(wav_file_stream, BUCKET_NAME, object_name)
                
                if s3_url:
                    transcription, translation = process_audio_s3(s3_url)
                    st.write("Transcription:", transcription)
                    if translation:
                        st.write("Translation to English:", translation)
            else:
                st.error("Failed to convert file to WAV for upload to S3.")
        
        else:
            # Process locally as MP3
            transcription, translation = process_local_transcription_and_translation(uploaded_file)
            
            if transcription is not None:
                st.write("Transcription:", transcription)
                if translation:
                    st.write("Translation to English:", translation)
            else:
                st.error("Failed to process the audio locally.")
        
        # Show additional translation options
        st.write("Additional Translation Options:")
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        
        translated_text = None
        
        if col1.button("French"):
            translated_text = f"Translated to French: {translate_text(transcription, 'en', 'fr')}"
        
        if col2.button("Spanish"):
            translated_text = f"Translated to Spanish: {translate_text(transcription, 'en', 'es')}"
        
        if col3.button("German"):
            translated_text = f"Translated to German: {translate_text(transcription, 'en', 'de')}"
        
        if col4.button("Hindi"):
            translated_text = f"Translated to Hindi: {translate_text(transcription, 'en', 'hi')}"
        
        if col5.button("Russian"):
            translated_text = f"Translated to Russian: {translate_text(transcription, 'en', 'ru')}"
        
        if col6.button("Japanese"):
            translated_text = f"Translated to Japanese: {translate_text(transcription, 'en', 'ja')}"
        
        # Display the translated text below the buttons
        if translated_text:
            st.write(translated_text)

if __name__ == "__main__":
    main()
