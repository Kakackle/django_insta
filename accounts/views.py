from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth import login as auth_login
from users.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import UpdateView
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #create an attached user profile
            profile = UserProfile.objects.create(user=user)
            #log the created user in
            auth_login(request, user)
            return redirect('instaapp:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.django-html', {'form': form})

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'accounts/account.django-html'
    success_url = reverse_lazy('accounts:account_view')

    def get_object(self):
        return self.request.user