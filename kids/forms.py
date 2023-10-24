from django import forms


class ColdForm(forms.Form):
    until_3_month = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                           choices=((False, 'خیر'), (True, 'بله')),
                                           label='آیا کودک شما زیر ۳ ماه است',
                                           widget=forms.Select(attrs={'class': 'form-select'}))
    fever = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                   choices=((False, 'خیر'), (True, 'بله')),
                                   label='آیا کودک شما تبی بیش از ۳۸/۵ درجه سانتی گراد دهانی یا ۳۹ درجه سانتی گراد مقعدی دارد',
                                   widget=forms.Select(attrs={'class': 'form-select'}))
    ailment = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                     choices=((False, 'خیر'), (True, 'بله')),
                                     label='آیا کودک به شدت احساس ناخوشی می کند',
                                     widget=forms.Select(attrs={'class': 'form-select'}))
    breath = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                    choices=((False, 'خیر'), (True, 'بله')),
                                    label='آیا کودک شما در بلع مشکل شدید دارد',
                                    widget=forms.Select(attrs={'class': 'form-select'}))
