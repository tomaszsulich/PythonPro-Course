"""
URL configuration for celery_lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from background_tasks.views import (
    create_email_notification_view,
    csv_report_status_view,
    generate_report_view,
    generate_users_csv_view,
    hello_world_view,
    image_result_view,
    multiply_view,
    process_video_view,
    send_priority_email_view,
    start_chain_view,
    start_progress_task_view,
    task_status_view,
    upload_image_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-email-notification/', create_email_notification_view, name='create_email_notification'),
    path('csv-report-status/<str:task_id>/', csv_report_status_view, name='csv_report_status'),
    path('generate-report/', generate_report_view, name='generate_report'),
    path('generate-users-csv/', generate_users_csv_view, name='generate_users_csv'),
    path('hello-world/', hello_world_view, name='hello_world'),
    path('image-result/<int:image_id>/', image_result_view, name='image_result'),
    path('multiply/', multiply_view, name='multiply'),
    path('process-video/', process_video_view, name='process_video'),
    path('send-priority-email/', send_priority_email_view, name='send_priority_email'),
    path('start-chain/', start_chain_view, name='start_chain'),
    path('start-progress-task/', start_progress_task_view, name='start_progress_task'),
    path('task-status/<str:task_id>/', task_status_view, name='task_status'),
    path('upload-image/', upload_image_view, name='upload_image'),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)