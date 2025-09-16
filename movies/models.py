from django.db import models
from django.contrib.auth.models import User
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    def __str__(self):
        return str(self.id) + ' - ' + self.name
    
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie,
        on_delete=models.CASCADE)
    user = models.ForeignKey(User,
        on_delete=models.CASCADE)
    likes_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name
    
class Director(models.Model):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'review')  # Prevent duplicate likes
    
    def __str__(self):
        return f"{self.user.username} likes {self.review.id}"

