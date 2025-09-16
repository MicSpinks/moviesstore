from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from django.contrib.auth.decorators import login_required
from django.urls import reverse
 
@login_required
def toggle_hide(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        if request.user in movie.hidden_by.all():
            movie.hidden_by.remove(request.user)   # un-hide
        else:
            movie.hidden_by.add(request.user)      # hide
    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or reverse('movies:hidden_movies')
    return redirect(next_url)

# (add this)
@login_required
def hidden_movies(request):
    movies = request.user.hidden_movies.all()
    return render(request, 'movies/hidden_movies.html', {'movies': movies})


def index(request):
    search_term = request.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()

    # Exclude movies the current user has hidden
    if request.user.is_authenticated:
        movies = movies.exclude(hidden_by=request.user)
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies
    return render(request, 'movies/index.html',
                  {'template_data': template_data})


def show(request, id):
    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=movie).order_by('-date')
    
    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    template_data['reviews'] = reviews
 
    return render(request, 'movies/show.html', {'template_data': template_data})

@login_required
def create_review(request, id):
    if request.method == 'POST' and request.POST['comment'] != '':
        movie = Movie.objects.get(id=id)
        review = Review()
        review.comment = request.POST['comment']
        review.movie = movie
        review.user = request.user
        review.save()
        return redirect('movies:show', id=id)
    else:
        return redirect('movies:show', id=id)
    
@login_required
def edit_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user:
        return redirect('movies:show', id=id)
    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit Review'
        template_data['review'] = review
        return render(request, 'movies/edit_review.html',
            {'template_data': template_data})
    elif request.method == 'POST' and request.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('movies:show', id=id)
    else:
        return redirect('movies:show', id=id)
    
@login_required
def delete_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id,
        user=request.user)
    review.delete()
    return redirect('movies:show', id=id)
