from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Officer, Scholar, Article
from .serializers import ArticleSerializer, OfficerSerializer, ScholarSerializer
# from .officers import officers

# Create your views here.

# dummy data
@api_view(['GET'])
def getRoutes(request):
    return JsonResponse('Hello, World!', safe=False)

# api/articles
@api_view(['GET'])
def getArticles(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

# api/article
@api_view(['GET'])
def get_article_detail(request, post):
    article = Article.objects.get(slug=post)
    serializer = ArticleSerializer(article, many=False)
    return Response(serializer.data)

# api/scholars
@api_view(['GET'])
def getScholars(request):
    scholars = Scholar.objects.all()
    serializer = ScholarSerializer(scholars, many=True)
    return Response(serializer.data)

# api/officers
@api_view(['GET'])
def getOfficers(request):
    officers = Officer.objects.all().order_by('viewOrder')
    serializer = OfficerSerializer(officers, many=True)
    return Response(serializer.data)

# api/officer
@api_view(['GET'])
def getOfficer(request, pk):
    officer = Officer.objects.get(_id=pk)
    serializer = OfficerSerializer(officer, many=False)
    return Response(serializer.data)