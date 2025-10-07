from django.db import models
from django.contrib.auth.models import User

class Petition(models.Model):
    movie_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def vote_count(self):
        return self.votes.count()

    def __str__(self):
        return self.movie_name


class PetitionVote(models.Model):
    petition = models.ForeignKey(Petition, related_name='votes', on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('petition', 'voter')
