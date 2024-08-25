# Generated by Django 5.0.3 on 2024-08-25 13:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Grade",
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
                ("grade_number", models.IntegerField()),
                (
                    "term",
                    models.CharField(
                        choices=[("1", "Term 1"), ("2", "Term 2")], max_length=1
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subjects",
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
                ("subject_name", models.CharField(max_length=15)),
                (
                    "grade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UserProfile.grade",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Userprofile",
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
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("STUDENT", "Student"),
                            ("TEACHER", "Teacher"),
                            ("ADMIN", "Admin"),
                        ],
                        max_length=10,
                    ),
                ),
                ("admission_date", models.DateTimeField(auto_now_add=True)),
                (
                    "grade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UserProfile.grade",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Video",
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
                ("title", models.CharField(max_length=50)),
                ("video_file", models.FileField(upload_to="videos/")),
                ("description", models.TextField(blank=True, null=True)),
                ("upload_date", models.DateTimeField(auto_now_add=True)),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UserProfile.subjects",
                    ),
                ),
            ],
        ),
    ]