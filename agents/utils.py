from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import streamlit as st

def get_api_key():
    """Get API key from user input"""
    if 'api_key' not in st.session_state:
        st.session_state.api_key = None
    
    # Create a sidebar section for API key input
    with st.sidebar:
        st.subheader("OpenAI API Configuration")
        api_key = st.text_input(
            "Enter your OpenAI API key:",
            type="password",
            help="You can get your API key from https://platform.openai.com/account/api-keys",
            value=st.session_state.api_key or ""
        )
     
        
        if api_key:
            st.session_state.api_key = api_key
            st.success("API key saved successfully!")
        elif st.session_state.api_key:
            st.info("Using previously entered API key")
        else:
            st.warning("Please enter your API key to continue")
    
    return st.session_state.api_key

# Add this at the top of your script, after the imports
if 'user_input' not in st.session_state:
    st.session_state.user_input = ''

def init_llm(temp=0.7):
    """Initialize LLM with user-provided API key"""
    api_key = get_api_key()
    if not api_key:
        st.error("API key is required to proceed")
        st.stop()
    return OpenAI(temperature=temp, openai_api_key=api_key)

def create_chain(template, input_vars, llm=None):
    """Create LLM chain with API key validation"""
    try:
        prompt = PromptTemplate(template=template, input_variables=input_vars)
        return LLMChain(prompt=prompt, llm=llm or init_llm())
    except Exception as e:
        st.error(f"Error initializing LLM: {str(e)}")
        st.stop()

def handle_file_upload(label, accept_types):
    """Handle file uploads with progress indication"""
    uploaded_file = st.file_uploader(label, type=accept_types)
    if uploaded_file:
        with st.spinner(f"Processing {uploaded_file.name}..."):
            content = uploaded_file.getvalue().decode()
        st.success("File processed successfully!")
        return content
    return None