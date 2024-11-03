import streamlit as st
import pymupdf
from scripts.llm import ask_llm, validate_json

st.title("Resume Parser")
st.write("This application allows you to extract key information from a resume.")

uploaded_file = st.file_uploader("Upload a resume", type=["pdf"])
if uploaded_file is not None:
    bytearray = uploaded_file.read()
    pdf = pymupdf.open(stream=bytearray, filetype="pdf")
    
    context = ""
    for page in pdf:
        context = context + "\n\n" + page.get_text()
    pdf.close()
    # st.write(context)


question = """You are tasked with parsing a job resume. Your goal is to extract relevant information in a valid structured 'JSON' format. 
                Do not write preambles or explanations."""

if st.button("Extract Information"):
    with st.spinner("Extracting information..."):
        response = ask_llm(context=context, question=question)

    with st.spinner("Validating extracted information..."):
        response = validate_json(response)
        
    st.write("**Extracted Information:**")
    st.write(response)

    # decorate final output
    st.balloons()