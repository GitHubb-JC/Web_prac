import random
from django.shortcuts import render

# Create your views here.
def index(request):
    # 환영하는 메인 페이지를 보여준다
    names = ['메더', '레시라무', '제크로무', '요가람', '솔가레오']
    name = random.choice(names)
    context = {
        'name': name,
        'img': 'https://lh3.googleusercontent.com/RGShDyVofSODXIJ0eQ9umAID8tCw9KdqBFrtgCEdrxjJijG1qZBryfECP9IRV1MOJhCk4Za4VYB34DE-hnPesZNNVYMwgHKs9KrNue3LNJRJuw=rw-e365-w1440',
    }
    return render(request, 'index.html', context)

def welcome(request, name):
    # print(name)
    context = {
        'name': name,
        'greetings': ['레시', '제크', '큐레']
    }
    return render(request, 'welcome.html', context)