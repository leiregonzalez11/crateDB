FROM python:3.7
WORKDIR /app
RUN apt-get -qq update
RUN apt-get install -qq -y python3-pip
RUN pip3 install crate
COPY clientapp.py /app/clientapp.py
CMD ["python3", "clientapp.py"]
