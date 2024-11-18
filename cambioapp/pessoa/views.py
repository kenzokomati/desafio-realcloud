from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Pessoa
from .functions import totalsum_pessoa, average_pessoa
from django.http import JsonResponse

def home(request):
    people = Pessoa.objects.all()
    total = None  
    average = None

    if request.method == "POST":
        total = totalsum_pessoa()
        average = round(average_pessoa(), 2)
        messages.success(request, "Cálculo realizado com sucesso!")

    return render(request, 'home.html', {
        'people': people,
        'total': total,
        'average': average
    })


def get_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		person_record = Pessoa.objects.get(id=pk)
		return render(request, 'record.html', {'person_record':person_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')


def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Pessoa.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_record(request):

  form = AddRecordForm(request.POST or None)
	# if request.user.is_authenticated:
  if request.method == "POST":
    if form.is_valid():
      add_record = form.save()
      messages.success(request, "Record Added...")
      return redirect('home')
  return render(request, 'add_record.html', {'form':form})
	# else:
	# 	messages.success(request, "You Must Be Logged In...")
	# 	return redirect('home')


def update_record(request, pk):
  current_record = Pessoa.objects.get(id=pk)
  form = AddRecordForm(request.POST or None, instance=current_record)
  if form.is_valid():
    form.save()
    messages.success(request, "Record Has Been Updated!")
    return redirect('home')
  return render(request, 'update_record.html', {'form':form})