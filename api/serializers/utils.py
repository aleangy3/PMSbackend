def get_currently_with(history):
    if not len(history) > 0:
        return None
    for hist in history:
        if hist.is_retain:
            return get_user_data(hist.marked_to)

    return None


def get_user_data(user):
    if not user:
        return None
    data = {
        "id": user.id,
        "username": user.username,
        "name": user.name,
        "role": user.role.code_name if user.role else None,
        "role_id": user.role.id if user.role else None,
    }
    return data
