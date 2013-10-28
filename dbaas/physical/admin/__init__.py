# -*- coding:utf-8 -*-
from django.contrib import admin
from .. import models
from .databaseinfra import DatabaseInfraAdmin
from .engine import EngineAdmin
from .plan import PlanAdmin

admin.site.register(models.DatabaseInfra, DatabaseInfraAdmin)
admin.site.register(models.Engine, EngineAdmin)
admin.site.register(models.Plan, PlanAdmin)
