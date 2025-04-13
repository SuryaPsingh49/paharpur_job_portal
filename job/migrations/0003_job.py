# Generated by Django 5.0.3 on 2024-04-01 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0002_recruiter"),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("title", models.CharField(max_length=100)),
                ("salary", models.FloatField(max_length=20)),
                ("image", models.FileField(upload_to="")),
                ("description", models.CharField(max_length=300)),
                ("experience", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=150)),
                ("skills", models.CharField(max_length=150)),
                ("creationdate", models.DateField()),
                (
                    "recruiter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="job.recruiter"
                    ),
                ),
            ],
        ),
    ]
