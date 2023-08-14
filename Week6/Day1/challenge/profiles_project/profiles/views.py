from .models import Profile
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(name)
        print(email)
        profile = Profile.objects.create(name=name, email=email)
        return JsonResponse({'201': f'Profile {profile.name} with email {profile.email} created.'})

@csrf_exempt
def delete_profile(request, profile_id):
    if request.method == 'DELETE':
        profile = Profile.objects.get(id=profile_id)
        profile.delete()
        return HttpResponse(f'profile {profile_id} was deleted.')
    