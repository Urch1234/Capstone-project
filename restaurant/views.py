from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, UserSerializer, BookingSerializer


# Create your views here.
def index(request):
    return render(request, "index.html", {})


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAutheentication])
def msg(request):
    return Response({"message": "This view is protected"})


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
