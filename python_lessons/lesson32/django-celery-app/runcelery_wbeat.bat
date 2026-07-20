start "Celery Worker" cmd /k celery -A core worker -l INFO --pool=solo
start "Celery Beat" cmd /k celery -A core beat -l INFO