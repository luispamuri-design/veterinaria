from django.http import HttpResponse
from django.db import connection
from django.db.utils import OperationalError

def test_db(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT DATABASE();")
            db = cursor.fetchone()
        return HttpResponse(f"✅ Conectado a la base de datos: {db[0]}")
    except OperationalError as e:
        return HttpResponse(f"❌ No se pudo conectar a la base de datos: {e}")
