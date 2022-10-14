from django import forms
from django.shortcuts import render

from Forms.web.models import Person


# Create your views here.


class NameForms(forms.Form):
    OCCUPANCES = (
        (1, 'child'),
        (2, 'high school students'),
        (3, 'students'),
        (4, 'adult'),
    )
    your_name = forms.CharField(max_length=30,
                                label='My name',
                                help_text="Typeyou name!",)
    age = forms.IntegerField(max_value=30, label='My age', initial=7, widget=forms.NumberInput())

    story = forms.CharField(
        widget=forms.Textarea,
    )

    occupances = forms.ChoiceField(choices=OCCUPANCES,)
    occupances2 = forms.ChoiceField(choices=OCCUPANCES, widget=forms.RadioSelect)



def index(request):
    name = None
    if request.method == 'GET':
        form = NameForms()
    else:
        form = NameForms(request.POST)
        form.is_valid()
        name = form.cleaned_data['your_name']
        Person.objects.create(
            name=name
        )
    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'index.html', context)
