from base.models import Setting, Social


def context_controller(request):
    settings = Setting.get_settings()
    socials = Social.objects.filter()

    context = {
        'settings': settings,
        'socials': socials,
    }
    return context
