from base.models import Setting, Social
from order.service import order_service


def context_controller(request):
    settings = Setting.get_settings()
    socials = Social.objects.filter()

    order = order_service.get_order(request)

    context = {
        'settings': settings,
        'socials': socials,
        'order': order,
    }
    return context
