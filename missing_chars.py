def missing_chars(full_set: list, existing_chars: list):
    missing_chars = []
    for char in full_set:
        if char not in existing_chars:
            missing_chars.append(char)

    return missing_chars