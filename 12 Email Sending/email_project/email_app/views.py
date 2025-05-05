from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormDataForm

def send_email(request):
    subject = 'Test Email with Attachments'
    from_email = 'your mail id'
    to_email = ['recipient mail id']  # Convert to a list for multiple recipients

    # Render HTML content from template
    html_content = render_to_string('email_template.html', {'recipient_name': 'Recipient'})

    # Create EmailMessage object
    email = EmailMultiAlternatives(subject, 'Text content here', from_email, to_email)
    email.attach_alternative(html_content, "text/html")

    # Add custom headers
    email.extra_headers['X-Mailer'] = 'Django Mailer'

    # Send email
    try:
        email.send()
        return HttpResponse('Congrats! Email sent successfully!')
    except Exception as e:
        return HttpResponse(f'An error occurred: {str(e)}')

def form_view(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            attachment = request.FILES['attachment']

            # Prepare the email
            subject = 'Form Submission'
            message = 'Thank you for your submission!'
            from_email = 'your mail id'
            to_email = [email]

            email = EmailMessage(subject, message, from_email, to_email)
            email.attach(attachment.name, attachment.read(), attachment.content_type)  # Use attach instead of attach_file

            # Send the email
            try:
                email.send()
                return render(request, 'success.html')
            except Exception as e:
                return render(request, 'error.html', {'error_message': str(e)})
    else:
        form = FormDataForm()
    return render(request, 'form.html', {'form': form})  


