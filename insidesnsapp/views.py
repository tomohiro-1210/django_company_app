from django.shortcuts import render
from django.contrib.auth.models import User #ユーザーモデルの読み込み
from django.db import IntegrityError #重複したときのエラー


# Create your views here.
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '' ,password)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています。'})# {}はモデルまたは任意で出したデータ


    return render(request, 'signup.html', {})# {}はモデルまたは任意で出したデータ