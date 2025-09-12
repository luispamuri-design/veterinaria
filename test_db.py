import os
import django
from django.db import connections
from django.db.utils import OperationalError
from django.http import HttpResponse

# Configura Django para usar settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veterinaria.settings')
django.setup()

db_conn = connections['default']

try:
    c = db_conn.cursor()
    c.execute("SELECT DATABASE();")
    row = c.fetchone()
    print(f"✅ Conectado a la base de datos: {row[0]}")
except OperationalError as e:
    print(f"❌ No se pudo conectar a la base de datos: {e}")
