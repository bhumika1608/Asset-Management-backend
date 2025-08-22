from django.core.management.base import BaseCommand
from assets.models import Asset

class Command(BaseCommand):
    help = 'Set contributedBy for all assets that do not have it.'

    def handle(self, *args, **options):
        default_user = 'default_user'  # Change this to your desired username
        updated = 0
        for asset in Asset.objects.all():
            if not asset.contributedBy:
                asset.contributedBy = default_user
                asset.save()
                updated += 1
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated} assets.'))
