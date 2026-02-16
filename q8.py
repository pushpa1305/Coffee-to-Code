def sanitize_email(raw_input: str) -> str:
    clean_email = raw_input.strip().lower()
    if clean_email.count('@') == 1:
        return clean_email
    else:
        return "Invalid Email"
