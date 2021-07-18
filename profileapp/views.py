from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profileapp import serializers
from profileapp import models

from rest_framework.authentication import TokenAuthentication
from profileapp import permissions

class HelloApiView(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerializer
    def get(self, request, format=None):
        """Return a list"""
        an_apiview=[
            'we use get, post, patch, put, delete'
        ]
        return Response({'message':'hello!','an_apiview':an_apiview})

    def post(self, request):
        """create list"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """edit object"""
        return Response({'method':'PUT'})


    def patch(self, request, pk=None):
        """edit object partially"""
        return Response({'method':'PATCH'})


    def delete(self, request,pk=None):
        """hell yea delete"""
        delete=['delete','ok']
        return Response({'delete':delete})


class HellowViewSet(viewsets.ViewSet):
    """Test viewset api"""
    serializer_class=serializers.HelloSerializer
    def list(self, request):
        """return list"""
        list=['list, create, retrieve, update,partial_update. delete']

        return Response({'hi':'hi in list','list':list})

    def create(self, request):
        """create new message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """handle object ny ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """update object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method':'partial_update'})

    def destroy(self, request, pk=None):
        return Response({'http_method':'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """create and update profile"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
