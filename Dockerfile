FROM amazonlinux

ENV PYTHONUNBUFFERED=1

RUN yum update -y
RUN yum upgrade -y
RUN yum groupinstall "Development Tools" -y
RUN yum install python3-devel -y
RUN yum install which -y
RUN python3 -m pip install --upgrade pip

COPY app app
COPY .env .env
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt --no-cache-dir

EXPOSE 8000
CMD gunicorn app.main:APP --bind="0.0.0.0:8000"
