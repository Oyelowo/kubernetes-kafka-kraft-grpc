FROM python:3.7-alpine

ARG PASS="d293aW1zb3NlY3VyZQ==" | base64 -d
RUN echo $PASS
ENV DB_USERNAME=ct_admin
ENV DB_PASSWORD=$PASS
ENV DB_NAME=geoconnections
ENV DB_HOST=postgres
ENV DB_PORT=5432

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
