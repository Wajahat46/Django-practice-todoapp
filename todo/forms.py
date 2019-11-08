from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "input", "placeholder": "Enter todo !!"}
        ),
        max_length=40,
    )

