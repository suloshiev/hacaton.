
from django.db import models
from django.contrib.auth import get_user_model
from post.models import Post

User = get_user_model()


class UserProfile(models.Model):
    '''Модель для профиля User'''
    options = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others','Others')
    )
    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile_data')
    gender = models.CharField(
        max_length = 20,
        choices = options,
        default = 'male',
        null=False,
        blank=False
        )
    nik_name = models.CharField(max_length=50, null=True, blank=True)
    dob=models.DateField(null=True,blank=True,default=None)
    phone=models.CharField(max_length=20,null=True,blank=True)
    works_at=models.CharField(max_length=200,null=True,blank=True)
    lives_in=models.CharField(max_length=200,null=True,blank=True)
    studies_at=models.CharField(max_length=200,null=True,blank=True)
    profile_image=models.ImageField(upload_to="profile_image",null=True,blank=True)



class Comment(models.Model):
    '''Модель для коментариев'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.comment



class Friend(models.Model):
    '''Модель для добавление в друзья'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends', verbose_name='Тот кто хочет дружить')
    profil = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='friends', verbose_name='Тот с кем хочет дружить')
    add_delet = models.BooleanField('Друзья', default=False)

    def __str__(self):
        return f'{self.profil} {self.add_delet}'
