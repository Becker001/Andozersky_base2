from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template

from myapp1.models import Contact, Application
from mydjangoproject.forms import ContactForm, ApplicationFrom


# Create your views here.


def index_page(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            surname = form.cleaned_data['surname']
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']

            # Создание и сохранение экземпляра модели Contact
            contact = Contact(name=name, email=email, surname=surname, number=number, message=message)
            contact.save()

            send_message(name, surname, email, number, message)
            context = {'success': 1}

    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'index.html', context=context)



def send_message(name, surname, email, number, message):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'surname': surname, 'email': email, 'number': number, 'message': message}
    subject = 'Сообщение от пользователя'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_context = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['alexbaratov387@gmail.com'])
    msg.attach_alternative(html_context, 'text/html')
    msg.send()




def book_page(request):
    context = {}
    if request.method == 'POST':
        form = ApplicationFrom(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            surname = form.cleaned_data['surname']
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']
            data = form.cleaned_data['data']
            data2 = form.cleaned_data['data2']
            place = form.cleaned_data['place']

            # Создание и сохранение экземпляра модели Contact
            application = Application(name=name, email=email, surname=surname, number=number, message=message, data=data, data2=data2, place=place)
            application.save()

            send_application(name, surname, email, number, message, data, data2, place)
            context = {'success': 1}

    else:
        form = ApplicationFrom()
    context['form'] = form
    return render(request, 'book.html', context=context)

def send_application(name, surname, email, number, message, data, data2, place):
    text = get_template('application.html')
    html = get_template('application.html')
    context = {'name': name, 'surname': surname, 'email': email, 'number': number, 'message': message, 'data': data, 'data2': data2, 'place': place}
    subject = 'Сообщение от пользователя'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_context = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['alexbaratov387@gmail.com'])
    msg.attach_alternative(html_context, 'text/html')
    msg.send()



def about_page(request):
    return render(request, 'about.html')


def services_page(request):
    return render(request, 'services.html')


def feedback_page(request):
    return render(request, 'feedback.html')


def contact_page(request):
    return render(request, 'contact.html')

# def index_page (request):
#     context = {}
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             send_message(form.cleaned_data['name'], form.cleaned_data['surname'], form.cleaned_data['email'], form.cleaned_data['number'], form.cleaned_data['message'])
#             context = {'success': 1}
#     else:
#         form = ContactForm()
#     context['form'] = form
#     return render(request, 'index.html', context=context)
#
# def book_page(request):
#     return render(request, 'book.html')
#
#
# def send_message(name, surname, email, number, message):
#     text = get_template('message.html')
#     html = get_template('message.html')
#     context = {'name': name, 'surname': surname, 'email': email, 'number': number, 'message': message}
#     subject = 'Сообщение от пользователя'
#     from_email = 'from@example.com'
#     text_content = text.render(context)
#     html_context = html.render(context)
#
#     msg = EmailMultiAlternatives(subject, text_content, from_email, ['manager@example.com'])
#     msg.attach_alternative(html_context, 'text/html')
#     msg.send()
