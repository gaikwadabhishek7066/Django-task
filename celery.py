import os
from celery import Celery

# Set default settings module for 'celery' command-line program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_project.settings')

app = Celery('backend_project')

# Load task modules from all registered Django app configs
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks.py in all installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
