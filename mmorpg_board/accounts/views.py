from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegisterForm
from .models import CustomUser

from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            send_mail(
                'Подтверждение регистрации',
                f'Ваш код: {user.verification_code}',
                settings.EMAIL_HOST_USER,
                [user.email],
            )
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            error_message = "Пожалуйста, заполните все поля."
            return render(request, 'registration/login.html', {'error_message': error_message})

        # Аутентификация пользователя
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('post_list')  # Перенаправляем на главную страницу
            else:
                error_message = "Аккаунт не активен."
        else:
            error_message = "Неверное имя пользователя или пароль."
        return render(request, 'registration/login.html', {'error_message': error_message})

    return render(request, 'registration/login.html')
