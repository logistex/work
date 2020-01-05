import django
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(        # 작성일자
            default=timezone.now)               # 여기는 timezone.now()가 아니라 timezone.now
    published_date = models.DateTimeField(      # 게시일자
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()    # 여기는 timezone.now가 아니라 timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):  # 댓글
    post = models.ForeignKey('blog.Post',
                             on_delete=models.CASCADE,
                             related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=django.utils.timezone.now)
    # created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

