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

EXPOSE 8501

# Command to run the app (replace 'app.py' with your app script)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.headless=true"]
