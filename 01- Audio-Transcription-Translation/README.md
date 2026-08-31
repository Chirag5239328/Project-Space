# Audio Transcription and Translation Application

## Overview

This project is an audio transcription and translation application developed as my individual capstone project.

The project initially started from a personal communication problem. I found it difficult to communicate seamlessly through audio messages, which led me to explore whether audio could be converted into text and then translated when required.

The initial idea was simply to upload an audio file and receive a transcription. However, I felt that a transcription-only application would be relatively limited. I therefore expanded the project to include language handling, translation and cloud storage so that it could potentially be used by people with different language requirements.

The application was developed using pretrained models rather than training speech or translation models from scratch.

---

## Problem

The initial problem I wanted to address was difficulty communicating through audio messages.

I wanted a way to upload an audio file, convert the spoken content into text and, when required, translate that content into another language.

During the development process, I also considered that a public application could receive audio files in languages other than English. This led to the addition of language handling and translation functionality.

---

## Objective

The main objectives of the project were to:

- Convert audio files into text.
- Identify whether the uploaded audio was in English or another language.
- Provide transcription in the original language where possible.
- Translate non-English audio into English.
- Allow users to translate the resulting English text into another desired language.
- Store uploaded files using cloud storage.
- Create a simple interface through which the complete process could be performed.

---

## Application Workflow

The final application follows this general workflow:

Audio File
    |
    v
File Upload
    |
    v
AWS Storage
    |
    v
Language Handling
    |
    +----------------------+
    |                      |
    v                      v
English              Other Language
    |                      |
    v                      v
Whisper               Whisper
Transcription         Transcription
    |                      |
    |                      v
    |                Translate to English
    |                      |
    +----------+-----------+
               |
               v
         Display Text
               |
               v
    Optional Translation
               |
               v
       Desired Language

For non-English audio, the application initially displays the transcription in the original language together with its English translation.

For subsequent translation, the English text is retained as the common intermediate representation.

---

## How It Works

### 1. Audio Upload

The user uploads an audio file through the Streamlit interface.

The uploaded file is stored using AWS so that it can be accessed during the subsequent processing stages.

### 2. Language Handling

The application checks whether the uploaded audio is in English or another language.

The processing path then depends on the detected language.

### 3. Transcription

Whisper is used as the pretrained speech-to-text model.

The audio is converted into textual content while attempting to preserve the spoken language.

### 4. Translation

For non-English audio, the application translates the resulting text into English.

MarianMT pretrained translation models from Hugging Face were used for the translation component.

The English text is then used as the common text representation for any further translation requested by the user.

### 5. User Translation

After transcription and, where required, translation into English, the user can select another language for translation.

---

## Technologies Used

### Programming Language

- Python

### Application Interface

- Streamlit

### Speech-to-Text

- Whisper

### Machine Translation

- MarianMT
- Hugging Face pretrained models

### Cloud

- AWS

---

## My Role

This was an individual project, so I was responsible for the development and integration of the complete application.

My work included:

- Designing the application workflow
- Integrating the pretrained models
- Developing the Streamlit interface
- Implementing audio processing
- Integrating AWS cloud storage
- Handling different language scenarios
- Integrating transcription and translation
- Testing the application using different audio samples
- Troubleshooting issues during integration

---

## Development Process

The project initially consisted of a much simpler idea:

Audio File
    |
    v
Transcription
    |
    v
Text

As I worked on the project, I realised that this would have limited practical use if the application were made available to other users.

A user could upload an audio file in a language that I could not assume in advance. This led me to expand the project to handle multiple languages and translation.

I also introduced cloud storage so that the uploaded file could be retained during the processing workflow.

This resulted in the broader application:

Audio
  |
  v
Language Handling
  |
  v
Transcription
  |
  v
English Translation when required
  |
  v
User-selected Translation

---

## Testing

I tested the application using audio samples collected from publicly available sources.

The test material included:

- Randomly sourced audio files
- Audio extracted from publicly available videos
- TED Talk-style speech recordings
- Different languages
- Mixed-language and Hinglish-style speech

The testing was particularly useful for understanding the limitations of pretrained models when they were exposed to audio that differed from ideal or standard inputs.

---

## Challenges

### Transcription Accuracy

One of the main challenges was achieving consistent transcription accuracy.

The application achieved approximately 75-80% accuracy in my testing, although performance varied depending on the audio.

### Hindi and Hinglish Audio

The application did not perform particularly well with Hindi audio.

Hinglish and mixed-language speech also presented difficulties because the audio could contain switching between languages within the same recording.

### Model Limitations

Since the project relied on pretrained models rather than models trained specifically for the dataset or use case, the quality of the output depended considerably on the characteristics of the input audio.

### Cloud Integration

The application was initially developed without cloud storage.

Introducing AWS later required changes to parts of the existing workflow and integration, which was one of the more difficult parts of the development process.

### Integration

Individually, the different components were manageable. Integrating transcription, language handling, translation, cloud storage and the user interface into one workflow was considerably more challenging.

---

## Key Learnings

This project helped me understand that building an application around pretrained models involves more than simply obtaining predictions from a model.

Some of my main learnings were:

- How speech-to-text systems can be integrated into applications.
- How pretrained NLP models can be incorporated into a practical workflow.
- How translation can be added as a layer on top of transcription.
- The importance of handling different types of user input.
- The practical challenges of multilingual and mixed-language audio.
- How cloud storage can be integrated into an application workflow.
- How changing the requirements of a project can affect its architecture.
- The difference between getting an individual component to work and integrating several components into a complete application.
- The importance of testing a system with varied real-world inputs.

---

## Limitations

The project was developed as an academic capstone and therefore has several limitations.

- Transcription accuracy was not consistently high for every type of audio.
- Hindi audio was not handled particularly well.
- Hinglish and mixed-language speech presented additional difficulties.
- The application depended on the capabilities and limitations of the pretrained models.
- The project was tested using a limited collection of audio samples.
- The application was not developed as a production-scale commercial service.

---

## Future Improvements

Possible improvements to the project include:

- Improving transcription accuracy for Indian languages.
- Better handling of Hinglish and code-switching.
- Supporting a wider range of languages.
- Improving translation quality.
- Adding better audio preprocessing for noisy recordings.
- Improving error handling.
- Improving the user interface.
- Adding more robust cloud-based processing.
- Testing the application on a larger and more diverse dataset.

---

## Project Structure

The repository contains the implementation and supporting material for the project.

01-capstone-audio-transcription-translation/
|
├── README.md
├── src/
├── requirements.txt
├── screenshots/
└── sample/

---

## Project Paper

A technical paper was written based on this project as part of my undergraduate academic work.

The paper was not published.

---

## Academic Context

This project was completed as an individual capstone project during my undergraduate degree in Data Science.

The project was particularly useful to me because it started with a problem I personally experienced and gradually developed into a broader application by considering how the same solution could potentially be useful to other users.

---

## Disclaimer

This project is an academic implementation and should not be considered a production-ready transcription or translation service.

Model performance can vary depending on the language, audio quality, accent, background noise and characteristics of the recording.
