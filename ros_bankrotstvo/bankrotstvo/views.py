from django.shortcuts import render
from bitrix24 import *


def indexPage(request):
    if request.POST:
        treatment(req=request)
        return render(request, 'bankrotstvo/ths.html')
    return render(request,'bankrotstvo/index.html')


def treatment(req):
    webhook = "https://novoedelo.bitrix24.ru/rest/16/nj3wt62rh1o3hypk/"
    b = Bitrix24(webhook)
    fields = {
        "TITLE": "Заявка из РосБанкротства",
        "STATUS_ID": "NEW",
        "SOURCE_DESCRIPTION": "Заявка из РосБанкротства",
        'UF_CRM_1653238944': req.POST.get('Сумма долга', ''),
        'UF_CRM_1653237303': req.POST.get('Имущество[]', ''),
        'UF_CRM_1653236732': req.POST.get('Время не оплаты кредитов', ''),
        'UF_CRM_60D9DCACA6083': req.POST.get('Ипотека', ''),
        'UF_CRM_1654518616': req.POST.get('Алименты', ''),
        'UF_CRM_1654518720': req.POST.get('Рассрочка', ''),
        'UF_CRM_1594822925': req.POST.get('Место жительства', ''),
        "PHONE": [{"VALUE": f"{req.POST.get('phone', '')}", "VALUE_TYPE": "WORK"}],
        'NAME': req.POST['Имя'],
        "UTM_SOURCE": req.GET.get('utm_source', ''),
        "UTM_MEDIUM": req.GET.get('utm_medium', ''),
        "UTM_CONTENT": req.GET.get('utm_content', ''),
        "UTM_CAMPAIGN": req.GET.get('utm_campaign', ''),
        "UTM_TERM": req.GET.get('utm_term', ''),
    }
    addLead = b.callMethod("crm.lead.add", fields=fields)

def thsPage(request):
    return render(request,'bankrotstvo/ths.html')