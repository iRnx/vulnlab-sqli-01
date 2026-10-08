LAB_FLAGS = {
    "stage01": "flag{sql01_catalog_boundary}",
    "stage02": "flag{sql01_customer_scope}",
    "stage03": "flag{sql01_ticket_filter}",
    "stage04": "flag{sql01_report_filter}",
    "stage05": "flag{sql01_legacy_auth}",
    "stage06": "flag{sql01_hash_chain}",
}


def submit_flag(request, value: str) -> tuple[bool, str | None]:
    value = value.strip()

    matched_stage = None

    for stage, expected in LAB_FLAGS.items():
        if value == expected:
            matched_stage = stage
            break

    if matched_stage is None:
        return False, None

    solved = set(
        request.session.get(
            "solved_flags",
            [],
        )
    )

    solved.add(matched_stage)

    request.session["solved_flags"] = sorted(
        solved
    )

    return True, matched_stage


def progress(request) -> dict[str, object]:
    solved = set(
        request.session.get(
            "solved_flags",
            [],
        )
    )

    stages = []

    for number in range(1, 7):
        key = f"stage{number:02d}"

        stages.append(
            {
                "number": number,
                "solved": key in solved,
            }
        )

    return {
        "solved_count": len(solved),
        "total": len(LAB_FLAGS),
        "stages": stages,
    }
