# Anthropod Assignment: Movie review sentiment

This repository contains a Streamlit web application that leverages the Google Gemini API to classify movie review as 
positive negative or neutral and also provides a confidence score and a short explanation for its reasoning.

## Features

* Interactive web interface built with Streamlit.
* Powered by the Google Gemini Flash model.
* Json Cache file to reduce cost.

## Local Development Setup

Follow these steps to run the application on your local machine.

### 1. Clone the Repository

```bash
git clone [https://github.com/VanshDhoka/anthropod-assignment.git](https://github.com/VanshDhoka/anthropod-assignment.git)
cd anthropod-assignment
````

### 2\. Create a Virtual Environment (Recommended)

It's a good practice to create a virtual environment to manage project dependencies.

**For macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**For Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3\. Install Dependencies

Install all the required Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4\. Set Up Environment Variables

The application requires your Gemini API key.

1.  Create a new file named `.env` in the root of the project directory.
2.  Add your API key to this file as shown below:
    ```env
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
    ```
3.  **Important:** For local execution, you need to remove or comment out line 6 in the `streamlit_app.py` file. This line is intended for deployment on Streamlit Cloud, which uses a different secret management system.
    ```python
    #GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY")
    ```

### 5\. Run the Streamlit App

Once the setup is complete, you can start the Streamlit server.

```bash
streamlit run streamlit_app.py
```

The application will now be running and accessible in your web browser, typically at `http://localhost:8501`.
