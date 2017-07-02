from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views import View

import datetime

from .forms import SortForm, BasicForm, QuestionsForm

from .models import Question, Album

# ----Original----
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# ----Changed to----
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# ----Changed again to----
# from django.template import loader
# def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

# ----Which is equivalent to----
# returns an HttpResponse object of the given template rendered with the given context.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
        'sort_form': SortForm,
    }
    return render(request, 'polls/index.html', context)
# ----Originally----
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# ----Changed to----
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

#----Equivalently---
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

# ----Updated to----
from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# ----Originally----
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

#----Updated to----
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

#----From https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms----
def renew_book_librarian(request, pk):
    book_inst=get_object_or_404(BookInstance, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})

def search(request):
    """ Handle registration form """
    if request.method == 'POST':
        response = dict(
            errors=list(),
        )

        search_result = request.POST['search']

        context = {}
        context['results'] = search_result
        return render(request, 'polls/selected.html', context)
    else:
        return render(request, 'polls/selected.html')


def sort(request):
    """ Handle registration form """
    if request.method == 'POST':
        response = dict(
            errors=list(),
        )

        sort_option = request.POST['sort_choice']

        context = {}
        context['results'] = sort_option
        return render(request, 'polls/selected.html', context)
    else:
        return render(request, 'polls/selected.html')

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'genre', 'image']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'genre']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('polls:index')

class BasicView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "form": BasicForm
        }
        return render(request, "polls/basic.html", context) # Try Django 1.8 & 1.9 http://joincfe.com/youtube

    def post(self, request, *args, **kwargs):
        form = BasicForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

        context = {
            "form": form
        }
        return render(request, "polls/basic.html", context)

class QuestionsView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "form": QuestionsForm
        }
        return render(request, "polls/questions.html", context)

    def post(self, request, *args, **kwargs):
        form = QuestionsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

        context = {
            "form": form
        }
        return render(request, "polls/questions.html", context)