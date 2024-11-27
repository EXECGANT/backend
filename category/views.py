from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializer
from library.crud_operations import CRUDOperations
from library.savefile import saveFile
from django.http import QueryDict

class CategoryView(APIView):
    
    def get(self, request):
        response = CRUDOperations.getAllData(model=models.CategoryModel, serializer=serializer.CategorySerializer)
        return Response(response, status=status.HTTP_200_OK)
    
    def post(self, request):
        category_details={
            **request.POST.dict(),
            'category_image' : 'image'
        }
        check_serializer=serializer.CategorySerializer(data=category_details)
        if check_serializer.is_valid():
            category_details['category_image']=saveFile(path="category",file=request.FILES['category_image'])
            response = CRUDOperations.addNewData(serializer=serializer.CategorySerializer, data=category_details)
            if response['status']:
                return Response(response['data'],status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id):
        if 'category_image' in request.POST:
            response = CRUDOperations.updateExistingData(model=models.CategoryModel, serializer=serializer.CategorySerializer, data=request.data, id=id)
            if response['status']:
                return Response(response['data'],status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            category_details={
            **request.POST.dict(),
            'category_image' : 'image'
            }
            check_serializer=serializer.CategorySerializer(data=category_details)
            if check_serializer.is_valid():
                category_details['category_image']=saveFile(path="category",file=request.FILES['category_image'])
                response = CRUDOperations.updateExistingData(model=models.CategoryModel, serializer=serializer.CategorySerializer, data=category_details, id=id)
                if response['status']:
                    return Response(response['data'],status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, id):
        response = CRUDOperations.deleteExistingData(model=models.CategoryModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)