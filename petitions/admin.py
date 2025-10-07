from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Petition, PetitionVote

@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_name', 'created_by', 'created_at', 'vote_count')
    list_filter = ('created_at', 'created_by')
    search_fields = ('movie_name', 'created_by__username')

@admin.register(PetitionVote)
class PetitionVoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'petition', 'voter')
    list_filter = ('petition',)
    search_fields = ('petition__movie_name', 'voter__username')
