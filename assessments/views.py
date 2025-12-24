from rest_framework import viewsets
from .models import Topic, Question
from .serializers import TopicSerializer, QuestionSerializer

class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        topic_name = self.request.query_params.get('topic__name')
        if topic_name:
            queryset = queryset.filter(topic__name=topic_name)
        topic_id = self.request.query_params.get('topic')
        if topic_id:
             queryset = queryset.filter(topic_id=topic_id)
        return queryset
