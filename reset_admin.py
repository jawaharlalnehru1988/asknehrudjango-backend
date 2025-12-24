import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asknehrudjango.settings')
django.setup()

from django.contrib.auth.models import User

username = 'admin'
password = 'admin123'
email = 'admin@example.com'

try:
    if User.objects.filter(username=username).exists():
        u = User.objects.get(username=username)
        u.set_password(password)
        u.save()
        print(f"Password for user '{username}' has been reset to '{password}'.")
    else:
        User.objects.create_superuser(username, email, password)
        print(f"User '{username}' created with password '{password}'.")
except Exception as e:
    print(f"An error occurred: {e}")
