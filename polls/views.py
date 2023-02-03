from django.http import HttpResponse
from django.template import loader

from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import permissions

from polls.models import Question, Choice, Tag


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['url', 'question_text', 'choice_set', ]


class ChoiceSerializer(serializers.ModelSerializer):
    included_serializers = {
        'question': QuestionSerializer,
    }
    class Meta:
        model = Choice
        fields = ['choice_text', 'question', ]


class TagSerializer(serializers.HyperlinkedModelSerializer):
    included_serializers = {
        'choice': ChoiceSerializer,
    }

    # class JSONAPIMeta:
        # included_resources = ['choice']
    class Meta:
        model = Tag
        fields = ['url', 'tag_text', 'choice', ]


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tag.objects.all().prefetch_related('choice', 'choice__question')
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
    # renderer_classes = (JSONRenderer, )
    pagination_class = None

    def list(self, *args, **kwargs):
        resp = super().list(*args, **kwargs)
        import pdb; pdb.set_trace()
        return resp


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('-pub_date').prefetch_related('choice_set')
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
    # renderer_classes = (JSONRenderer, )
    pagination_class = None


class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    # renderer_classes = (JSONRenderer, )
    pagination_class = None


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }

    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
