from django.contrib import admin

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


admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Ticket)
admin.site.register(ReportRow)
admin.site.register(LegacyAccount)
admin.site.register(AuditNote)
admin.site.register(VaultAccount)
admin.site.register(InventoryItem)
