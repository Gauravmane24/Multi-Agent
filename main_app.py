import streamlit as st
from agents.code_agent import (
    code_comparator,
    code_optimizer,
    unit_test_generator,
    code_reviver
)
from agents.doc_agent import (
    srs_generator,
    sdd_generator,
    prompt_engineer,
    documentation_generator
)
from agents.architecture_generator import ( architecture_generator)
from agents.code_explainer import ( code_explainer)         

st.set_page_config(page_title="AI Agent Suite", layout="wide")

def main():
    st.sidebar.title("AI Agent Suite")
    agent_choice = st.sidebar.selectbox(
        "Choose Agent",
        ["Code Comparator", "Code Optimizer", "Unit Test Generator",
         "Code Reviver", "SRS Generator", "SDD Generator",
         "Prompt Engineer", "Documentation Generator","architecture_generator","code_explainer"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("Upload files and enter prompts as needed for each agent")

    if agent_choice == "Code Comparator":
        code_comparator()
    elif agent_choice == "Code Optimizer":
        code_optimizer()
    elif agent_choice == "Unit Test Generator":
        unit_test_generator()
    elif agent_choice == "Code Reviver":
        code_reviver()
    elif agent_choice == "SRS Generator":
        srs_generator()
    elif agent_choice == "SDD Generator":
        sdd_generator()
    elif agent_choice == "Prompt Engineer":
        prompt_engineer()
    elif agent_choice == "Documentation Generator":
        documentation_generator()
    elif agent_choice == "architecture_generator":
        architecture_generator()
    elif agent_choice == "code_explainer":
        code_explainer()

if __name__ == "__main__":
    main()