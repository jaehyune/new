from django.db import models
from django.conf import settings
import re

# Create your models here.
     

class Tag(models.Model):
    tag=models.CharField(max_length=20)
    
    def __str__(self):
        return self.tag

class Board(models.Model):
    title = models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True, null=True)
    body=models.TextField()
    tags=models.ManyToManyField(Tag)
    
    class Meta:
        ordering=['-pub_date'] 

    #note: content에서 tags를 추출하여, tag 객체 가져오기, 신규 태그는 Tag instance 생성, 본인의 tag_set에 등록, 
    
    def __str__(self):
        return self.title
   

class Reple(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author_name=models.CharField(null=True, max_length=200)
    board=models.ForeignKey(Board,on_delete=models.CASCADE)
    body=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering=['-pub_date']
    
    def __str__(self):
        return self.body





    