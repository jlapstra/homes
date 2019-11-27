from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from homes.models import Home
from homes.serializers import HomeSerializer

class HomesEndpoint(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

    def get(self, request):
        try:
            queryset = self.get_queryset()
        except Home.DoesNotExist:
            raise NotFound(detail="Homes matching query do not exist", code=404)

        serialize = self.serializer_class(queryset, many=True)

        return Response(serialize.data, status=200)

class SingleHomeEndpoint(generics.RetrieveAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    lookup_field = 'zillow_id'

    def get(self, request, zillow_id):
        try:
            queryset = Home.objects.get(zillow_id=zillow_id)
        except Home.DoesNotExist:
            raise NotFound(detail="Home matching query does not exist", code=404)

        serialize = self.serializer_class(queryset)

        return Response(serialize.data, status=200)

class CreateHomeEndpoint(generics.CreateAPIView):
    serializer_class = HomeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=200)
