from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status



####################################################################
#                                                                  #
#                    Class based api_view                          #
#                                                                  #
####################################################################

class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            student = Student.objects.get(id=pk)
            serialized_data = StudentSerializer(student)
            return Response(serialized_data.data)

        students = Student.objects.all()
        serialized_data = StudentSerializer(students, many=True)
        return Response(serialized_data.data)

    def post(self, request, format=None):
        serialized_data = StudentSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'messsage': 'Data created!'}, status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        student = Student.objects.get(id=pk)
        serialized_data = StudentSerializer(student, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'messsage': 'Data Updated Completely!'})
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        student = Student.objects.get(id=pk)
        serialized_data = StudentSerializer(student, data=request.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'messsage': 'Data Updated Partially!'})
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None, format=None):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'message': 'Data deleted!'}, status=status.HTTP_202_ACCEPTED)



####################################################################
#                                                                  #
#                    Funtion based api_view                        #
#                                                                  #
####################################################################


# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def student_api(request, pk=None):
#     if request.method == 'GET':
#         if pk is not None:
#             student = Student.objects.get(id=pk)
#             serialized_data = StudentSerializer(student)
#             return Response(serialized_data.data)

#         students = Student.objects.all()
#         serialized_data = StudentSerializer(students, many=True)
#         return Response(serialized_data.data)

#     if request.method == 'POST':
#         serialized_data = StudentSerializer(data=request.data)
#         if serialized_data.is_valid():
#             serialized_data.save()
#             return Response({'messsage': 'Data created!'}, status=status.HTTP_201_CREATED)
#         return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'PUT':
#         student = Student.objects.get(id=pk)
#         serialized_data = StudentSerializer(student, data=request.data)
#         if serialized_data.is_valid():
#             serialized_data.save()
#             return Response({'messsage': 'Data Updated Completely!'})
#         return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'PATCH':
#         student = Student.objects.get(id=pk)
#         serialized_data = StudentSerializer(student, data=request.data, partial=True)
#         if serialized_data.is_valid():
#             serialized_data.save()
#             return Response({'messsage': 'Data Updated Partially!'})
#         return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         student = Student.objects.get(id=pk)
#         student.delete()
#         return Response({'message': 'Data deleted!'}, status=status.HTTP_202_ACCEPTED)
