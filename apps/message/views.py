from django.shortcuts import render

# Create your views here.
from apps.message.models import UserMessage


def getform(request):
    '''
    通过orm生成的对象model 进行增删改查
    :param request:
    :return:
    '''
    all_messages =UserMessage.objects.filter(name='BensonMax',address='广州')
    #all_messages.delete()
    #all_messages = UserMessage.objects.all()
    #for message in all_messages:
    #    message.delete()
    # if request.method == "POST":
    #     name = request.POST.get('name','')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "helloworld3"
    #
    #     user_message.save()

    return render(request, 'message_form.html')