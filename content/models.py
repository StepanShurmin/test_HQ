from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор продукта')
    title = models.CharField(max_length=100, verbose_name="название продукта", )
    started_at = models.DateTimeField(verbose_name='дата и время старта')
    price = models.PositiveIntegerField(verbose_name='стоимость')

    def enrol_users_to_groups(self):

        groups = self.groups.all()

        unassigned_users = User.objects.exclude(groups__product=self)

        for group in groups:

            needed_users = group.max_students - group.students.count()

            if needed_users > 0:
                users_to_assign = unassigned_users[:needed_users]
                group.students.add(*users_to_assign)
                unassigned_users = unassigned_users[needed_users:]


    def __str__(self):
        return f"{self.title} {self.price} руб"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Lesson(models.Model):
    product = models.ForeignKey(Product, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(unique=True, max_length=200, verbose_name='название')
    video_url = models.URLField(verbose_name='ссылка на видео')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

class Group(models.Model):
    product = models.ForeignKey(Product, related_name='groups', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='название группы')
    students = models.ManyToManyField(User, verbose_name='ученики')
    min_students = models.PositiveIntegerField(default=5, verbose_name='минимальное количество участников в группе')
    max_students = models.PositiveIntegerField(default=20,verbose_name='максимальное количество участников в группе')

    def __str__(self):
        return f"{self.title} ({self.product.title})"

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'
