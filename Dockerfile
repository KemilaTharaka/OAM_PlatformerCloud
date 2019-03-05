FROM python:2.7

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY static ./
COPY templates ./
RUN pip install --no-cache-dir -r requirements.txt



COPY . .
EXPOSE 5000
CMD [ "python", "main.py" ]
