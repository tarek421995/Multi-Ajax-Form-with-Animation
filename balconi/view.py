from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.template import Context
def test_form(request):
    context ={
        'tarek':'tarek'
    }
    if request.method == "POST":
        firstName = request.POST.get("first")
        lastName = request.POST.get("last")
        nickName = request.POST.get("nick")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        about = request.POST.get("about")
        github = request.POST.get("github")
        linkedin = request.POST.get("linkedin")
        work = request.POST.get("work")
        achive = request.POST.get("achive")
        country = request.POST.get("country")
        city = request.POST.get("city")
        postCode = request.POST.get("postCode")
        msg = {
            'first' : firstName,
            'last' : lastName,
            'nick' : nickName,
            'email' :email,
            'phone' : phone,
            'about' : about,
            'github' : github,
            'linkedin' :linkedin,
            'work' : work,
            'achive' :achive , 
            'country':country,
            'city' : city,
            'postCode' : postCode,
        }
        # htmly = get_template('email.html')

        msg_html = render_to_string('email.html', {'msg': msg})
        print(msg)
        # d = Context({ 'msg': msg })
        # text_content = ''
        # html_content = htmly.render(d)
        # msg = EmailMultiAlternatives(
        #     'Form Test Assesment',
        #      text_content,
        #      settings.EMAIL_HOST_USER,
        #     [settings.EMAIL_HOST_USER],
        #       )
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()
        send_mail(
            subject='Form Test Assesment',
            message='',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS],
            html_message=msg_html,
            fail_silently=False)
        return JsonResponse({"message": "Success! Your card was added."})
    return render(request, "base.html", context)