FROM python:3.9-slim

# Set the working directory
WORKDIR /code

# Copy the requirements file into the container at /code
COPY ./requirements.txt /code/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /code
COPY ./app /code/app

# Environment variable to include your code in Python path
ENV PYTHONPATH=/code/app

# Expose ports for both Streamlit and FastAPI
EXPOSE 8501 8000

# Run both Streamlit and FastAPI apps
CMD ["sh", "-c", "uvicorn api:app --host 0.0.0.0 --port 8000 & streamlit run streamlit.py --server.port 8501"]
