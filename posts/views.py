from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GetAllInfo, PostSerializer
from .models import posts
from rest_framework.decorators import api_view
from rest_framework import generics


# Create your views here.


@api_view(['GET'])
def taskList(request):
    tasks = posts.objects.all().order_by('-id')
    serializer = GetAllInfo(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = posts.objects.get(id=pk)
    serializer = GetAllInfo(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = GetAllInfo(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = posts.objects.get(id=pk)
    serializer = GetAllInfo(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = posts.objects.get(id=pk)
    task.delete()

    return Response('Item succsesfully delete!')
