import json
from django.core.management.base import BaseCommand
from insights.models import Insight
from datetime import datetime


class Command(BaseCommand):
    help = "Import JSON data into the database"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str, help="Path to JSON file")

    def handle(self, *args, **kwargs):
        json_file_path = kwargs["json_file"]
        with open(json_file_path, "r", encoding="utf-8") as file:
            insights_data = json.load(file)

        for insight_data in insights_data:
            # Replace empty strings with None
            for key, value in insight_data.items():
                if value == "":
                    insight_data[key] = None

            # Convert 'added' and 'published' to datetime objects
            added = (
                datetime.strptime(insight_data["added"], "%B, %d %Y %H:%M:%S")
                if insight_data["added"] is not None
                else None
            )
            published = (
                datetime.strptime(insight_data["published"], "%B, %d %Y %H:%M:%S")
                if insight_data["published"] is not None
                else None
            )

            Insight.objects.create(
                end_year=insight_data.get("end_year"),
                intensity=insight_data["intensity"],
                sector=insight_data.get("sector"),
                topic=insight_data.get("topic"),
                insight=insight_data.get("insight"),
                url=insight_data.get("url"),
                region=insight_data.get("region"),
                start_year=insight_data.get("start_year"),
                impact=insight_data.get("impact"),
                added=added,
                published=published,
                country=insight_data.get("country"),
                relevance=insight_data.get("relevance"),
                pestle=insight_data.get("pestle"),
                source=insight_data.get("source"),
                title=insight_data.get("title"),
                likelihood=insight_data.get("likelihood"),
            )
        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
