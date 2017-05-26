from django.shortcuts import render

from .models import UserMessage
# Create your views here.
def getform(request):
    # 取所有
    # all_message = UserMessage.objects.all()
    # for message in all_message:
    #     print(message.name)

    # where
    # all_message = UserMessage.objects.filter(name="xuxule", address="金华")
    # all_message.delete() # 批量删除
    # for message in all_message:
    #   message.delete() # 单个删除

    # 添加数据
    # user_message = UserMessage()
    # user_message.name = 'paidaxing'
    # user_message.email = '819384406@qq.com'
    # user_message.address = '温州'
    # user_message.message = 'oo'
    # user_message.save()

    # if request.method == 'POST':
    #     user_message = UserMessage()
    #     user_message.name = request.POST['name']
    #     user_message.email = request.POST.get('email', '')
    #     user_message.address = request.POST.get('address', '')
    #     user_message.message = request.POST.get('message', '')
    #     user_message.save()

    message = None
    all_message = UserMessage.objects.filter(name = 'paidaxing')
    if all_message:
        message = all_message[0]

    return render(request, 'message_form.html', {
        'my_message': message
    })