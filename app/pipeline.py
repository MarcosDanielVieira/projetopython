# app/pipeline.py

def set_staff_status(strategy, details, user=None, *args, **kwargs):
    if user and not user.is_staff:
        user.is_staff = True
        user.save()
