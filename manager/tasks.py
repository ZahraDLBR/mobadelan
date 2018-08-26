from celery.schedules import crontab
from celery.task import periodic_task
from datetime import timedelta
from django.utils import timezone

#from core.models import Staff

from celery import Celery

#@periodic_task(run_every=timedelta(seconds=10))
#def recover_access():
#    print("here")

#    staff_list = Staff.objects.all()

    # for staff in staff_list:
    #     if staff.user.is_active == False:
    #
    #         if staff.ban_expiration_date < timezone.now():
    #             print("there")
    #             staff.user.is_active = True
    #             staff.save()


app = Celery('tasks', broker='redis//localhost')

@app.task
def add(x, y):
    return x + y



