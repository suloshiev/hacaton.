
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator



User = get_user_model()


class Post(models.Model):
    '''Модель поста'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=4000)
    post_image = models.ImageField(upload_to="post_image",null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content



class Like(models.Model):
    '''Модель для Like'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='Владелиц лайка')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', verbose_name='пост')
    like = models.BooleanField('Лайк', default=False)

    def __str__(self):
        return f'{self.post} {self.like}'



class Rating(models.Model):
    """Модель для рейтинга"""

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', verbose_name='Владелец рейтинга')
    product = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings', verbose_name='Пост')
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ], default=1
    )

    def __str__(self):
        return f'{self.product} - {self.rating}'


class Favorite(models.Model):
    '''Модель для избранного'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorits')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorits')
    favorite = models.BooleanField('Избранное',default=False)

    def __str__(self):
        return f'{self.owner} {self.post}'


class Contact(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
