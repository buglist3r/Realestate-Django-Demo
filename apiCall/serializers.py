from django.contrib.auth.models import User, Group
from rest_framework import serializers
from listings.models import Listing


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = ('id', 'title', 'photo_main', 'address', 'city', 'state', 'zipcode', 'price', 'garage')
