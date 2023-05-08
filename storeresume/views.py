from django.shortcuts import render, HttpResponse
from .forms import JobSeekerForm
from .database import resume_collection
import bson
# Create your views here.


def jobseeker_homepage(request):
    return render(request, 'storeresume/base.html')

def signup_with_resume(request):
    if request.method == 'POST':
        record = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'address': request.POST.get('address'),
        }
        res = request.FILES['resume']
        resume = res.read()
        record['resume'] = bson.binary.Binary(resume)

        resume_collection.insert_one(record)

        return render(request, 'storeresume/signup_success.html')
    else:
        form = JobSeekerForm()
    return render(request, 'storeresume/jobseeker_signup.html', {'form': form})
