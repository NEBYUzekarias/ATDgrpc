# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging

import grpc
import json
import csv
import pandas
import io



import atd_pb2
import atd_pb2_grpc

class Client():
    def __init__(self, port='localhost:50051'):
        self.port = port
        self.image =None
      
    def open_grpc_chunnel(self):
        channel = grpc.insecure_channel(self.port)
        stub = atd_pb2_grpc.ImageClassStub(channel)
        return stub

    def send_request(self ,  stub , image):
        self.image = image 
      

        
        
        

        print(type(self.image))
        message = atd_pb2.GrpcRequest(image= image)

        response = stub.getStage(message)
        print("send_requests")


    
        return response
    

    

if __name__ == '__main__':
    logging.basicConfig()
    client = Client()

    stub = client.open_grpc_chunnel()
    resp = client.send_request(stub, "blalbla")
    print (resp)
    #run()
