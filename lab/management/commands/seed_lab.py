from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.core.management.base import BaseCommand

from lab.models import (
    AuditNote,
    Customer,
    InventoryItem,
    LegacyAccount,
    Product,
    ReportRow,
    Ticket,
    VaultAccount,
)
from lab.services.flags import LAB_FLAGS


class Command(BaseCommand):
    help = "Recria os dados do VulnLab SQL Injection 01."

    def handle(self, *args, **options):
        models = [
            Product,
            Customer,
            Ticket,
            ReportRow,
            LegacyAccount,
            AuditNote,
            VaultAccount,
            InventoryItem,
        ]

        for model in models:
            model.objects.all().delete()

        self._seed_products()
        self._seed_customers()
        self._seed_tickets()
        self._seed_reports()
        self._seed_legacy_accounts()
        self._seed_audit_notes()
        self._seed_vault()
        self._seed_inventory()

        self.stdout.write(
            self.style.SUCCESS(
                "VulnLab resetado e populado."
            )
        )

    def _seed_products(self):
        Product.objects.bulk_create(
            [
                Product(
                    name="OrbitBook 14",
                    category="Notebook",
                    description="Notebook corporativo de 14 polegadas.",
                    is_public=True,
                ),
                Product(
                    name="OrbitDock USB-C",
                    category="Acessórios",
                    description="Dock USB-C para estações de trabalho.",
                    is_public=True,
                ),
                Product(
                    name="OrbitCam Pro",
                    category="Vídeo",
                    description="Webcam para videoconferência.",
                    is_public=True,
                ),
                Product(
                    name="Internal Recovery Kit",
                    category="Internal",
                    description=LAB_FLAGS["stage01"],
                    is_public=False,
                ),
            ]
        )

    def _seed_customers(self):
        Customer.objects.bulk_create(
            [
                Customer(
                    reference="CUST-1001",
                    name="Aurora Sistemas",
                    email="contato@aurora.local",
                    city="São Paulo",
                    notes="Cliente empresarial ativo.",
                    is_internal=False,
                ),
                Customer(
                    reference="CUST-1002",
                    name="Brisa Digital",
                    email="contato@brisa.local",
                    city="Campinas",
                    notes="Plano profissional.",
                    is_internal=False,
                ),
                Customer(
                    reference="INT-9001",
                    name="Internal Audit",
                    email="audit@internal.local",
                    city="Internal",
                    notes=LAB_FLAGS["stage02"],
                    is_internal=True,
                ),
            ]
        )

    def _seed_tickets(self):
        Ticket.objects.bulk_create(
            [
                Ticket(
                    title="Falha no login",
                    status="open",
                    priority="high",
                    body="Usuário não consegue concluir autenticação.",
                    is_internal=False,
                ),
                Ticket(
                    title="Atualização cadastral",
                    status="closed",
                    priority="low",
                    body="Dados atualizados com sucesso.",
                    is_internal=False,
                ),
                Ticket(
                    title="Internal security note",
                    status="internal",
                    priority="critical",
                    body=LAB_FLAGS["stage03"],
                    is_internal=True,
                ),
            ]
        )

    def _seed_reports(self):
        ReportRow.objects.bulk_create(
            [
                ReportRow(
                    region="sudeste",
                    product="OrbitBook 14",
                    amount="14990.00",
                    details="Relatório público.",
                    is_internal=False,
                ),
                ReportRow(
                    region="sul",
                    product="OrbitCam Pro",
                    amount="7290.00",
                    details="Relatório público.",
                    is_internal=False,
                ),
                ReportRow(
                    region="internal",
                    product="Security Review",
                    amount="0.00",
                    details=LAB_FLAGS["stage04"],
                    is_internal=True,
                ),
            ]
        )

    def _seed_legacy_accounts(self):
        LegacyAccount.objects.bulk_create(
            [
                LegacyAccount(
                    username="guest",
                    password="guest123",
                    role="user",
                ),
                LegacyAccount(
                    username="operator",
                    password="operator2026",
                    role="user",
                ),
                LegacyAccount(
                    username="legacy_admin",
                    password="not-listed-here",
                    role="admin",
                ),
            ]
        )

    def _seed_audit_notes(self):
        AuditNote.objects.bulk_create(
            [
                AuditNote(
                    title="Rotina de backup",
                    content="Backups locais verificados.",
                    is_public=True,
                ),
                AuditNote(
                    title="Inventário trimestral",
                    content="Inventário concluído.",
                    is_public=True,
                ),
                AuditNote(
                    title="Security migration",
                    content="Contas administrativas foram migradas para o cofre.",
                    is_public=True,
                ),
            ]
        )

    def _seed_vault(self):
        hasher = PBKDF2PasswordHasher()

        password_hash = hasher.encode(
            password="dragon",
            salt="VulnLabStage06Salt",
            iterations=100_000,
        )

        VaultAccount.objects.create(
            username="archive_admin",
            password_hash=password_hash,
            display_name="Archive Administrator",
        )

    def _seed_inventory(self):
        InventoryItem.objects.bulk_create(
            [
                InventoryItem(
                    sku="INV-001",
                    name="OrbitBook 14",
                    quantity=12,
                ),
                InventoryItem(
                    sku="INV-002",
                    name="OrbitDock USB-C",
                    quantity=29,
                ),
                InventoryItem(
                    sku="INV-003",
                    name="OrbitCam Pro",
                    quantity=18,
                ),
            ]
        )
