import os
import django
from django.db import connections
from django.db.utils import OperationalError
from django.http import HttpResponse

# Configura Django para usar settings
import psycopg2

conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
cur = conn.cursor()
cur.execute("SELECT 1;")
print("✅ Conectado a la base de datos")
cur.close()
conn.close()
