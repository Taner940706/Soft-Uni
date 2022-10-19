import uuid

from django import forms

from djangoProject3.web.models import Todo, Person
from djangoProject3.web.validate import validate_text, ValidationRange


class TodoForm(forms.Form):
    text = forms.CharField(
        validators=(validate_text,),
        error_messages={
            'required': 'Todo text must be set!'
        }
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


class PersonCreatorForm(forms.Form):
    class Meta:
        model = Person
        field = '__all__'

    def clean_profile_image(self):
        profile_image = self.cleaned_data['profile_image']
        profile_image.name = str(uuid.uuid4())
        return profile_image
