FROM python:3.9

WORKDIR /app

# RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip
RUN  python3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         -m pip install -r requirements.txt
# RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
#     --grpc_python_out=. ../protobufs/recommendations.proto
COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]
 

                                                                        