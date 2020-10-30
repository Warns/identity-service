from social_core.exceptions import AuthException


# This implementation is based on python-social-auth's `associate_by_email`:
# https://github.com/python-social-auth/social-core/blob/master/social_core/pipeline/social_auth.py#L51
def associate_by_user_id(backend, details, user=None, *args, **kwargs):
    """
    If `user_id` exists in the strategy session, the social platform account
    is attached to the Django account denoted with this `user_id` value.
    """
    if user:
        return None

    user_id = backend.strategy.session_get('user_id')
    if user_id:
        user = backend.strategy.storage.user.get_user(pk=user_id)
        if user:
            return {'user': user, 'is_new': False}

    return None


def check_user_allowed(strategy, backend, details, *args, **kwargs):
    """
    Check if a social platform account is being attached to a Django account.
    If it is, the Django account must be active in order to continue.
    """
    user_id = strategy.session_get('user_id')

    if not user_id:
        return None

    user = backend.strategy.storage.user.get_user(pk=user_id)
    if user is None:
        raise AuthException(backend, 'Account not found')
    if not user.is_active:
        raise AuthException(backend, 'Account is not activated')
