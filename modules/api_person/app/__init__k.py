# from concurrent import futures
# import grpc

# from protobuf import person_pb2, person_pb2_grpc
# # from .protobuf import person_pb2, person_pb2_grpc
# from .grpc import PersonServicer


# class Server:

#     @staticmethod
#     def run():
#         server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#         person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServicer(), server)
#         server.add_insecure_port('[::]:50051')
#         server.start()
#         server.wait_for_termination()
