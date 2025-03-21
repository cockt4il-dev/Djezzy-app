from django.core.management.base import BaseCommand
from django.core.cache import cache
from django.db.models import Count, DateTimeField, F
from django.db.models.functions import TruncMonth, Cast
from calc.models import NPSResponses

class Command(BaseCommand):
    help = "Preload the cache with monthly data"

    def handle(self, *args, **kwargs):
        data = (
            NPSResponses.objects
            .annotate(parsed_date=Cast('response_dttm', DateTimeField()))
            .annotate(month=TruncMonth('parsed_date'))
            .values(month=F('month'))
            .annotate(count=Count('id'))
            .order_by('month')
        )

        labels = [entry["month"].strftime("%Y-%m") for entry in data]
        counts = [entry["count"] for entry in data]
        response_data = {"labels": labels, "data": counts}

        # Store in cache for 1 hour
        cache.set("monthly_data", response_data, 3600)

        self.stdout.write(self.style.SUCCESS("Successfully preloaded cache"))