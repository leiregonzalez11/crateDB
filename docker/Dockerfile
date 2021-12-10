FROM python:3.7
WORKDIR /app
RUN pip install crate
COPY ./clientapp.py /app/clientapp.py
CMD ["python", "clientapp.py"]
