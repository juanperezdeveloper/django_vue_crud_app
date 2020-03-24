'''
@ Author: BrightStar1120
@ Date: 2019-03-24
@ Last Modified by: BrightStar1120
@ Last Modified Date: 2019-03-24
'''

from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer