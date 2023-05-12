from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate, Voter

def home(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}
    return render(request, 'home.html', context)

def vote(request):
    if request.method == 'POST':
        candidate_id = request.POST.get('candidate')
        voter_email = request.POST.get('email')
        voter = Voter.objects.get(email=voter_email)
        if not voter.voted:
            candidate = Candidate.objects.get(pk=candidate_id)
            candidate.votes += 1
            candidate.save()
            voter.voted = True
            voter.save()
            return HttpResponse('Vote submitted successfully.')
        else:
            return HttpResponse('You have already voted.')
    else:
        candidates = Candidate.objects.all()
        context = {'candidates': candidates}
        return render(request, 'vote.html', context)