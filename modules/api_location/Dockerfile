FROM python:3.9
ARG PASS="d293aW1zb3NlY3VyZQ==" | base64 -d
RUN echo $PASS
ENV DB_USERNAME=ct_admin
ENV DB_PASSWORD=$PASS
ENV DB_NAME=geoconnections
ENV DB_HOST=postgres
ENV DB_PORT=5432

WORKDIR /app

#RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN python3 -m pip install --upgrade setuptools
#RUN pip3 install --no-cache-dir  --force-reinstall -Iv grpcio==1.41.0


RUN python3 -m  pip install -r requirements.txt


EXPOSE 50052

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
