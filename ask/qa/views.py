from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage
# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import AskForm, AnswerForm

from .models import Question

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def not_found (request, *args, **kwargs):
#    raise Http404
    return('Not OK')

#/question/5/
@csrf_exempt
def vquestion(request, pk):
    question = get_object_or_404(Question, id=pk)
    answers = question.answer_set.all()
    form = AnswerForm(initial={'question': str(pk)})
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })

# /popular/?page=3
def vpopular(request):
    qs = Question.objects.order_by('-rating')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('popular') + '?page='
    return render(request, 'popular.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })
def vsignup(request, *args, **kwargs):
    return HttpResponse('OK vsignup')

def vlogin(request, *args, **kwargs):
    return HttpResponse('OK vlogin')

#vquestion,vpopular,vquestion_ask,vsignup,vlogin,vlogout,vmainpg,vquestion_ans

def vlogout(request, *args, **kwargs):
    return HttpResponse('OK vlogout')

#/?page=2
def vmainpg(request, *args, **kwargs):
    qs = Question.objects.order_by('-id')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('mainpg')
    return render(request, 'main.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })
@csrf_exempt
def vquestion_ask(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            ask = form.save()
            url = ask.get_url()
            #return HttpResponseRedirect(url)
            return HttpResponseRedirect('OK')
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form
    })
@csrf_exempt
def vquestion_ans(request, *args, **kwargs):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            answer = form.save()
            url = answer.get_url()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect('/')