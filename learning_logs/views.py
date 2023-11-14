from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    
    return render(request, 'learning_logs/topic.html', {'topic': topic, 'entries': entries})

def create_topic(request):
    """Create new topic"""
    if request.method != 'POST':
        # No data submitted create a blank form
        form = TopicForm()
    else:
        # POST data submitted process the data
        form = TopicForm(data=request.POST) 
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    # deplay a black or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/create_topic.html', context)

def create_entry(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        # No data submitted, display blank form
        form = EntryForm()
    else:
        # Data submitted, process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            create_entry = form.save(commit=False)
            create_entry.topic = topic
            create_entry.save()
            
            return redirect('learning_logs:topic', topic_id = topic_id)
    
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/create_entry.html', context)

def edit_entry(request, entry_id):
      
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)