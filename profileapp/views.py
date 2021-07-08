from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list"""
        an_apiview=[
            'we use get, post, patch, put, delete'
        ]
        return Response({'message':'hello!','an_apiview':an_apiview})

    def post(self, request, format=None):
        """create list"""
        creation=[
            'posted/created'
        ]
        return Response({'sup':'yea','creation':creation})

    def patch(self, request, format=None):
        """edit list"""
        patch=[
            'patched/created'
        ]
        return Response({'sup':'yea','patch':patch})

    def put(self, request, format=None):
        """edit partially"""
        put=['we put']
        return Response({'sup':'yea','put':put})


    def delete(self, request,format=None):
        """hell yea delete"""
        delete=['delete','ok']
        return Response({'delete':delete})
