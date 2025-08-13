from .models import StudySetting

def settings(request):
    return {'settings': StudySetting.load()}