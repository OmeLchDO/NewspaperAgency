from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinValueValidator
from captcha.fields import CaptchaField
from catalog.models import Redactor, Newspaper


class RedactorCreateForm(UserCreationForm):
    MIN_YEARS_OF_EXPERIENCE = 0

    years_of_experience = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(MIN_YEARS_OF_EXPERIENCE)])
    
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
         "first_name", "last_name", "years_of_experience"
        )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by Username.."})
    )


class NewspaperForm(forms.ModelForm):
    redactors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    captcha = CaptchaField()

    class Meta:
        model = Newspaper
        fields = "__all__"


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title.."})
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name.."})
    )
