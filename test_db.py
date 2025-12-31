#!/usr/bin/env python3
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asknehrudjango.settings')
django.setup()

from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT version();")
    version = cursor.fetchone()[0]
    print("✓ PostgreSQL Connection Successful!")
    print(f"✓ Database Version: {version}")
    
    cursor.execute("SELECT COUNT(*) FROM django_migrations;")
    count = cursor.fetchone()[0]
    print(f"✓ Migrations Applied: {count}")
    
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()
    print(f"✓ Total Tables: {len(tables)}")
    print("\nTables in database:")
    for table in tables:
        print(f"  - {table[0]}")
