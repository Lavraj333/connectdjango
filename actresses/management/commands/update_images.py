import json
from django.core.management.base import BaseCommand
from actresses.models import Actress

class Command(BaseCommand):
    help = 'Update actress images from fixtures file'

    def handle(self, *args, **kwargs):
        try:
            with open("actresses/fixtures/actresses.json", encoding="utf-8") as f:
                data = json.load(f)

            for item in data:
                pk = item["pk"]
                name = item["fields"]["name"]
                profile_path = item["fields"]["profile_path"]

                if profile_path:
                    Actress.objects.filter(pk=pk).update(profile_path=profile_path)
                    self.stdout.write(f"✅ {name}")
                else:
                    self.stdout.write(f"⏭ Skipped {name}")

            self.stdout.write(self.style.SUCCESS("✅ All images updated!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Error: {e}"))