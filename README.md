# Multi-Agent
# AI Agents Suite 🤖

A Streamlit-based application featuring multiple AI-powered agents for code analysis, documentation generation, and software engineering tasks. Built with LangChain and OpenAI.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://yourapp-url.streamlit.app/)

![Demo](assets/demo.gif) <!-- Add demo GIF later -->

## Features

### Code Agents
- **Code Comparator**: Compare two code files and highlight differences
- **Code Optimizer**: Improve code efficiency and readability
- **Unit Test Generator**: Create test cases in various frameworks
- **Code Reviver**: Modernize legacy codebases

### Documentation Agents
- **SRS Generator**: Create Software Requirements Specifications
- **SDD Generator**: Build Software Design Documents
- **Auto Documentation**: Generate code documentation in multiple styles
- **Architecture Generator**: Create system diagrams from descriptions

### Specialized Tools
- **Prompt Engineer**: Optimize and refine AI prompts
- **Code Explainer**: Get detailed code analysis
- **Documentation Assistant**: Generate technical docs from requirements

## Installation

1. **Prerequisites**:
   - Python 3.8+
   - OpenAI API key

2. **Clone repository**:
   ```bash
   git clone https://github.com/yourusername/ai-agents-suite.git
   cd ai-agents-suite
Install dependencies:

bash
Copy
pip install -r requirements.txt
Run the application:

bash
Copy
streamlit run main_app.py
Usage
Launch the application

Enter your OpenAI API key in the sidebar

Select an agent from the sidebar menu

Upload files or input prompts as required

View and download generated results

UI Screenshot <!-- Add screenshot -->

Configuration
Sidebar Settings
API Key Management: Securely input OpenAI credentials

Model Selection: Choose between GPT-3.5 and GPT-4

Temperature Control: Adjust creativity vs determinism

Supported Formats
Code Files: .py, .js, .java, .c, .cpp

Documents: .txt, .md

Contributing
We welcome contributions! Please follow these steps:

Fork the repository

Create your feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add some amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

License
Distributed under the MIT License. See LICENSE for more information.

Acknowledgments
OpenAI for the GPT models

LangChain team for the AI orchestration framework

Streamlit for the awesome web app framework

ChromaDB for vector storage solutions

PlantUML for diagram generation
