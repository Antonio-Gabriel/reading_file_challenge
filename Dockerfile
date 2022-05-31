FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /extracting-file

COPY requirements.txt /extracting-file/


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /extracting-file/

expose 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]