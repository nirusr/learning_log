from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        print ('I am here...')
        # Process completed form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            print ('form is valid')
            new_user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            authenticated_user = authenticate(username=username,
                                              password=raw_password)
            print (username, raw_password)
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:topics'))
        else:
            print (form.is_valid())
            print (form.errors)
            messages.error(request,form.errors)
    context = {'form': form}
    return render(request, 'users/register.html', context)

