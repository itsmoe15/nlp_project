# NLP Text Classification App

A Streamlit-based application for categorizing text using a pre-trained spaCy model.

## Features

- Clean, modern UI with Streamlit
- Text input via direct pasting
- PDF upload with drag-and-drop functionality
- Classification results displayed with confidence scores
- Interactive visualization of results

## Setup and Installation

1. Install required packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## How to Use

1. Enter text directly in the text input area or upload a PDF file
2. Click "Classify Text" to get categorization results
3. View the top predicted categories and their confidence scores

## Model

The app uses a pre-trained spaCy model located in the `Model/textcat` directory.
