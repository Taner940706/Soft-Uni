from django import forms

from car.web.models import Profile, Car


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'username': forms.TextInput(

            ),
            'email': forms.EmailInput(

            ),
            'age': forms.NumberInput(

            ),
            'password': forms.PasswordInput(

            )
        }


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')


class DeleteCarForm(CreateCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')


class DeleteBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()


class DeleteProfileForm(DeleteBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            Car.objects \
                .all() \
                .delete()
            self.instance.delete()
