FROM python:3.7
WORKDIR /app
RUN apt-get -qq update
RUN apt-get install -qq -y python3-pip
RUN pip3 install crate
COPY clientapp-volumes.py /app/clientapp-volumes.py
CMD ["python3", "clientapp.py"]
