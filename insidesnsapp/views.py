from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User #ユーザーモデルの読み込み
from django.db import IntegrityError #重複したときのエラー
from django.contrib.auth import authenticate ,login ,logout #ログイン機能
from .models import snsModel #モデルの読み込み
from django.contrib.auth.decorators import login_required #ログイン必須の読み込み


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


    return render(request, 'signup.html', {})# {}はモデルまたは任意で出したデータ
    

# ログイン
def loginfunc(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
             login(request, user)
             return redirect('list')
        else:
            return render(request, 'login.html', {})
    
    return render(request, 'login.html', {})

#ログアウト
def logoutfunc(request):
    logout(request)
    return redirect('login')

@login_required #ログイン必須
# 投稿一覧
def listfunc(request):
    object_list = snsModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

@login_required
#投稿詳細
def detailfunc(request, pk):
    object = get_object_or_404(snsModel, pk=pk)
    return render(request, 'detail.html', {'object':object})

def likefunc(request, pk):
    object = snsModel.objects.get(pk=pk) #投稿データを引っ張り出す
    object.good = object.good + 1 #いいねが足される
    object.save() #いいねが保存される
    return redirect('list')

def readfunc(request, pk):
    object = snsModel.objects.get(pk=pk) #投稿データを引っ張り出す
    #ユーザー情報を取って既読を押せるか押せないかを処理する
    username = request.user.get_username()
    if username in object.readtext:
        return redirect('list')
    else: 
        object.read = object.read + 1 #いいねが足される
        object.readtext = object.readtext + '  ' + username
        object.save() #いいねが保存される
        return redirect('list')