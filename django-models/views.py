from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def role_check(role):
    def check(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(check)

@role_check('Admin')
def admin_view(request):
    return HttpResponse("Welcome, Admin!")

@role_check('Librarian')
def librarian_view(request):
    return HttpResponse("Hello Librarian, manage your books!")

@role_check('Member')
def member_view(request):
    return HttpResponse("Hey Member! Browse and borrow.")