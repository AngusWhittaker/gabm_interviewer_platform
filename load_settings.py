import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gabm_infra.settings")
django.setup()

from pages.models import StudySetting

StudySetting.load()