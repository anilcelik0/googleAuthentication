from django.db import models

# Create your models here.
class photo_share(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    name=models.CharField(max_length=2000)
    photo=models.ImageField()
    yt=models.DateTimeField(auto_now_add = True)
    
    user=models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='photo_user', null=False)
    
    def __str__(self):
        return self.name