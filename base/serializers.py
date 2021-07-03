from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Officer, Article, Scholar
from django.urls import reverse
# from rest_framework.reverse import reverse

class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = '__all__'

class ScholarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholar
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    officer_name = serializers.CharField(source='officer')

    class Meta:
        use_natural_foreign_keys = True
        model = Article
        # fields = '__all__'
        fields = ('_id', 'title', 'content', 'officer_name', 'publishDate', 'status', 'slug',)
        # fields = ('_id', 'title', 'body', 'officer', 'publishDate', 'status', 'slug', 'get_url', 'get_absolute_url')

    # def get_url(self, article_post):
    #     my_url = article_post.get_absolute_url
    #     return my_url


