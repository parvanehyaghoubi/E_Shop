from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:

        if request.method == 'POST':
            user_ = request.POST.get('username')
            pass_ = request.POST['password']

            user = authenticate(username=user_, password=pass_)

            if user is not None:
                login(request, user=user)
                return redirect('index')
            else:
                print('Error, User Not Found.')
                return redirect('login')
                # print(f'''
                # user: {user}
                # ''')
                # print(f'''
                # user_: {user_}
                # pass_: {pass_}
                # ''')

                # print('''
                # !!!Button pushed!!!
                # ''')
        return render(request, template_name='login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user_ = request.POST.get('username')
            email_ = request.POST.get('email')
            pass_ = request.POST['password']
            pass2_ = request.POST['password2']
            if pass_ == pass2_:
                user = User.objects.create_user(
                    username=user_,
                    email=email_,
                    password=pass_,
                )
                user.save()
                return redirect('signin')
            else:
                print('''
                Password do not match!
                ''')
                return redirect('register')

        return render(request, template_name='register.html')


def signout(request):
    logout(request)
    return redirect('detail')
