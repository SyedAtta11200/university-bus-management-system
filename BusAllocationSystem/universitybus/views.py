from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Bus
from .serializers import BusSerializer


class BusView(ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class BusViewRUD(RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    lookup_field = 'pk'