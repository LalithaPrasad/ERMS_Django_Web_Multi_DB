from app_django.models import Admin, Employee

class DBRouter:

    def db_for_read(self, model, **hints):
        if model=='Admin':
            return 'admindata'
        elif model=='Employee':
            return 'empdata'
        else:
            return 'default'

    def db_for_write(self, model, **hints):
        if model=='Admin':
            return 'admindata'
        elif model=='Employee':
            return 'empdata'
        else:
            return 'default'
