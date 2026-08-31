import streamlit as st
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains.question_answering import load_qa_chain
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document

os.environ["GOOGLE_API_KEY"] = "AIzaSyByD2DGdJdAtCS3r2ixLzuMjo7RGRM_Ct8"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_conversational_chain():
    prompt_template = """
    The context you are going to be provided is a Transcription from an Audio or Video file.
    Answer the question as detailed as possible from the provided context, and make sure to provide all the details. 
    If the answer is not related to the provided context just say, "I can't help with that but I can help with the Transcription."
    Do not provide an incorrect answer. Answer in the same language as the context.\n\n
    Context:\n {context}\n
    Question: \n{question}\n
    Answer:
    """
    
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question, context):
    chain = get_conversational_chain()
    docs = [Document(page_content=context)]
    
    try:
        with st.spinner("Generating response..."):
            response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
            st.write("**Reply:**", response["output_text"])
    except Exception as e:
        st.error(f"Error generating response: {e}")

def main():
    st.set_page_config(page_title="LLM Transcription Chat", layout="wide")
    st.header("Explore and Discuss the Transcription")

    user_question = st.text_input("Ask a question about the transcription")

    use_translation = st.checkbox("Use Translation")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Content")
        if use_translation:
            if "translation" in st.session_state:
                st.write("**Translation:**")
                st.write(st.session_state["translation"])
            else:
                st.info("No translation available.")
        else:
            if "transcription" in st.session_state:
                st.write("**Transcription:**")
                st.write(st.session_state["transcription"])
            else:
                st.info("No transcription available.")
                
    with col2:
        if user_question:
            context = st.session_state.get("translation") if use_translation else st.session_state.get("transcription")
            if context:
                user_input(user_question, context)
            else:
                st.warning("Please provide a transcription or translation first.")

if __name__ == "__main__":
    main()
