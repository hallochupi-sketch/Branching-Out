def filter_by_age(users, min_age=None, max_age=None):
    """
    Return users whose age is within the given bounds.
    If only min_age is given, filter users with age >= min_age.
    If only max_age is given, filter users with age <= max_age.
    If both are given, filter min_age <= age <= max_age.
    """
    if min_age is not None and max_age is not None:
        return [u for u in users if min_age <= u.get("age", 0) <= max_age]
    elif min_age is not None:
        return [u for u in users if u.get("age", 0) >= min_age]
    elif max_age is not None:
        return [u for u in users if u.get("age", 0) <= max_age]
    else:
        return users
