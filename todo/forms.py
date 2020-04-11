from django import forms
from .models import Todo


class TodoForm(forms.Form):
    text = forms.CharField(max_length=80, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g. Delete junk files',
               'aria-label': 'Todo', 'aria-describedby': 'add-btn'}
    ))


class MainTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g. Delete junk files',
                       'aria-label': 'Todo', 'aria-describedby': 'add-btn'}
            )

        }
