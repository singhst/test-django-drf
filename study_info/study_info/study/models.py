from django.db import models


# Create your models here.
class Study(models.Model):
    Programme = models.TextField()
    University = models.TextField()
    Programme_Fee = models.IntegerField()
    Country = models.TextField()
    Address = models.TextField()
    Latitude = models.TextField()
    Longitude = models.TextField()

    class Meta:
        db_table = "study"

# === By Manager.raw(), raw SQL query ==============
def fun_raw_sql_query(**kwargs):
    fee = kwargs.get('fee')
    if fee:
        result = Study.objects.raw('SELECT * FROM study WHERE Programme_Fee > %s', [fee])
    else:
        result = Study.objects.raw('SELECT * FROM study')
    return result