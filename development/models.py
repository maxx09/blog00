from django.db import models

class Category(models.Model):

    category_name = models.CharField(max_length=10)

    def __str__(self):
        return self.category_name


class HashTag(models.Model):

    tag = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.tag)


class Article(models.Model):

    title = models.CharField(max_length=100)
    subTitle = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    hashtag = models.ManyToManyField(HashTag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)


class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comment')
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}에 댓글 : {}'.format(self.article.title, self.content)

