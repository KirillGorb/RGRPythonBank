from django.shortcuts import render
from .models import Account
from registration.models import User

def main_window(request):
    user = User.objects.get(pk=request.session.get('user_id'))
    account = Account.objects.get(user=user)

    positiveTweet = [i * 5 for i in range(20)]
    youtube_video_id = 'https://youtu.be/8NdDwcXNwiA'
    context = {
        'youtube_video_id':youtube_video_id,
        'positiveTweet': positiveTweet,
        'account': account
    }
    return render(request, 'account/index.html', context)
