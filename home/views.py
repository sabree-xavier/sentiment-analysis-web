from wsgiref.util import FileWrapper
from django.shortcuts import redirect, render
from django.http import FileResponse, StreamingHttpResponse
import mimetypes 
from .models import *
from .views import *
from .forms import *
from home.utility import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login

from datetime import datetime, timedelta
from pytz import timezone

def home_view(request):
    user_ip = get_client_ip(request)
    tz = timezone('EST')

    if not request.user.is_authenticated:
        user, created = get_user_model().objects.get_or_create(username=user_ip)
        login(request, user)

    if request.method == 'POST':
        review_text = request.POST.get('review', '')

        if review_text == "random":
            review_text = createRandomReview() 
            str(review_text).replace('\"', "")
        else:
            review_text = "\"" + review_text + "\""
        sentiment_value = calculateSentimentValue(review_text)
        
        review = ReviewModel(review=review_text, user=str(user_ip),timestamp_field=datetime.now(tz) - timedelta(hours=4), sentiment_value=sentiment_value)
        if(review_text != ""):
            review.save()

    reviews = ReviewModel.objects.all()

    context = {
        'reviews': reviews,
        'user' : user_ip,
        'resume': ResumeModel.objects.all(),
        'current_page': 0
    }

    return render(request, 'home.html', context)