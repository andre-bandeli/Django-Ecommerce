
FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /store
ADD requirements.txt /store/
RUN pip install -r requirements.txt
ADD . /store/