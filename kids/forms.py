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
                                    label='آیا کودک شما در تنفس مشکل دارد',
                                    widget=forms.Select(attrs={'class': 'form-select'}))
    swallow = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                     choices=((False, 'خیر'), (True, 'بله')),
                                     label='آیا کودک شما در بلع مشکل شدید دارد',
                                     widget=forms.Select(attrs={'class': 'form-select'}))
    fever_3_days = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                          choices=((False, 'خیر'), (True, 'بله')),
                                          label='آیا تب بیش از ۳۷/۵ درجه سانتی گراد دهانی یا ۳۸ درجه سانتی گراد مقعدی بیش از ۳ روز وجود دارد',
                                          widget=forms.Select(attrs={'class': 'form-select'}))
    liquids = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                     choices=((False, 'خیر'), (True, 'بله')),
                                     label='آیا کودک به خوبی مایعات نمی نوشد',
                                     widget=forms.Select(attrs={'class': 'form-select'}))
    discharge = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                       choices=((False, 'خیر'), (True, 'بله')),
                                       label='آیا ترشح بینی پیوسته سبز رنگ است',
                                       widget=forms.Select(attrs={'class': 'form-select'}))
    sputum = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                    choices=((False, 'خیر'), (True, 'بله')),
                                    label='آیا کودک خلط سبز رنگ دارد',
                                    widget=forms.Select(attrs={'class': 'form-select'}))
