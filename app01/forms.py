from django import forms
from django.forms import widgets
from django.core.validators import ValidationError


class RegForm(forms.Form):
    username = forms.CharField(label='用户名a')
    password = forms.CharField(label='密码',
                               min_length=4,
                               widget=widgets.PasswordInput
                               )
    re_password = forms.CharField(label='确认密码',
                                  min_length=4,
                                  widget=widgets.PasswordInput
                                  )

    def clean(self):
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')
        if pwd == re_pwd:
            return self.cleaned_data
        self.add_error('re_password', '两次密码不一致')
        raise ValidationError('两次密码不一致')
