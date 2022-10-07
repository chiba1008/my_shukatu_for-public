from ensurepip import version
from tabnanny import verbose
from unicodedata import category
from django.db import models
from urllib.parse import urlparse
from django.contrib.auth import get_user, get_user_model

User = get_user_model()

class ShukatuPost(models.Model):
    CATEGORY = (('maker','メーカー'),
                ('trading company','商社'),
                ('retail','小売'),
                ('finance','金融'),
                ('service','サービス'),
                ('mass media','マスコミ'),
                ('IT','IT'),
                ('government office','官公庁・公社・団体'),
                ('others','その他'),
                )


    title = models.CharField(verbose_name = '企業名', max_length = 100)
    myPageId = models.CharField(verbose_name = 'myPageId', max_length = 100)
    myPageUrl = models.CharField(verbose_name = 'myPageUrl', max_length = 255)
    posted_at = models.DateTimeField(verbose_name = '登録日時', auto_now_add = True)
    category = models.CharField(verbose_name = 'カテゴリ', max_length = 50, choices = CATEGORY, null = True, blank =True)
    user = models.ForeignKey(User, verbose_name='ログインユーザー', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
