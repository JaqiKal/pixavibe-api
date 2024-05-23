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
