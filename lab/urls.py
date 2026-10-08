from django.urls import path

from lab import views


app_name = "lab"

urlpatterns = [
    path("", views.home, name="home"),
    path("catalog/", views.catalog, name="catalog"),
    path("customers/", views.customer_lookup, name="customers"),
    path("tickets/", views.tickets, name="tickets"),
    path("reports/", views.reports, name="reports"),
    path("legacy-login/", views.legacy_login, name="legacy_login"),
    path("audit/", views.audit_notes, name="audit_notes"),
    path("vault-login/", views.vault_login, name="vault_login"),
    path("inventory/", views.inventory, name="inventory"),
    path("progress/", views.submit_flag_view, name="progress"),
    path("api/status/", views.lab_status_api, name="lab_status_api"),
]
