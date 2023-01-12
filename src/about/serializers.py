from rest_framework import serializers
from src.custom_lib.functions import current_user
from django.utils import timezone

from .models import OurTeam, MessageFromCeo


class OurTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = OurTeam
        fields = "__all__"
        read_only_fields = ['created_by', 'created_date_ad', 'created_date_bs']




    def create(self, validated_data):
        # provide current time
        date_now = timezone.now()
        validated_data['created_by'] = current_user.get_created_by(self.context)
        our_team = OurTeam.objects.create(**validated_data, created_date_ad=date_now)
        return our_team


    def to_representation(self, instance):
        my_fields = {'image'}
        data = super().to_representation(instance)
        for field in my_fields:
            try:
                if not data[field]:
                    data[field] = ""
            except KeyError:
                pass
        return data

class CeoMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageFromCeo
        fields = "__all__"
        read_only_fields = ['created_by', 'created_date_ad', 'created_date_bs']


    def to_representation(self, instance):
        my_fields = {'image'}
        data = super().to_representation(instance)
        for field in my_fields:
            try:
                if not data[field]:
                    data[field] = ""
            except KeyError:
                pass
        return data


    def create(self, validated_data):
        # provide current time
        date_now = timezone.now()
        validated_data['created_by'] = current_user.get_created_by(self.context)
        ceo_message = MessageFromCeo.objects.create(**validated_data, created_date_ad=date_now)
        return ceo_message