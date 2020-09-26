from django.db import models


class Genere(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movies(models.Model):
    title=models.CharField(max_length=50)
    release=models.IntegerField()
    rating=models.IntegerField()
    stock=models.IntegerField()
    price=models.FloatField()
    image=models.ImageField(default='photo.jpg', upload_to='picture')
    genre=models.ForeignKey(Genere, on_delete=models.CASCADE)


    def __str__(self):
        return self.title




