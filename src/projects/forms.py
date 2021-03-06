from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import CustomUser
from projects.models import Project, Client
from engineers.models import Partner, Skill


class EntryForm(forms.ModelForm):
    """案件登録用のフォーム"""

    class Meta:
        # 利用するモデルクラスを指定
        model = Project
        # 利用するモデルのフィールドを指定
        fields = (
            'name', 'description', 'skills', 'location', 'project_date', 'start_time', 'end_time', 'partners')

    name = forms.CharField(
        label='案件名',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '案件名'}),
    )
    description = forms.CharField(
        label='案件詳細',
        max_length=2000,
        required=True,
        strip=False,
        widget=forms.Textarea(attrs={'placeholder': '案件詳細'}),
    )
    skills = forms.CharField(
        label='必要資格',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'data-target': 'modal1', 'id': '_skill_val', 'placeholder': '必要資格'}),
    )
    location = forms.CharField(
        label='場所',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '場所'}),
    )
    project_date = forms.DateField(
        label='案件日',
        required=True,
        widget=forms.DateInput(attrs={'placeholder': '案件開始日', 'type': 'date'}),
    )
    start_time = forms.TimeField(
        label='開始時刻',
        required=True,
        widget=forms.TimeInput(attrs={'placeholder': '開始時刻', 'type': 'time', 'value': ':00'}),
    )
    end_time = forms.TimeField(
        label='終了時刻',
        required=True,
        widget=forms.TimeInput(attrs={'placeholder': '終了時刻', 'type': 'time', 'value': ':00'}),
    )
    partners = forms.ModelMultipleChoiceField(
        label='取引先',
        required=True,
        queryset=Partner.objects,
        widget=forms.SelectMultiple()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO 修正したい
        for field in self.fields.values():
            if field.label == '必要資格':
                field.widget.attrs['class'] = 'form-control modal_open'
            else:
                field.widget.attrs['class'] = 'form-control'


class EditForm(forms.ModelForm):
    """案件編集用のフォーム"""

    class Meta:
        # 利用するモデルクラスを指定
        model = Project
        # 利用するモデルのフィールドを指定
        fields = (
            'id', 'name', 'description', 'skills', 'location', 'project_date', 'start_time', 'end_time', 'partners')

    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    name = forms.CharField(
        label='案件名',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '案件名'}),
    )
    description = forms.CharField(
        label='案件詳細',
        max_length=2000,
        required=True,
        strip=False,
        widget=forms.Textarea(attrs={'placeholder': '案件詳細'}),
    )
    skills = forms.CharField(
        label='必要資格',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'data-target': 'modal1', 'id': '_skill_val', 'placeholder': '必要資格'}),
    )
    location = forms.CharField(
        label='場所',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '場所'}),
    )
    project_date = forms.DateField(
        label='案件日',
        required=True,
        widget=forms.DateInput(attrs={'placeholder': '案件開始日', 'type': 'date'}),
    )
    start_time = forms.TimeField(
        label='開始時刻',
        required=True,
        widget=forms.TimeInput(attrs={'placeholder': '開始時刻', 'type': 'time'}),
    )
    end_time = forms.TimeField(
        label='終了時刻',
        required=True,
        widget=forms.TimeInput(attrs={'placeholder': '終了時刻', 'type': 'time'}),
    )
    partners = forms.ModelMultipleChoiceField(
        label='取引先',
        required=True,
        queryset=Partner.objects,
        widget=forms.SelectMultiple()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO 修正したい
        for field in self.fields.values():
            if field.label == '必要資格':
                field.widget.attrs['class'] = 'form-control modal_open'
            else:
                field.widget.attrs['class'] = 'form-control'
