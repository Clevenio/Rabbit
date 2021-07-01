# Generated by Django 3.2.18 on 2023-03-29 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cluster",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "uuid",
                    models.CharField(db_index=True, max_length=60, verbose_name="uuid"),
                ),
                (
                    "description",
                    models.CharField(max_length=200, verbose_name="Description"),
                ),
                ("info", models.TextField(verbose_name="Info")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Related user",
                    ),
                ),
            ],
            options={
                "db_table": "app_cluster",
            },
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "uuid",
                    models.CharField(db_index=True, max_length=60, verbose_name="uuid"),
                ),
                (
                    "description",
                    models.CharField(max_length=200, verbose_name="Description"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Related user",
                    ),
                ),
            ],
            options={
                "db_table": "app_group",
            },
        ),
        migrations.CreateModel(
            name="Host",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "pending"),
                            ("running", "running"),
                            ("stopped", "stopped"),
                            ("missing", "missing"),
                        ],
                        default="pending",
                        max_length=20,
                        verbose_name="Status",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Name")),
                ("slug", models.CharField(max_length=150, verbose_name="Slug")),
                (
                    "uuid",
                    models.CharField(db_index=True, max_length=60, verbose_name="uuid"),
                ),
                (
                    "cloud_provider",
                    models.CharField(max_length=50, verbose_name="Cloud Provider"),
                ),
                ("specification", models.TextField(verbose_name="Specifications")),
                ("hostname", models.CharField(max_length=100, verbose_name="Hostname")),
                (
                    "remote_id",
                    models.CharField(max_length=100, verbose_name="Remote ID"),
                ),
                ("username", models.CharField(max_length=100, verbose_name="Username")),
                (
                    "ipaddress",
                    models.CharField(max_length=100, verbose_name="IP Address"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "cluster",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.cluster",
                        verbose_name="Related Cluster",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.group",
                        verbose_name="Related Group",
                    ),
                ),
            ],
            options={
                "db_table": "app_host",
            },
        ),
        migrations.CreateModel(
            name="Key",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Name")),
                ("slug", models.CharField(max_length=150, verbose_name="Slug")),
                (
                    "cloud_provider",
                    models.CharField(max_length=50, verbose_name="Cloud Provider"),
                ),
                (
                    "remote_id",
                    models.CharField(max_length=100, verbose_name="Remote ID"),
                ),
                (
                    "uuid",
                    models.CharField(db_index=True, max_length=60, verbose_name="uuid"),
                ),
                ("public_key", models.TextField(verbose_name="Public Key")),
                ("private_key", models.TextField(verbose_name="Private Key")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Related user",
                    ),
                ),
            ],
            options={
                "db_table": "app_key",
            },
        ),
        migrations.CreateModel(
            name="Option",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(db_index=True, max_length=30, verbose_name="Name"),
                ),
                ("value", models.CharField(max_length=200, verbose_name="Value")),
                (
                    "autoload",
                    models.BooleanField(default=False, verbose_name="Autoload"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
            ],
            options={
                "db_table": "app_option",
            },
        ),
        migrations.CreateModel(
            name="ResetRequest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        db_index=True, max_length=60, verbose_name="Email"
                    ),
                ),
                (
                    "token",
                    models.CharField(
                        db_index=True, max_length=200, verbose_name="Token"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("expire_at", models.DateTimeField(verbose_name="Expire at")),
                (
                    "messages_count",
                    models.PositiveSmallIntegerField(verbose_name="Messages Count"),
                ),
            ],
            options={
                "db_table": "app_reset_request",
            },
        ),
        migrations.CreateModel(
            name="UserMeta",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=60, verbose_name="Meta name"
                    ),
                ),
                ("value", models.TextField(verbose_name="Meta Value")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Related User",
                    ),
                ),
            ],
            options={
                "db_table": "app_user_meta",
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.CharField(db_index=True, max_length=60, verbose_name="UUID"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "pending"),
                            ("failed", "failed"),
                            ("succeeded", "succeeded"),
                        ],
                        default="pending",
                        max_length=20,
                        verbose_name="Status",
                    ),
                ),
                ("payload", models.TextField(verbose_name="payload")),
                ("result", models.TextField(verbose_name="Result")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Parent User",
                    ),
                ),
            ],
            options={
                "db_table": "app_task",
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "theme",
                    models.CharField(
                        choices=[("light", "light"), ("dark", "dark")],
                        default="light",
                        max_length=20,
                        verbose_name="Theme",
                    ),
                ),
                (
                    "company",
                    models.CharField(default="", max_length=60, verbose_name="Company"),
                ),
                (
                    "team",
                    models.CharField(default="", max_length=60, verbose_name="Team"),
                ),
                (
                    "job_title",
                    models.CharField(
                        default="", max_length=100, verbose_name="Job Title"
                    ),
                ),
                (
                    "personal_url",
                    models.CharField(
                        default="", max_length=100, verbose_name="Personal URL"
                    ),
                ),
                (
                    "api_key",
                    models.CharField(
                        default="", max_length=100, verbose_name="API Key"
                    ),
                ),
                (
                    "timezone",
                    models.CharField(
                        default="", max_length=50, verbose_name="Timezone"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Related user",
                    ),
                ),
            ],
            options={
                "db_table": "app_profile",
            },
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=200, verbose_name="Content")),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("running", "RUNNING"),
                            ("success", "SUCCESS"),
                            ("failed", "FAILED"),
                        ],
                        default="message",
                        max_length=20,
                        verbose_name="Kind",
                    ),
                ),
                (
                    "delivered",
                    models.BooleanField(default=False, verbose_name="Delivered"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "task",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.task",
                        verbose_name="Related Task",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Related user",
                    ),
                ),
            ],
            options={
                "db_table": "app_notification",
            },
        ),
        migrations.CreateModel(
            name="KeyMeta",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=60, verbose_name="Meta name"
                    ),
                ),
                ("value", models.TextField(verbose_name="Meta Value")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "key",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.key",
                        verbose_name="Related Key",
                    ),
                ),
            ],
            options={
                "db_table": "app_key_meta",
            },
        ),
        migrations.CreateModel(
            name="HostMeta",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=60, verbose_name="Meta name"
                    ),
                ),
                ("value", models.TextField(verbose_name="Meta Value")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "host",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.host",
                        verbose_name="Related Host",
                    ),
                ),
            ],
            options={
                "db_table": "app_host_meta",
            },
        ),
        migrations.AddField(
            model_name="host",
            name="key",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="app.key",
                verbose_name="Related Key",
            ),
        ),
        migrations.AddField(
            model_name="host",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Related user",
            ),
        ),
        migrations.CreateModel(
            name="GroupMeta",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=60, verbose_name="Meta name"
                    ),
                ),
                ("value", models.TextField(verbose_name="Meta Value")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.group",
                        verbose_name="Related Group",
                    ),
                ),
            ],
            options={
                "db_table": "app_group_meta",
            },
        ),
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("activity", models.TextField(verbose_name="Activity")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Related User",
                    ),
                ),
            ],
            options={
                "db_table": "app_activity",
            },
        ),
    ]
