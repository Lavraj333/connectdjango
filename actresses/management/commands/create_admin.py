from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create or reset superuser'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if User.objects.filter(username='admin').exists():
            # Reset password if user already exists
            user = User.objects.get(username='admin')
            user.set_password('glamour2025')
            user.save()
            self.stdout.write(self.style.SUCCESS('✅ Password reset to glamour2025'))
        else:
            User.objects.create_superuser(
                username='admin',
                email='admin@glamour.com',
                password='glamour2025'
            )
            self.stdout.write(self.style.SUCCESS('✅ Superuser created!'))