from django.db import models


class NPSSurveytypes(models.Model):
    survey_type = models.IntegerField(primary_key=True)
    survey_name = models.TextField()


class NPSQuestions(models.Model):  # Use PascalCase for model names
    survey_type = models.ForeignKey(
        NPSSurveytypes,
        on_delete=models.CASCADE,
        db_column='survey_type'
    )
    lang_id = models.TextField()
    question_number = models.IntegerField()
    regexp_replace = models.TextField()
    question_name = models.TextField()
    question_type = models.TextField()
    
    
    def __str__(self):
        return f"Survey Type: {self.survey_type}"
    
class NPSResponses(models.Model):
    survey_dttm = models.TextField()
    msisdn = models.TextField()
    response_dttm = models.TextField()
    question_number = models.IntegerField()
    question_name = models.TextField()
    question_type = models.TextField()
    response_raw = models.TextField()
    response_parsed = models.TextField()


# Create your models here.

