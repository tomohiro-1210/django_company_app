from django.db import models

# Create your models here.
class snsModel(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    author = models.CharField(max_length=50)
    post_img = models.ImageField(upload_to='') #upload_toは保存先を指定する
    good = models.IntegerField() #いいね
    read = models.IntegerField() #既読
    readtext = models.TextField() #

