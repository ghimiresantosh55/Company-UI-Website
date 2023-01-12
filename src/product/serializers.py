from rest_framework import serializers
from src.custom_lib.functions import current_user
from django.utils import timezone

from .models import Product


class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ['created_by', 'created_date_ad', 'created_date_bs']


    def create(self, validated_data):
        print(validated_data, "this is validated data")
        # provide current time
        date_now = timezone.now()
        validated_data['created_by'] = current_user.get_created_by(self.context)
        product= Product.objects.create(**validated_data, created_date_ad=date_now)
        return product