import streamlit as st
from .utils import *

def code_comparator():
    st.header("Code Comparator Agent")
    col1, col2 = st.columns(2)
    
    with col1:
        code1 = handle_file_upload("Upload First Code File", ["py", "js", "java"])
    with col2:
        code2 = handle_file_upload("Upload Second Code File", ["py", "js", "java"])
    
    if code1 and code2:
        chain = create_chain("""
        Compare these two code snippets and highlight key differences:
        Code 1: {code1}
        Code 2: {code2}
        
        Provide analysis in this format:
        1. Structural Differences
        2. Functional Differences
        3. Optimization Opportunities
        4. Potential Issues
        """, ["code1", "code2"])
        
        result = chain.run(code1=code1, code2=code2)
        st.subheader("Comparison Results")
        st.markdown(result)

def code_optimizer():
    st.header("Code Optimization Agent")
    code = handle_file_upload("Upload Code to Optimize", ["py", "js", "java"])
    
    if code:
        chain = create_chain("""
        Optimize this code and explain improvements:
        {code}
        
        Provide response with:
        1. Optimized Code
        2. List of Improvements
        3. Performance Metrics Estimation
        """, ["code"])
        
        result = chain.run(code=code)
        st.subheader("Optimization Results")
        st.code(result.split("```")[1] if "```" in result else result)

# Similar implementations for other code agents...
def unit_test_generator():
    st.header("Unit Test Generator Agent")
    code = handle_file_upload("Upload Code for Test Generation", ["py", "js", "java"])
    test_framework = st.selectbox("Select Testing Framework", ["pytest", "unittest", "JUnit", "Jest"])
    
    if code and st.button("Generate Tests"):
        chain = create_chain("""
        Generate comprehensive unit tests for this code using {framework}:
        {code}
        
        Include:
        1. Test cases for all main functions
        2. Edge cases
        3. Mocking where appropriate
        4. Assertions with clear messages
        """, ["code", "framework"])
        
        result = chain.run(code=code, framework=test_framework)
        st.subheader("Generated Test Cases")
        st.code(result.split("```")[1] if "```" in result else result)

def code_reviver():
    st.header("Code Reviver Agent")
    code = handle_file_upload("Upload Legacy Code", ["py", "js", "java", "c"])
    target_language = st.selectbox("Target Language Version", 
                                ["Python 3.11", "Java 17", "ES6+", "Modern C++"])
    
    if code:
        chain = create_chain("""
        Modernize and revive this legacy code for {target}:
        {code}
        
        Provide:
        1. Updated code with modern syntax
        2. List of deprecated features replaced
        3. Security improvements
        4. Performance optimizations
        5. Compatibility notes
        """, ["code", "target"])
        
        result = chain.run(code=code, target=target_language)
        st.subheader("Revived Code")
        st.code(result.split("```")[1] if "```" in result else result)