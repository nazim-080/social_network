from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author", verbose_name="Автор"
    )
    title = models.CharField("Заголовок", max_length=200)
    body = models.TextField("Текст", max_length=3000)
    liked_users = models.ManyToManyField(
        User,
        related_name="post_liked_users",
        verbose_name="Лайкнувшие пользователи",
        blank=True,
    )
    created_at = models.DateTimeField("Время создания записи", auto_now_add=True)
    updated_at = models.DateTimeField("Время обновления записи", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
