from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label="Select Group")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'group')

    def save(self, commit=True):
        user = super().save(commit=False)
        group = self.cleaned_data['group']

        if commit:
            user.save()
            user.groups.add(group)

        return user
