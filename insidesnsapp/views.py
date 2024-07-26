from django.shortcuts import render, redirect
from django.contrib.auth.models import User #ユーザーモデルの読み込み
from django.db import IntegrityError #重複したときのエラー
from django.contrib.auth import authenticate ,login #ログイン機能
from .models import snsModel #モデルの読み込み


# Create your views here.

# サインアップ
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '' ,password)
            return render(request, 'signup.html', {'some':100})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています。'})# {}はモデルまたは任意で出したデータ


    # return render(request, 'signup.html', {})# {}はモデルまたは任意で出したデータ
    return redirect('login')

# ログイン
def loginfunc(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
             login(request, user)
             return render(request, 'login.html', {'context': 'ログイン済み'})
        else:
            return render(request, 'login.html', {'context': 'ログインしていません'})
    
    return render(request, 'login.html', {'context': 'get method'})
            
# 投稿一覧
def listfunc(request):
    object_list = snsModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

#
