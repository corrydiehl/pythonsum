FROM python:alpine
WORKDIR /usr/src/app
COPY sum.py /usr/src/app/sum.py
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 3000
CMD ["python", "sum.py"]