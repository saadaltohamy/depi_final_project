FROM python:3.9-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /code/app

ENV PYTHONPATH=/code/app

EXPOSE 8501

CMD ["streamlit", "run", "app/summaryfiles.py", "--server.port=8501", "--server.headless=true"]
