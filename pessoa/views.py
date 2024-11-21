from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Pessoa
from .functions import totalsum_pessoa, average_pessoa, obter_valor_dolar
from decimal import Decimal 

def landingpage(request):
    return render(request, 'landingpage.html')

def home(request):
    people = Pessoa.objects.all()
    total = None
    average = None
    exchange_rate = None
    exchange_BRL = None  

    if request.method == "POST":
        if 'calculate_totals' in request.POST:
            total = totalsum_pessoa()
            average = round(average_pessoa(), 2)
            messages.success(request, "Cálculo realizado com sucesso!")
        elif 'get_exchange_rate' in request.POST:
            try:
                person_id = request.POST.get('inputText')
                if person_id:
                    person = Pessoa.objects.get(id=int(person_id)) 
                    person_quantity = Decimal(person.quantity) 
                    exchange_rate = Decimal(obter_valor_dolar()) 
                    exchange_BRL = round(person_quantity / exchange_rate, 2) 
                else:
                    messages.error(request, "Por favor, insira um ID válido.")
            except Pessoa.DoesNotExist:
                messages.error(request, "Pessoa não encontrada com o ID fornecido.") 
            except Exception as e:
                messages.error(request, f"Erro ao obter a taxa de câmbio: {str(e)}")

    return render(request, 'home.html', {
        'people': people,
        'total': total,
        'average': average,
        'exchange_BRL': exchange_BRL,
        'exchange_rate': exchange_rate
    })

def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out...')
    return redirect('home')


def get_record(request, pk):
    if request.user.is_authenticated:
        person_record = Pessoa.objects.get(id=pk)
        return render(request, 'record.html', {'person_record': person_record})
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
    if request.method == "POST":
        if form.is_valid():
            add_record = form.save()
            messages.success(request, "Record Added...")
            return redirect('home')
    return render(request, 'add_record.html', {'form': form})

def update_record(request, pk):
    current_record = Pessoa.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('home')
    return render(request, 'update_record.html', {'form': form})
