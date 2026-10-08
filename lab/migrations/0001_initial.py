from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AuditNote",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=160)),
                ("content", models.TextField()),
                ("is_public", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("reference", models.CharField(max_length=30, unique=True)),
                ("name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254)),
                ("city", models.CharField(max_length=80)),
                ("notes", models.TextField(blank=True)),
                ("is_internal", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="InventoryItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sku", models.CharField(max_length=40, unique=True)),
                ("name", models.CharField(max_length=120)),
                ("quantity", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="LegacyAccount",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("username", models.CharField(max_length=80, unique=True)),
                ("password", models.CharField(max_length=120)),
                ("role", models.CharField(default="user", max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("category", models.CharField(max_length=80)),
                ("description", models.TextField()),
                ("is_public", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="ReportRow",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("region", models.CharField(max_length=80)),
                ("product", models.CharField(max_length=120)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("details", models.TextField(blank=True)),
                ("is_internal", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=180)),
                ("status", models.CharField(max_length=40)),
                ("priority", models.CharField(max_length=30)),
                ("body", models.TextField()),
                ("is_internal", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="VaultAccount",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("username", models.CharField(max_length=80, unique=True)),
                ("password_hash", models.CharField(max_length=255)),
                ("display_name", models.CharField(max_length=120)),
            ],
        ),
    ]
