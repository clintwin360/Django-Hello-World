from django.shortcuts import render

##  New additions
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from django.contrib.auth import authenticate, login, logout as auth_views
from .models import User, UserManager, Contact, Sponsor, Participant, ClinicalTrial, Criteria, Categories, ClinicalTrialCriteriaResponse, QuestionSchema
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
#from .forms import *
from django.views.generic.edit import FormView
from .forms import NewUserForm, UserCreationForm
#from .forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic

# End of new additions

# Create your views here.


def index(request):
    return render(request, 'index.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def logout(request):
    logout(request)
    return redirect('registration/logged_out.html')
    
def password_reset(request):
    password_reset(request)
    return redirect('registration/password_reset.html')	
"""
def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})
	

def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        if (bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode())):
            request.session['id'] = user.id
            return redirect('/success')
    return redirect('/')


def logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/') 


# View for contact us form
def contact(request):
    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = ContactForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            # Insert into DB
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('success.html')
    else:
        # GET, generate unbound (blank) form
        form = ContactForm()
    return render(request,'contactform.html',{'form':form})
"""
# Static page for About us
class AboutPageView(TemplateView):
    template_name = 'about.html'

# Static page for How it Works
class HowWorksPageView(TemplateView):
    template_name = 'how_works.html'	

# Static page for Contact us
class ContactPageView(TemplateView):
    template_name = 'contact.html'	
	
	
# Static page for directions
class DirectionsPageView(TemplateView):
    template_name = 'directions.html'

# Static page for Message display
class MessagePageView(TemplateView):
    template_name = 'messages.html'	
	

class ClinicalTrialCreateView(generic.CreateView):
    model = ClinicalTrial
    fields = ('trialId', 'sponsorId', 'title', 'objective','recruitmentStartDate','recruitmentEndDate','enrollmentTarget','inclusionCriteria','exclusionCriteria','url','followUp','location','comments')
    template_name = 'create_trial_form.html'
