from django import forms
from . import models, parser_lib

class ParserForm(forms.Form):
    MEDIA_CHOISES = (
        ('lib', 'Library'),
        ('lib2', 'Library2')
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOISES)
    class Meta:
        fields =[
            'media_type',
        ]


    def parser_data(self):
        if self.data['media_type'] == 'library':
            file_library = parser_lib.parsing()
            for i in file_library:
                models.LibraryParser.objects.create(**i)