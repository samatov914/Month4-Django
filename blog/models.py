from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

class Comment(models.Model):
    username = models.CharField(max_length=16,verbose_name="Имя автора")
    text = models.CharField(max_length=300, verbose_name="Текст комментария")
    created = models.DateField(auto_now=True, verbose_name= "Дата создания комментария")
    post = models.ForeignKey(Post,on_delete= models.CASCADE, related_name="post_comment", verbose_name="Пост")

    def __str__(self):
        return f"{self.username} - {self.post.title}"
    

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"