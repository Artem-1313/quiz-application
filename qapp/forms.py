from django import forms


class addQuiz(forms.Form):
    options = forms.CharField(widget=forms.TextInput())
    is_right = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[('1','')], required=False)
