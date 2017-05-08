from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serialize import PosisiSerialize
import logging

class Posisi(APIView):
    def get(self):
        pass
    def post(self, request):
        logging.warning(request.data)
        return Response({"Status" : "OK"}, status=status.HTTP_201_CREATED)
        

