from django.contrib import admin

# Register your models here.
from .models import User, UserManager, Contact, Sponsor, Participant, ClinicalTrial, Criteria, Categories, ClinicalTrialCriteriaResponse, QuestionSchema

admin.site.register(Sponsor)
admin.site.register(Participant)
admin.site.register(ClinicalTrial)
admin.site.register(Criteria)
admin.site.register(Categories)
admin.site.register(ClinicalTrialCriteriaResponse)
admin.site.register(QuestionSchema)