from setuptools import find_packages,setup

setup(
    name = "MCQ's Generator using LLM's",
    version= "0.0.1",
    author = "Mani Krishna",
    author_email= "mandepudi.mk@gmail.com",
    install_requires = ["openai","langchain","streamlit","python-dotenv","PyPDF2"] ,
    packages = find_packages
)