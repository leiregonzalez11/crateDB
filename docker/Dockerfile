FROM python:3.7
WORKDIR /app
RUN pip install crate
COPY ./docker/clientapp.py /app/clientapp.py
CMD ["python3", "clientapp.py"]
