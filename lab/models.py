from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=80)
    description = models.TextField()
    is_public = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Customer(models.Model):
    reference = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    city = models.CharField(max_length=80)
    notes = models.TextField(blank=True)
    is_internal = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.reference} - {self.name}"


class Ticket(models.Model):
    title = models.CharField(max_length=180)
    status = models.CharField(max_length=40)
    priority = models.CharField(max_length=30)
    body = models.TextField()
    is_internal = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class ReportRow(models.Model):
    region = models.CharField(max_length=80)
    product = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField(blank=True)
    is_internal = models.BooleanField(default=False)


class LegacyAccount(models.Model):
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=120)
    role = models.CharField(max_length=40, default="user")

    def __str__(self) -> str:
        return self.username


class AuditNote(models.Model):
    title = models.CharField(max_length=160)
    content = models.TextField()
    is_public = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class VaultAccount(models.Model):
    username = models.CharField(max_length=80, unique=True)
    password_hash = models.CharField(max_length=255)
    display_name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.username


class InventoryItem(models.Model):
    sku = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=120)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name
