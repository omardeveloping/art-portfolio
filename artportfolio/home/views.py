from django.shortcuts import render
from rest_framework import viewsets
from .models import PortfolioImage
from .serializers import PortfolioSerializer
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PortfolioImage
from django.shortcuts import get_object_or_404

from .permissions import StaffWritePermission

# Create your views here.
def home(request):
    data = {}
    return render(request, "home.html", data)

@api_view(["GET"])
def portfolio(request):
    response = requests.get("http://127.0.0.1:8000/api/images/")
    data = response.json()
    return render(request, 'portfolio.html', {"imagenes": data})

@api_view(["POST"])
def like_image(request, id):
    post = get_object_or_404(PortfolioImage, id=id)
    post.likes += 1
    post.save()
    return Response({"likes": post.likes})

def about(request):
    data = {}
    return render(request, 'about.html', data)

def chat(request):
    data = {}
    return render(request, 'chat.html', data)

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = PortfolioImage.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [StaffWritePermission]