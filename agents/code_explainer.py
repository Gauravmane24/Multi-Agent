import streamlit as st
from agents.utils import handle_file_upload,create_chain
def code_explainer():
    code = handle_file_upload("Upload Code to Explain", ["py", "js", "java"])
    if code:
        chain = create_chain("""
        Explain this code in detail:
        {code}
        
        Include:
        1. Functionality Overview
        2. Algorithm Explanation
        3. Complexity Analysis
        4. Potential Improvements
        """, ["code"])
        st.markdown(chain.run(code=code))