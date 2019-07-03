from concurrent import futures
import time
import logging

import grpc
import json
import csv
import pandas as pd 
import io 
import base64
from PIL import Image
import pickle
import numpy as np
import atd_pb2
import atd_pb2_grpc
import cv2 

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class AtdServicer(atd_pb2_grpc.ImageClassServicer):
    
    def getStage(self, request, context):
        image = request.image
        # var =(bytes(image))
        print(type(image))
        imgdata = base64.b64decode(str(image))
        # image = Image.open(io.BytesIO(imgdata))
        # byt = pickle.loads(image)
        # nparr = np.frombuffer(image, dtype=np.uint32)
        # print("size",image)
        path = "data/img"+ time.strftime("%Y%m%d-%H%M%S")+".png"

        f = open(path, 'wb')
        f.write(bytearray(image))
        f.close()
        # filename = 'some_image.png'  # I assume you have a way of picking unique filenames
        # with open(filename, 'wb-') as f:
        #     f.write(imgdata)
        # print(nparr.size)
        # nparr =  cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
        # print("in server")
        # print(type(nparr))
        # path = "img"+ time.strftime("%Y%m%d-%H%M%S")
        # cv2.imwrite('misgana.png',byt)

     

        
    
        return atd_pb2.GrpcReply(stage="Stage bla",
                                stageAcc=50)
    def save(self, encoded_data, filename):

        nparr = np.fromstring(encoded_data.decode('base64'), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)
        return cv2.imwrite(filename, img)

class Server():
    def __init__(self):
        self.port = '[::]:50051'
        self.server = None

    def start_server(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        atd_pb2_grpc.add_ImageClassServicer_to_server(AtdServicer(), self.server)
        print('Starting server. Listening on port 50051.')
        self.server.add_insecure_port(self.port)
        self.server.start()

    def stop_server(self):
        self.server.stop(0)




if __name__ == '__main__':
    server = Server()
    server.start_server()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop_server()