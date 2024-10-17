
# Text Summarization App

This project provides a simple web application for summarizing text documents. It utilizes a fine-tuned T5 model to generate summaries and offers a web interface built with Streamlit for ease of use. The application can be accessed both locally and through a cloud deployment.

## Features

- **Text Summarization**: Input a block of text to receive a concise summary.
- **FastAPI & Streamlit Interfaces**: Choose between a FastAPI or Streamlit-based interface for interacting with the model.

## Project Structure

- `/app`:
  - `main.py`: Contains the FastAPI app setup for deployment.
  - `streamlit.py`: Streamlit app for a more interactive front-end.
  - `model_function.py`: Defines the function that takes text input and outputs a summary.
  - `t5-small-fine-tuning.ipynb`: Jupyter notebook for fine-tuning and evaluating the summarization model.
- `requirements.txt`: Lists all Python libraries that the project depends on.
- `Dockerfile`: Container configuration file.

## Installation

To set up this project locally, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/summarization-app.git
    cd summarization-app
    ```

2. **Create a Virtual Environment (Optional)**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**

    - **Using Streamlit:**

      ```bash
      streamlit run app/streamlit.py
      ```

    - **Using FastAPI:**

      ```bash
      uvicorn app.main:app --reload
      ```

## Usage

To use the app, you can either navigate to the local URL provided by Streamlit or FastAPI after running it locally, or you can access it directly through the cloud deployment:

- **Cloud Deployment**: [Text Summarization App](https://depi-summarization.streamlit.app/)

Enter the text you want to summarize in the input box and click the `Summarize` button. The summary will appear shortly.

## Deployment

This application is containerized using Docker. To build and run the Docker container, execute:

```bash
docker build -t summarization-app .
docker run -p 8501:8501 summarization-app
```

This will build the Docker image and run it, making the app accessible via `localhost:8501` if using Streamlit.

## Team Members

- Saad Al-Tohamy
- Ahmed Shetia
- Sayed Gamal
- Mohamed Ayman
- Esraa Rabea
- Reem Gamal

## License

This project is licensed under the MIT License - see the LICENSE file for details.

