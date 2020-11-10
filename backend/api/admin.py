from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportMixin, ImportMixin, ExportActionModelAdmin, ImportExportActionModelAdmin
from .models import Va
from .models import Intent
from .models import Svp
from .models import Project
from .models import Transition
from response.models import ResponseTemplate
from response.models import ResponseValue

# Register your models here.
admin.site.register(Va, ImportExportModelAdmin)
admin.site.register(Intent, ImportExportModelAdmin)
admin.site.register(Svp, ImportExportModelAdmin)
admin.site.register(Project, ImportExportModelAdmin)
admin.site.register(Transition, ImportExportModelAdmin)
admin.site.register(ResponseTemplate, ImportExportModelAdmin)
admin.site.register(ResponseValue, ImportExportModelAdmin)

