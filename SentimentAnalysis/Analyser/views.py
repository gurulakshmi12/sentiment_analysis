from django.shortcuts import render, redirect
from .forms import TextInputForm, SentimentForm
from .models import SentimentAnalysis
from transformers import pipeline

# Initialize the sentiment analysis pipeline once
nlp = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def index(request):
    form = TextInputForm()
    return render(request, 'index.html', {'form': form})

def analyze_sentiment(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            result = nlp(user_input)[0]
            sentiment_score = result['score']
            sentiment_label = result['label']
            analysis = SentimentAnalysis(
                user_input=user_input,
                sentiment_score=sentiment_score,
                sentiment_label=sentiment_label
            )
            analysis.save()
            return redirect('result', analysis_id=analysis.id)
    else:
        form = TextInputForm()
    
    
    return render(request, 'index.html', {'form': form})

def result(request, analysis_id):
    analysis = SentimentAnalysis.objects.get(id=analysis_id)
    return render(request, 'result.html', {
        'user_input': analysis.user_input,
        'sentiment_score': analysis.sentiment_score,
        'sentiment_label': analysis.sentiment_label
    })

def history(request):
    analyses = SentimentAnalysis.objects.all().order_by('-created_at')
    return render(request, 'history.html', {'analyses': analyses})
