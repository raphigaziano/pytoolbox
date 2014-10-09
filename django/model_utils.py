# Grabbed and slightly adapted from
# https://bitbucket.org/tominardi/huron/   (utils.model_utils).
def field_has_changed(instance, field, manager='objects'):
    """
    Returns true if a field has changed in a model

    May be used in a model.save() method.

    """

    if not instance.pk:
        return True
    manager = getattr(instance.__class__, manager)
    old = getattr(manager.get(pk=instance.pk), field)
    return not getattr(instance, field) == old
