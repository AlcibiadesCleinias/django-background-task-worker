FROM python:3.9.6-alpine

WORKDIR /opt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update

RUN pip install --upgrade pip
COPY requirements.txt /opt/.
RUN pip install -r /opt/requirements.txt

COPY src/entrypoint.sh /opt/.

COPY src/ /opt/

ENTRYPOINT ["/opt/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
