from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

def is_admin(User):
    return hasattr(User, 'UserProfile') and User.Userrofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin!")