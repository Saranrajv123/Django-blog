from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    def signals(self):
        import users.signals
