FROM python:3.10
WORKDIR /task
COPY task /task
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python", "/task/__init__.py"]
