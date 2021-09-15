from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# @api_view()
@api_view(['GET'])
def say_hello(request):
    return Response({'message': 'Hello World!'})


@api_view(['POST'])
def say_hello_post_req(request):
    if request.method == 'POST':
        return Response({'message': 'Hello World! This is post request!', 'data': request.data})


# @api_view(['GET', 'POST'])
# def say_hello_post_req(request):
#     if request.method == 'GET':
#         return Response({'message': 'Hello World! This is get request!'})

#     if request.method == 'POST':
#         return Response({'message': 'Hello World! This is post request!'})