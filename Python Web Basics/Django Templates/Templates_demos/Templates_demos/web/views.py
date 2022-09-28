import _random
from datetime import datetime

from django.shortcuts import render, redirect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Name: {self.name} and age: {self.age}'


def index(request):
    context = {
        'title': 'SoftUni Homepage',
        'value': _random.Random(),
        'info': {
            'address': 'Varna',
        },
        'student': Student('Taner', 27),
        'now': datetime.now(),
        'students': [
            'pesh',
            'gosho',
            'maria',
            'stamat'
        ],
        'values': list(range(1,20))
    }

    return render(request, 'index.html', context)


def redirect_to_home(request):
    return redirect('index')


def about(request):
    render(request, 'about.html')