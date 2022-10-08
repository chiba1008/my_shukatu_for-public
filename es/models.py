from email.policy import default
from ensurepip import version
from tabnanny import verbose
from time import timezone
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from urllib.parse import urlparse
from django.contrib.auth import get_user, get_user_model
from django.utils import timezone
from django import forms


User = get_user_model()

class EsPost(models.Model):
    title = models.CharField(verbose_name = 'タイトル', max_length = 100)
    content = models.TextField(verbose_name = '内容')
    posted_at = models.DateTimeField(verbose_name = '作成日時')
    updated_at = models.DateTimeField(verbose_name = '更新日時', null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='ログインユーザー', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.posted_at = timezone.now()  # 新規作成時の時刻を保存
        self.updated_at = timezone.now()  # 保存されるたびに更新
        return super(EsPost, self).save(*args, **kwargs)

