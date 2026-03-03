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


def filter_by_email(users, email):
    """
    Return a list of users whose email matches the given email string.
    """
    if not email:
        return users

    filtered = []
    for user in users:
        if user.get("email") == email:
            filtered.append(user)
    return filtered


def filter_users(users, username=None, country=None, email=None,
                 min_age=None, max_age=None):
    """
    Apply all available filters to the users list.
    """
    filtered = users

    if username:
        filtered = filter_by_username(filtered, username)
    if country:
        filtered = filter_by_country(filtered, country)
    if min_age is not None or max_age is not None:
        filtered = filter_by_age(filtered, min_age=min_age, max_age=max_age)
    if email:
        filtered = filter_by_email(filtered, email)

    return filtered
