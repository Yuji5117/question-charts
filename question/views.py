from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from .models import Question, Choice

# Questionを新しい順に取得し表示させる #
def index(request):
    new_question_list = Question.objects.order_by('-created_at')[:5]
    context = {
        'new_question_list': new_question_list,
    }
    return render(request, 'question/index.html', context)

# QuestionのIDを取得し詳細を表示させる #
def questionDetail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    
    context = {
        'question': question,
    }
    return render(request, 'question/detail.html', context)

# Questionを取得し、結果をさせる #
def questionResults(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context = {
        'question': question,
    }
    return render(request, 'question/results.html', context)

#  #
def questionVote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': "You didn't select a choice."
        }
        return render(request, 'question/detail.html', )
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('question:results', args=(question.id,)))


def resultsData(request, obj):
    votedata = []

    question = Question.objects.get(id=obj)
    votes = question.choice_set.all()

    for vote in votes:
        votedata.append({vote.choice_text:vote.votes})

    print(votedata)
    return JsonResponse(votedata, safe=False)