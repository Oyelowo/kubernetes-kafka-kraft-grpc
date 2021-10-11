FROM python:3.9

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
