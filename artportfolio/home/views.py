from django.shortcuts import render
from rest_framework import viewsets
from .models import PortfolioImage
from .serializers import PortfolioSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .permissions import StaffWritePermission

# Create your views here.
def home(request):
    data = {}
    return render(request, "home.html", data)

@api_view(["GET"])
def portfolio(request):
    images = PortfolioImage.objects.all()
    return render(request, "portfolio.html", {"imagenes": images})

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