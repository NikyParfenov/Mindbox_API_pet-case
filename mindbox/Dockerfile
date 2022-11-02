FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /usr/src/mindbox

COPY  ./requirements.txt /usr/src/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/mindbox

EXPOSE 8000