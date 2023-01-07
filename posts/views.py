from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GetAllInfo, PostSerializer
from .models import posts
from rest_framework.decorators import api_view
from rest_framework import generics


# Create your views here.


# class GetAllInfoAPI(APIView):
#     def get(self, request):
#         list_info = posts.objects.all()
#         mydata = GetAllInfo(list_info, many=True)
#         return Response(data=mydata.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         mydata = PostSerializer(request.data)
#         if not mydata.is_valid():
#             return Response('Sai du lieu roi!',status=status.HTTP_400_BAD_REQUEST)
#         title=mydata.data['title1']
#         desciption=mydata.data['desciption1']
#         posts.objects.create(title=title,desciption=desciption)
#         return Response(data=mydata.data, status=status.HTTP_200_OK)

# class ItemList(generics.ListCreateAPIView):
#     serializer_class=GetAllInfo
#
#     def get_queryset(self):
#         queryset=posts.objects.all()
#         location =self.request.query_params.get('location')
#         if location is not None:
#             queryset=queryset.filter()
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
