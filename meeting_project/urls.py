<<<<<<< HEAD
=======
 
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
# meeting_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meeting_app.urls')),
]