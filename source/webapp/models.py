from django.contrib.auth import get_user_model
from django.db import models


Status = [('moderate', 'модерация'), ('published', 'Опубликовано'), ('canceled', 'Отклонено'),  ('delete', 'Удаление')]


class Categories(models.Model):
    category_name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Category')

    def __str__(self):
        return self.category_name


class Comment(models.Model):
    announcements = models.ForeignKey('webapp.Announcement', related_name='announcements', on_delete=models.CASCADE,
                                      verbose_name='Project')
    comments_author = models.ForeignKey(get_user_model(), related_name='comments_author', on_delete=models.CASCADE, verbose_name='Author')
    comments = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Content')
    created_at = models.DateField(auto_now_add=True, verbose_name='Created')

    def __str__(self):
        return f'{self.pk} {self.comments}'


class Announcement(models.Model):
    # is_deleted = models.BooleanField(default=False)
    img = models.ImageField(null=True, blank=True, upload_to='pictures', verbose_name='Image')
    title = models.CharField(max_length=30, blank=False, null=False, verbose_name='Title')
    description = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Description')
    author = models.ForeignKey(get_user_model(), related_name='author', on_delete=models.CASCADE, verbose_name='Author')
    price = models.IntegerField(verbose_name='Price')
    category = models.ForeignKey('webapp.Categories', related_name='category', on_delete=models.PROTECT,
                                 verbose_name='Categories')
    status = models.CharField(max_length=15, choices=Status, default=Status[0][0],)
    created_at = models.DateField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateField(auto_now=True, verbose_name='Updated')
    published = models.DateField(auto_now=True, verbose_name='Published')

    def __str__(self):
        return f'{self.title}'


# class SoftDeleteModel(models.Model):
#     is_deleted = models.BooleanField(default=False)
#
#     def soft_delete(self):
#         self.is_deleted = True
#         self.save()
#
#     def restore(self):
#         self.is_deleted = False
#         self.save()
#
#     class Meta:
#         abstract = True




