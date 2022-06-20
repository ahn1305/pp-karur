from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SAttendanceConfig(AppConfig):
    name = 's_attendance'
    verbose_name = _("Staff Attendance")
