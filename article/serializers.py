'''
@ Author: BrightStar1120
@ Date: 2019-03-24
@ Last Modified by: BrightStar1120
@ Last Modified Date: 2019-03-24
'''

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'