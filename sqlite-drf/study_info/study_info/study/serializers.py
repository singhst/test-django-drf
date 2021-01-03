from rest_framework import serializers
from study.models import Study


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        # fields = '__all__' #use all fields in the SQLite database
        fields = ('id', 'Programme', 'University', 'Programme_Fee', 'Country', 'Address', 'Latitude', 'Longitude')

    # class ToUpperCaseCharField(serializers.TextField):
    #     def to_representation(self, value):
    #         return value.upper()