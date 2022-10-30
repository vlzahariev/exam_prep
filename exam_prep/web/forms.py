from django import forms

from exam_prep.web.models import Profile, Album


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()

        return self.instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': "Album Name"
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': "Artist"
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': "Description"
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': "Image URL"
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': "Price"
                }
            ),
        }


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    disabled_fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __init__(self, *args, **kwargs):
        super(AlbumDeleteForm, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True

