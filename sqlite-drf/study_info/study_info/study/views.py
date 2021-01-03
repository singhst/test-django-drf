# Create your views here.
from study.models import Study
from study.serializers import StudySerializer

from rest_framework import viewsets


# By "Django ORM" only
# # Create your views here.
# class StudyViewSet(viewsets.ModelViewSet):
#     queryset = Study.objects.all()
#     serializer_class = StudySerializer

# === (1) By Manager.raw(), raw SQL query ==============
from rest_framework.decorators import action
from study.models import fun_raw_sql_query
from rest_framework.response import Response
from rest_framework import viewsets, status
# === (1) By Manager.raw(), raw SQL query ==============

# === (2) Executing custom SQL directly ==============
from study.models import fun_sql_cursor_update
# === (2) Executing custom SQL directly ==============

# Create your views here.
class StudyViewSet(viewsets.ModelViewSet):
    queryset = Study.objects.all()
    serializer_class = StudySerializer

    # === (1) By Manager.raw(), raw SQL query ==============
    # /api_v2/study/raw_sql_query/?fee=50000
    @action(methods=['get'], detail=False)
    def raw_sql_query(self, request):
        fee = request.query_params.get('fee', None)
        study = fun_raw_sql_query(fee=fee)
        serializer = StudySerializer(study, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # === (1) By Manager.raw(), raw SQL query ==============

    # === (2) Executing custom SQL directly ==============
    # /api_v2/study/{pk}/sql_cursor_update/
    """ 
    e.g. Update the `id=2701` row & `Country column` to "test". 
    Request method: PUT 
    URL:            http://127.0.0.1:8000/api_v2/study/2701/sql_cursor_update/
    Body JSON:      {
                        "Country": "sql_put"
                    }
    """
    @action(methods=['put'], detail=True)
    def sql_cursor_update(self, request, pk=None):
        country = request.data.get('Country', None)
        if country:
            study_info = fun_sql_cursor_update(country=country, pk=pk)
            return Response(study_info, status=status.HTTP_200_OK)
    # === (2) Executing custom SQL directly ==============
