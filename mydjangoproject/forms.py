from django import forms

from myapp1.models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(min_length=2,
                           widget=forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'input__form'}))
    email = forms.EmailField(min_length=2,
                             widget=forms.EmailInput(attrs={'placeholder': 'Почта', 'class': 'input__form'}))
    surname = forms.CharField(min_length=2,
                              widget=forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'input__form'}))
    number = forms.CharField(min_length=2,
                             widget=forms.TextInput(attrs={'placeholder': 'Телефон', 'class': 'input__form'}))
    message = forms.CharField(min_length=20, widget=forms.Textarea(
        attrs={'placeholder': 'Сообщение', 'cols': 40, 'rows': 3, 'class': 'form__message'}))


class ApplicationFrom(forms.Form):
    name = forms.CharField(min_length=2,
                           widget=forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'input__book', 'size': '40'}))

    email = forms.EmailField(min_length=2,
                             widget=forms.EmailInput(attrs={'placeholder': 'Почта', 'class': 'input__book'}))

    surname = forms.CharField(min_length=2,
                              widget=forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'input__book'}))

    number = forms.CharField(min_length=2,
                             widget=forms.TextInput(attrs={'placeholder': '+7(XXX) XXX XX-XX', 'class': 'input__book'}))

    data = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Туда', 'type': 'date', 'class': 'input__book__calendar'}))

    data2 = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Обратно','type': 'date', 'class': 'input__book__calendar'}))

    place = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'people__input', 'id': 'numberField'}), required=True, min_value=1, max_value=25)

    message = forms.CharField(min_length=20, widget=forms.Textarea(
        attrs={'placeholder': 'Сообщение', 'cols': 40, 'rows': 3, 'class': 'book__message'}))


class EmailForm(forms.Form):
    email2 = forms.EmailField(min_length=2,
                             widget=forms.EmailInput(attrs={'placeholder': 'Почта', 'class': 'email__distribution'}))