from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Twitter
import json
from .serializers import TwitterSerializer


class TwitterViewSet(viewsets.ModelViewSet):
    queryset = Twitter.objects.all()
    serializer_class = TwitterSerializer

class TwitterViewNoParam(APIView):

    def get(self, request):
        queryset = Twitter.objects.all()
        serializer_class = TwitterSerializer(queryset, many=True)
        return Response({"twitters": serializer_class.data})
    
    def post(self, request):
        queryset = TwitterSerializer(data=request.data)
        if(queryset.is_valid()):
            postSaved = queryset.save()
            return Response({"status": "success"})
        else:
            return Response({"error": queryset.error_messages})

    # def post(self, request):
    #     queryset = TwitterSerializer(data=request.data)
    #     return Response(queryset.is_valid())
    #     if(queryset.is_valid()):
    #         postSaved = queryset.save()
    #         return Response({"twitters": queryset})
    #     else:
    #         return Response({"error": queryset.data})


class TwitterView(APIView):
    
    def get(self, request, pk=None):
        if(pk): 
            queryset = Twitter.objects.get(pk=pk)
            serializer_class = TwitterSerializer(queryset, many=False)
            return Response({'twitter': serializer_class.data})

    def delete(self, request, pk=None):
        if(pk):
            queryset = Twitter.objects.get(pk=pk)
            queryset.delete()
            return Response({"status": "the register with id {} has been delete".format(pk      )})
        else:
            return Response({"error": "Fail to delete this id : {}".format(pk)})

    def put(self, request, pk=None):
        if(pk):
            queryset = Twitter.objects.get(pk=pk)
            serializer_class = TwitterSerializer(instance=queryset, data=request.data, partial=True) 
            if(serializer_class.is_valid()):
                serializer_class.save()
                return Response({"status": "the register with id {} has been delete".format(pk)})
            else:
                return Response({"error": "Fail to delete this id : {}".format(pk)})