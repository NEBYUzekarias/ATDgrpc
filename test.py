import unittest
from atd_server import Server 
from atd_client import Client
import json
import pandas as pd 
import cv2
import numpy as np
import pickle
class TestGrpc(unittest.TestCase):


    def setUp(self, image="labels"):

        self.image = cv2.imread('data/image 3.png',1)

        self.image = cv2.resize(self.image,(299,299), interpolation = cv2.INTER_CUBIC)
        self.image = np.array(self.image)
        self.image =pickle.dumps(self.image)

        
        self.server = Server()
        self.server.start_server()
        print("start ser")
        self.client = Client()



    def test_grpc_call(self):
        self.stub = self.client.open_grpc_chunnel()

        stub = self.client.open_grpc_chunnel()
        

        response = self.client.send_request(stub,self.image)
        print("client")
      
        self.assertEqual(response.stage,"image" )
        self.assertEqual(response.stageAcc, 50)

      
        
    def tearDown(self):
        # self.client.channel.close()
        self.server.stop_server()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestGrpc("test_grpc_call"))
    unittest.main()