from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Delete users'

    def add_arguments(self, parser):
        parser.add_argument('arg1', nargs='+', type=int)
        # parser.add_argument('arg2', nargs='*', default=[1,2,3])
        # parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
        # parser.add_argument('numb', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        my_list = options['arg1']
        for i in my_list:
            u1 = User.objects.get(is_superuser=1)
            u2 = User.objects.get(pk=i)
            if u1 == u2:
                self.stdout.write(self.style.SUCCESS(f"Удалите суперпользователя из списка"))
                exit()
        for i in my_list:
            User.objects.get(pk=i).delete()

        self.stdout.write(self.style.SUCCESS(f"Удалены пользователи с id: {my_list}"))
