from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUpForm, UserEditForm, ChangePasswordForm
from django.contrib.auth import login as auth_login
from users.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import UpdateView
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            #create an attached user profile
            profile = UserProfile.objects.create(user=user, profile_img=form.cleaned_data.get("profile_img"))
            # profile.profile_img = request.POST.get('profile_img')
            # print('profile img: ', request.POST.get('profile_img'))
            profile.save()
            #log the created user in
            auth_login(request, user)
            return redirect('instaapp:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.django-html', {'form': form})

@login_required()
def edit_view(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = UserProfile.objects.get(user=request.user)
            img = form.cleaned_data.get("profile_img")
            if img:
                profile.profile_img = img
            profile.bio = form.cleaned_data.get("bio")
            profile.save()
            return redirect('accounts:account_edit')
    else:
        user = request.user
        initial_data = {
            'email' : user.email,
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'profile_img': user.profile.profile_img,
            'bio': user.profile.bio
        }
        form = UserEditForm(initial=initial_data)
    return render(request, 'accounts/account.django-html', {'form': form})

# @method_decorator(login_required, name='dispatch')
# class UserUpdateView(UpdateView):
#     model = User
#     fields = ('first_name', 'last_name', 'email', )
#     template_name = 'accounts/account.django-html'
#     success_url = reverse_lazy('accounts:account_view')

#     def get_object(self):
#         return self.request.user

@login_required()
def delete_view(request):
    if request.POST:
        # print('tried to delete me, huh?')
        User.objects.get(username=request.user.username).delete()
        return redirect('instaapp:home')
    
    return render(request, 'accounts/delete_confirm.django-html')

@login_required()
def change_password(request):
    if request.POST:
        user = request.user
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_pass = form.cleaned_data.get("old_password")
            new1 = form.cleaned_data.get("new_password_1")
            new2 = form.cleaned_data.get("new_password_2")
            if user.check_password(old_pass):
                if new1 == new2:
                    user.set_password(new1)
                    user.save()
                    print('password changed to: ', new1)
                    return redirect('users:user_view', user_slug=user.username)
    else:
        form = ChangePasswordForm()
    return render(request, 'accounts/change_password.django-html', {'form': form})
    