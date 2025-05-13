from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test, login_required

from .forms import SignUpForm, EntryForm

from .models import Entry
from django.contrib.auth.models import User
# Create your views here.

def enter(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, "enter_page.html")


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'sign_up.html', {'form': form})


@login_required
def homepage(request):
    entries = Entry.objects.all()
    return render(request, 'home.html', {'entries': entries})

@login_required
def create_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user_created = request.user
            entry.save()
            return redirect('home')
    else:
        form = EntryForm()
        return render(request, 'create_entry.html', {'form': form})

@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)

    if entry.user_created != request.user:
        return HttpResponseForbidden("You can not edit others' entries")

    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = EntryForm(instance=entry)
    return render(request, "edit_entry.html", {'form': form, 'entry': entry})


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def user_administration(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def delete_user(request, user_id):
    user_to_delete = get_object_or_404(User, id=user_id)

    if request.user == user_to_delete:
        redirect('user_administration')

    user_to_delete.delete()
    return redirect('user_administration')

@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def entry_manager(request):
    entries = Entry.objects.all()
    return render(request, "entry_manager.html", {'entries': entries})

@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def delete_entry(request, entry_id):
    entry_to_delete = get_object_or_404(Entry, id=entry_id)
    entry_to_delete.delete()
    return redirect('entry_manager')







