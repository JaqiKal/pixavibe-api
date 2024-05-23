from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
# converts model instances to JSON and vice versa
from .serializers import ProfileSerializer


class ProfileList(APIView):
    """
    List all profiles
    No Create view (post method), as profile creation handled by django
    signals.
    This class-based view provides a read-only endpoint for listing all
    profiles in the system. By inheriting from APIView, it leverages Django
    REST Framework's features to handle HTTP GET requests, retrieve data
    from the database, serialize it into JSON format, and send it back in
    the HTTP response. Profile creation is managed by Django signals,
    hence no post method is included in this view.
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetail(APIView):
    """
    Retrieve, update or delete a profile instance.
    """
    serializer_class = ProfileSerializer
    def get_object(self, pk):
        
        """
        Retrieve a profile by its primary key (pk).
        """
        try:
            profile = Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        
        """
        Handle GET request for retrieving a specific profile.
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
        

    def put(self, request, pk):
        
        """
        Handle PUT request for updating a specific profile.
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

