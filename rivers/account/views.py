from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = request.user
    
    if user.groups.filter(name='Seller').exists():
        group = 'Seller'
        content = 'Welcome to Group A Dashboard'
    elif user.groups.filter(name='Byer').exists():
        group = 'Byer'
        content = 'Welcome to Group B Dashboard'
    else:
        group = 'No Group'
        content = 'You are not assigned to any group.'
    
    context = {
        'group': group,
        'content': content,
    }
    
    return render(request, 'dashboard.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически логиним пользователя после регистрации
            return redirect('dashboard')  # Перенаправление после успешной регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
