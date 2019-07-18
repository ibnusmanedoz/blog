from django import forms
from todo.models import TodoData
from django.contrib.auth.models import User

class TodoDataForm(forms.ModelForm):
    class Meta():
        model = TodoData
        fields = ('todo_data','when','time')
        widgets = {
            'todo_data':forms.Textarea(
                attrs={
                    'class':'form-control col-lg-6'
                }
            ),
            'when':forms.DateInput(
                attrs={
                    'class':'datepicker col-lg-6'
                }
            ),
            'time':forms.TimeInput(
                attrs={
                    'class':'timepicker col-lg-6'
                }
            )
        }
