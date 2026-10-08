from django.db import connection


def search_products(term: str):
    sql = f"""
        SELECT
            id,
            name,
            category,
            description
        FROM
            lab_product
        WHERE
            is_public = 1
        AND
            name LIKE '%{term}%'
        ORDER BY
            name
    """

    return _fetch_all(sql)


def find_customer(reference: str):
    sql = f"""
        SELECT
            id,
            reference,
            name,
            email,
            city,
            notes
        FROM
            lab_customer
        WHERE
            reference = '{reference}'
        AND
            is_internal = 0
        LIMIT 20
    """

    return _fetch_all(sql)


def filter_tickets(status: str):
    sql = f"""
        SELECT
            id,
            title,
            status,
            priority,
            body
        FROM
            lab_ticket
        WHERE
            status = '{status}'
        AND
            is_internal = 0
        ORDER BY
            id DESC
    """

    return _fetch_all(sql)


def report_by_region(region: str):
    sql = f"""
        SELECT
            id,
            region,
            product,
            amount,
            details
        FROM
            lab_reportrow
        WHERE
            region = '{region}'
        AND
            is_internal = 0
        ORDER BY
            amount DESC
    """

    return _fetch_all(sql)


def authenticate_legacy(
    username: str,
    password: str,
):
    sql = f"""
        SELECT
            id,
            username,
            role
        FROM
            lab_legacyaccount
        WHERE
            username = '{username}'
        AND
            password = '{password}'
        LIMIT 1
    """

    return _fetch_one(sql)


def search_audit_notes(term: str):
    sql = f"""
        SELECT
            id,
            title,
            content
        FROM
            lab_auditnote
        WHERE
            is_public = 1
        AND
            title LIKE '%{term}%'
        ORDER BY
            id DESC
    """

    return _fetch_all(sql)


def _fetch_all(sql: str):
    with connection.cursor() as cursor:
        cursor.execute(sql)

        columns = [
            column[0]
            for column in cursor.description
        ]

        return [
            dict(
                zip(
                    columns,
                    row,
                )
            )
            for row in cursor.fetchall()
        ]


def _fetch_one(sql: str):
    with connection.cursor() as cursor:
        cursor.execute(sql)

        row = cursor.fetchone()

        if row is None:
            return None

        columns = [
            column[0]
            for column in cursor.description
        ]

        return dict(
            zip(
                columns,
                row,
            )
        )
