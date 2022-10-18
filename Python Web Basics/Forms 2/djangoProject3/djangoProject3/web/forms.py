from django import forms

from djangoProject3.web.models import Todo
from djangoProject3.web.validate import validate_text, ValidationRange


class TodoForm(forms.Form):
    text = forms.CharField(
        validators=(validate_text,
                   ),
    )

    is_done = forms.BooleanField(
        required=False,
    )
    priority = forms.IntegerField(
        validators=(ValidationRange(1, 10),
                    ),
    )


class TodoCreatorForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'