from django.http import HttpResponsePermanentRedirect

def permanent_redirect(request):
    return HttpResponsePermanentRedirect("/polls/")