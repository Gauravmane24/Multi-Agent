import streamlit as st
from .utils import *

def srs_generator():
    st.header("SRS Document Generator")
    requirements = st.text_area("Enter System Requirements")
    
    if st.button("Generate SRS"):
        chain = create_chain("""
        Generate Software Requirements Specification document based on:
        {requirements}
        
        Follow IEEE 830 format including:
        1. Introduction
        2. Overall Description
        3. System Features
        4. External Interface Requirements
        5. Non-Functional Requirements
        """, ["requirements"])
        
        result = chain.run(requirements=requirements)
        st.download_button("Download SRS", result, file_name="SRS.md")

def prompt_engineer():
    st.header("Prompt Engineering Agent")
    user_prompt = st.text_area("Enter your initial prompt")
    
    if user_prompt:
        chain = create_chain("""
        Improve this prompt using best practices in prompt engineering:
        Original Prompt: {prompt}
        
        Provide:
        1. Improved Prompt
        2. Explanation of Changes
        3. Suggested Usage Examples
        """, ["prompt"])
        
        result = chain.run(prompt=user_prompt)
        st.subheader("Optimized Prompt")
        st.code(result)

# Similar implementations for other document agents...
def sdd_generator():
    st.header("Software Design Document Generator")
    system_description = st.text_area("Enter System Architecture Description")
    diagram_type = st.selectbox("Select Diagram Type", ["UML", "Flowchart", "ERD", "Sequence"])
    
    if st.button("Generate SDD"):
        chain = create_chain("""
        Create a Software Design Document (SDD) based on:
        {description}
        
        Follow IEEE 1016 format including:
        1. Design Overview
        2. System Architecture
        3. Data Design
        4. Component Design
        5. Interface Design
        6. {diagram} Diagram Explanation
        """, ["description", "diagram"])
        
        result = chain.run(description=system_description, diagram=diagram_type)
        st.subheader("Software Design Document")
        st.markdown(result)
        st.download_button("Download SDD", result, file_name="SDD.md")

def documentation_generator():
    st.header("Code Documentation Generator")
    code = handle_file_upload("Upload Code to Document", ["py", "js", "java"])
    doc_style = st.selectbox("Documentation Style", ["Google Style", "JSDoc", "JavaDoc", "Sphinx"])
    
    if code:
        chain = create_chain("""
        Generate comprehensive documentation for this code using {style}:
        {code}
        
        Include:
        1. Module/Class overview
        2. Function/method descriptions
        3. Parameter details
        4. Return value explanations
        5. Usage examples
        6. Error handling documentation
        """, ["code", "style"])
        
        result = chain.run(code=code, style=doc_style)
        st.subheader("Generated Documentation")
        st.markdown(result)
        st.download_button("Download Docs", result, file_name="DOCUMENTATION.md")