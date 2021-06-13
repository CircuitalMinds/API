from . import register, models

register_manager = register.Manager()
register_manager.select_model = models.select_model

