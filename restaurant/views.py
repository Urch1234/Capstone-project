from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, UserSerializer, BookingSerializer


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
