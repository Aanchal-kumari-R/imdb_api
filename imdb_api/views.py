# from django.http import HttpResponse, JsonResponse
from .models import WatchList , StreamPlatform  
from .serializers import WatchListSerializer, StreamPlatformSerializer  
from rest_framework.response import Response
# from rest_framework import status 
from rest_framework.decorators import api_view 
# from django.http import Http404 
from rest_framework.views import APIView 
# from rest_framework import mixins
# from rest_framework import generics 
from rest_framework.reverse import reverse 
from rest_framework import viewsets


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'WatchList': reverse('watch-list-view', request=request, format=format),
        'StreamPlatform': reverse('stream-platform', request=request, format=format)
    })

class StreamPlatformViewSet(viewsets.ModelViewSet): 
      queryset = StreamPlatform.objects.all()
      serializer_class = StreamPlatformSerializer 


class WatchListViewSet(viewsets.ModelViewSet):  
     queryset = WatchList.objects.all()
     serializer_class = WatchListSerializer 




         
















