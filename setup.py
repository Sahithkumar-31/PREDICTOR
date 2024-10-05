from setuptools import setup, find_packages

setup(
    name = "env",
    version = "0.0.1",
    author = "sahith",
    install_requires = ["openai","langchain","streamlit","PyPDF2","pandas","langchain_community","python-dotenv"],
    packages = find_packages()
    
    )