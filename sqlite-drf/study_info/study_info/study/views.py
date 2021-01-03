# Create your views here.
from study.models import Study
from study.serializers import StudySerializer

from rest_framework import viewsets


# By "Django ORM" only
# # Create your views here.
# class StudyViewSet(viewsets.ModelViewSet):
#     queryset = Study.objects.all()
#     serializer_class = StudySerializer

# === By Manager.raw(), raw SQL query ==============
from rest_framework.decorators import action
from study.models import fun_raw_sql_query
from rest_framework.response import Response
from rest_framework import viewsets, status

# Create your views here.
class StudyViewSet(viewsets.ModelViewSet):
    queryset = Study.objects.all()
    serializer_class = StudySerializer

    # /api_v2/study/raw_sql_query/
    @action(methods=['get'], detail=False)
    def raw_sql_query(self, request):
        fee = request.query_params.get('fee', None)
        study = fun_raw_sql_query(fee=fee)
        serializer = StudySerializer(study, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# === By Manager.raw(), raw SQL query ==============