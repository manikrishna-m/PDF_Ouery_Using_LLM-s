# MCQs Creator Application with LangChain

## Overview

This project is a Multiple Choice Questions (MCQs) Creator Application powered by LangChain. The application allows users to generate MCQs based on the content of a PDF or text file. The generated questions are tailored to a specific subject and tone specified by the user.

## Features

- **PDF or Text File Input:** Users can upload a PDF or text file containing the content for which they want to generate MCQs.

- **Customization:** Users can specify the number of MCQs to be generated, the subject, and the tone for the questions.

- **LangChain Integration:** The application utilizes LangChain, a language model, to intelligently generate and evaluate MCQs based on the provided content.

- **User Interaction:** After generating the MCQs, the application presents the questions to the user for interaction. Users can select their answers, and the application provides feedback on their performance.

## Getting Started

1. **Clone the Repository:**
    ```bash
    git clone "{{http link}}"
    cd mcq-creator-langchain
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**
    ```bash
    streamlit run StreamlitAPP.py
    ```

4. **Upload File and Generate MCQs:**
   - Access the application in your web browser.
   - Upload a PDF or text file.
   - Specify the number of MCQs, subject, and tone.
   - Click the "Generate MCQs" button.

5. **Interact with the Quiz:**
   - The application presents the generated MCQs to the user.
   - Users can select their answers for each question.
   - Click the "Submit Answers" button to evaluate the responses.

## Dependencies

- Streamlit
- LangChain
- Other dependencies listed in `requirements.txt`

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [LangChain](link-to-langchain) for providing the language model and callback integration.
- [Streamlit](https://streamlit.io/) for the user interface framework.

Feel free to contribute, report issues, or suggest improvements!
