from django.db import models

# Create your models here.
class snsModel(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    author = models.CharField(max_length=50)
    post_img = models.ImageField(upload_to='') #upload_toは保存先を指定する
    good = models.IntegerField(null=True, blank=True, default=0) #いいね
    read = models.IntegerField(null=True, blank=True, default=0) #既読
    readtext = models.TextField(null=True, blank=True, default='投稿者') #既読つけた人

