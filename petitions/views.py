from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Petition, PetitionVote
from .forms import PetitionForm

@login_required
def petition_create(request):
    if request.method == "POST":
        form = PetitionForm(request.POST)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.created_by = request.user
            petition.save()
            return redirect("petition_list")
        else:
            print(form.errors) 
    else:
        form = PetitionForm()
    
    context = {
        "form": form,
        "template_data": "Create Petition"
    }
    
    return render(request, "petitions/create.html", context)


# Create your views here.
def petition_list(request):
    petitions = Petition.objects.all()
    return render(request, "petitions/list.html", {"petitions": petitions})



@login_required
def vote_petition(request, pk): 
    petition = get_object_or_404(Petition, pk=pk)
    vote, created = PetitionVote.objects.get_or_create(petition=petition, voter=request.user)
    if not created:
        vote.delete()
    return redirect("petition_list")
