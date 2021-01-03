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

# === (1) By Manager.raw(), raw SQL query ==============
def fun_raw_sql_query(**kwargs):
    fee = kwargs.get('fee')
    if fee:
        result = Study.objects.raw('SELECT * FROM study WHERE Programme_Fee > %s', [fee])
    else:
        result = Study.objects.raw('SELECT * FROM study')
    return result
# === (1) By Manager.raw(), raw SQL query ==============


# === (2) Executing custom SQL directly ==============
from collections import namedtuple

from django.db import connection

def namedtuplefetchall(cursor):
    # Return all rows from a cursor as a namedtuple
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

#簡單說明一下這段 code，前端可以帶入 id 和 song 來更新資料
def fun_sql_cursor_update(**kwargs):
    country = kwargs.get('country')
    pk = kwargs.get('pk')

    '''
    Note that if you want to include literal percent signs in the query,
    you have to double them in the case you are passing parameters:
    '''
    with connection.cursor() as cursor:
        cursor.execute("UPDATE study SET Country = %s WHERE id = %s", [country, pk])
        cursor.execute("SELECT * FROM study WHERE id = %s", [pk])
        # result = cursor.fetchone()
        result = namedtuplefetchall(cursor)
    result = [
        {
            'id': r.id,
            'Programme': r.Programme,
            'University': r.University,
            'Country': r.Country,
            'Address': r.Address,
            'Latitude': r.Latitude,
            'Longitude': r.Longitude,
            'Programme_Fee': r.Programme_Fee,
        }
        for r in result
    ]

    return result
# === (2) Executing custom SQL directly ==============
