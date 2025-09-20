from rest_framework import serializers
from .models import PortfolioImage

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioImage
        fields = "__all__"