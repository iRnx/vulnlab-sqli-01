from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.db import DatabaseError
from django.http import JsonResponse
from django.shortcuts import render

from lab.models import InventoryItem, VaultAccount
from lab.repositories import (
    authenticate_legacy,
    filter_tickets,
    find_customer,
    report_by_region,
    search_audit_notes,
    search_products,
)
from lab.services.flags import LAB_FLAGS, progress, submit_flag


def home(request):
    return render(
        request,
        "lab/home.html",
        {
            "progress": progress(request),
        },
    )


def catalog(request):
    term = request.GET.get(
        "q",
        "",
    )

    rows = []
    error = None

    if term:
        try:
            rows = search_products(term)
        except DatabaseError as exc:
            error = str(exc)

    return render(
        request,
        "lab/catalog.html",
        {
            "term": term,
            "rows": rows,
            "error": error,
        },
    )


def customer_lookup(request):
    reference = request.GET.get(
        "reference",
        "",
    )

    rows = []
    error = None

    if reference:
        try:
            rows = find_customer(reference)
        except DatabaseError as exc:
            error = str(exc)

    return render(
        request,
        "lab/customer_lookup.html",
        {
            "reference": reference,
            "rows": rows,
            "error": error,
        },
    )


def tickets(request):
    status = request.GET.get(
        "status",
        "",
    )

    rows = []
    error = None

    if status:
        try:
            rows = filter_tickets(status)
        except DatabaseError as exc:
            error = str(exc)

    return render(
        request,
        "lab/tickets.html",
        {
            "status": status,
            "rows": rows,
            "error": error,
        },
    )


def reports(request):
    region = request.GET.get(
        "region",
        "",
    )

    rows = []
    error = None

    if region:
        try:
            rows = report_by_region(region)
        except DatabaseError as exc:
            error = str(exc)

    return render(
        request,
        "lab/reports.html",
        {
            "region": region,
            "rows": rows,
            "error": error,
        },
    )


def legacy_login(request):
    account = None
    error = None

    if request.method == "POST":
        username = request.POST.get(
            "username",
            "",
        )

        password = request.POST.get(
            "password",
            "",
        )

        try:
            account = authenticate_legacy(
                username=username,
                password=password,
            )
        except DatabaseError as exc:
            error = str(exc)

    flag = None

    if (
        account
        and account.get("role") == "admin"
    ):
        flag = LAB_FLAGS["stage05"]

    return render(
        request,
        "lab/legacy_login.html",
        {
            "account": account,
            "flag": flag,
            "error": error,
        },
    )


def audit_notes(request):
    term = request.GET.get(
        "q",
        "",
    )

    rows = []
    error = None

    if term:
        try:
            rows = search_audit_notes(term)
        except DatabaseError as exc:
            error = str(exc)

    return render(
        request,
        "lab/audit_notes.html",
        {
            "term": term,
            "rows": rows,
            "error": error,
        },
    )


def vault_login(request):
    authenticated = False

    if request.method == "POST":
        username = request.POST.get(
            "username",
            "",
        )

        password = request.POST.get(
            "password",
            "",
        )

        account = (
            VaultAccount.objects
            .filter(
                username=username,
            )
            .first()
        )

        if (
            account
            and check_password(
                password,
                account.password_hash,
            )
        ):
            authenticated = True

    return render(
        request,
        "lab/vault_login.html",
        {
            "authenticated": authenticated,
            "flag": (
                LAB_FLAGS["stage06"]
                if authenticated
                else None
            ),
        },
    )


def inventory(request):
    term = request.GET.get(
        "q",
        "",
    )

    items = (
        InventoryItem.objects
        .all()
        .order_by("name")
    )

    if term:
        items = items.filter(
            name__icontains=term,
        )

    return render(
        request,
        "lab/inventory.html",
        {
            "term": term,
            "items": items,
        },
    )


def submit_flag_view(request):
    if request.method == "POST":
        value = request.POST.get(
            "flag",
            "",
        )

        accepted, stage = submit_flag(
            request,
            value,
        )

        if accepted:
            messages.success(
                request,
                f"Flag aceita. Etapa {int(stage[-2:])} concluída.",
            )
        else:
            messages.error(
                request,
                "Flag inválida.",
            )

    return render(
        request,
        "lab/progress.html",
        {
            "progress": progress(request),
        },
    )


def lab_status_api(request):
    return JsonResponse(
        progress(request)
    )
