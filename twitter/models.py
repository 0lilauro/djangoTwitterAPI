from django.db import models
from datetime import datetime 

# Create your models here.
class Twitter(models.Model):
    
    id = models.IntegerField(primary_key=True, blank=True)
    username = models.CharField(max_length = 100, null=False)
    post = models.CharField(max_length = 3000, null=False)
    date = models.DateTimeField(db_column='date_post', blank=True,default=datetime.now().strftime("%Y-%m-%d"),null=False)
    
    class Meta:
        db_table = "twitter"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return '"{}" - {}'.format(self.post, self.username)
