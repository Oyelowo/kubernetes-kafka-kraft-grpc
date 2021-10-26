FROM python:3.9

WORKDIR /app

# COPY protobufs/ /app/protobufs/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
#     --grpc_python_out=. ../protobufs/recommendations.proto

EXPOSE 50053

COPY . .
CMD ["python3", "./app/server.py"]
