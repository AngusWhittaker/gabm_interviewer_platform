import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gabm_infra.settings")
django.setup()

from pages.models import StudySetting
from sim_brain.models import Expert

# Load default settings
StudySetting.load()

# Load default experts
behavioural_economist = Expert()
behavioural_economist.name = "Behavioural Economist"
behavioural_economist.prompt = "Imagine you are an expert behavioural economist (with a PhD) taking notes while observing this interview. Write observations/reflections about the interviewee's economic behaviour, decision-making patterns, and socio-cognitive tendencies. (You should make more than 5 observations and fewer than 20. Choose the number that makes sense given the depth of the interview content above.)"
behavioural_economist.save()

demographer = Expert()
demographer.name = "Demographer"
demographer.prompt = "Imagine you are an expert demographer (with a PhD) taking notes while observing this interview. Write observations/reflections about the interviewee's demographic traits and social status. (You should make more than 5 observations and fewer than 20. Choose the number that makes sense given the depth of the interview content above.)"
demographer.save()

political_scientist = Expert()
political_scientist.name = "Political Scientist"
political_scientist.prompt = "Imagine you are an expert political scientist (with a PhD) taking notes while observing this interview. Write observations/reflections about the interviewee's political behaviour, affiliations and social socio-political identity. (You should make more than 5 observations and fewer than 20. Choose the number that makes sense given the depth of the interview content above.)"
political_scientist.save()

psychologist = Expert()
psychologist.name = "Psychologist"
psychologist.prompt = "Imagine you are an expert psychologist (with a PhD) taking notes while observing this interview. Write observations/reflections about the interviewee's psychological traits, emotional state, cognitive patterns and interpersonal dynamics. (You should make more than 5 observations and fewer than 20. Choose the number that makes sense given the depth of the interview content above.)"
psychologist.save()