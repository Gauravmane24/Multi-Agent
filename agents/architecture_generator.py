import streamlit as st
from agents.utils import create_chain
def architecture_generator():
    description = st.text_area("Enter system description")
    if description:
        chain = create_chain("""
        Generate PlantUML code for system architecture based on:
        {description}
        """, ["description"])
        uml_code = chain.run(description=description)
        st.image(f"http://www.plantuml.com/plantuml/png/{uml_code}")