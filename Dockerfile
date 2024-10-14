FROM python:3.13

WORKDIR /app

# Install dependencies
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Install app code
COPY . .

CMD [ "make", "serve" ]