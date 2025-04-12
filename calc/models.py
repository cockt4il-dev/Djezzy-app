from django.db import models
import uuid


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


class ReportReason(models.Model):
    username = models.TextField()
    type = models.TextField()
    code = models.IntegerField()
    regexp_replace = models.TextField(null=True, blank=True)
    survey_dttm = models.TextField()
    msisdn = models.TextField()



from django.db import models

class NpsSurvey(models.Model):
    day = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    ingestion_dttm = models.DateTimeField(null=True, blank=True)
    msisdn = models.CharField(max_length=50, null=True, blank=True)
    survey_type = models.CharField(max_length=50, null=True, blank=True)
    lang_id = models.CharField(max_length=10, null=True, blank=True)
    question_number = models.IntegerField(null=True, blank=True)
    first_resp = models.TextField(null=True, blank=True)
    last_resp = models.TextField(null=True, blank=True)
    filename = models.CharField(max_length=255, null=True, blank=True)
    invitation_id = models.CharField(max_length=50, null=True, blank=True)
    alert = models.CharField(max_length=50, null=True, blank=True)
    alert_status = models.CharField(max_length=50, null=True, blank=True)
    assigned_role = models.CharField(max_length=50, null=True, blank=True)
    assigned_user = models.CharField(max_length=50, null=True, blank=True)
    cfl_status = models.CharField(max_length=50, null=True, blank=True)
    nps_score = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    file_uuid = models.TextField(null=True, blank=True)
    account_type_desc = models.CharField(max_length=100, null=True, blank=True)
    account_type_key = models.CharField(max_length=50, null=True, blank=True)
    age_group = models.CharField(max_length=50, null=True, blank=True)
    b2b_quota_cluster = models.CharField(max_length=50, null=True, blank=True)
    b2b_quota_segment = models.CharField(max_length=50, null=True, blank=True)
    b2b_segment_type = models.CharField(max_length=50, null=True, blank=True)
    cc_agent_id = models.CharField(max_length=50, null=True, blank=True)
    cc_site_id = models.CharField(max_length=50, null=True, blank=True)
    cc_sitehead_id = models.CharField(max_length=50, null=True, blank=True)
    cc_team_id = models.CharField(max_length=50, null=True, blank=True)
    cc_team_leader_id = models.CharField(max_length=50, null=True, blank=True)
    channel = models.CharField(max_length=50, null=True, blank=True)
    city_id = models.CharField(max_length=50, null=True, blank=True)
    city_name = models.CharField(max_length=100, null=True, blank=True)
    curr_price_plan_desc = models.CharField(max_length=255, null=True, blank=True)
    curr_price_plan_key = models.CharField(max_length=50, null=True, blank=True)
    customer_segment = models.CharField(max_length=100, null=True, blank=True)
    data_arpu_segment = models.CharField(max_length=50, null=True, blank=True)
    handset_brand = models.CharField(max_length=100, null=True, blank=True)
    handset_type = models.CharField(max_length=100, null=True, blank=True)
    join_pos_id = models.CharField(max_length=50, null=True, blank=True)
    join_quota_cluster = models.CharField(max_length=50, null=True, blank=True)
    open_cases_crm = models.CharField(max_length=50, null=True, blank=True)
    pos_type = models.CharField(max_length=50, null=True, blank=True)
    pp_bundle = models.CharField(max_length=50, null=True, blank=True)
    prepaid_ind = models.BooleanField(null=True, blank=True)
    region_id = models.CharField(max_length=50, null=True, blank=True)
    region_name = models.CharField(max_length=100, null=True, blank=True)
    retail_agent_id = models.CharField(max_length=50, null=True, blank=True)
    retail_agent_type = models.CharField(max_length=50, null=True, blank=True)
    retail_pos_id = models.CharField(max_length=50, null=True, blank=True)
    retail_region_name = models.CharField(max_length=100, null=True, blank=True)
    sampling_outcome_reason = models.CharField(max_length=255, null=True, blank=True)
    sampling_outcome_reason_id = models.CharField(max_length=50, null=True, blank=True)
    segment_type = models.CharField(max_length=50, null=True, blank=True)
    sub_region = models.CharField(max_length=100, null=True, blank=True)
    sub_region_id = models.CharField(max_length=50, null=True, blank=True)
    sub_region_name = models.CharField(max_length=100, null=True, blank=True)
    survey_about_product = models.CharField(max_length=50, null=True, blank=True)
    transaction_date = models.DateField(null=True, blank=True)
    transaction_id = models.CharField(max_length=50, null=True, blank=True)
    use_nw_quota_segm = models.CharField(max_length=50, null=True, blank=True)
    use_quota_cluster = models.CharField(max_length=50, null=True, blank=True)
    use_quota_median = models.CharField(max_length=50, null=True, blank=True)
    use_quota_segm = models.CharField(max_length=50, null=True, blank=True)
    visit_date = models.TextField(null=True, blank=True)
    visit_id = models.CharField(max_length=50, null=True, blank=True)
    visit_type1 = models.CharField(max_length=50, null=True, blank=True)
    visit_type2 = models.CharField(max_length=50, null=True, blank=True)
    voice_arpu_segment = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "nps_survey"




class QuestionTypeSummary(models.Model):
    question_type = models.TextField(primary_key=True)
    response_count = models.IntegerField()

    class Meta:
        managed = False  # Don't let Django create/delete this table
        db_table = "question_type_summary"


class MonthlyResponseCounts(models.Model):
    year_month = models.CharField(max_length=7, primary_key=True)  # 'YYYY-MM'
    count = models.IntegerField()

    class Meta:
        managed = False  
        db_table = "monthly_response_counts"  # Matches the SQL view name


class DailyResponseCounts(models.Model):
    response_date = models.DateField(primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False  # Important: This tells Django not to try to manage this materialized view (e.g. no migrations)
        db_table = 'daily_response_counts'



class NPSOverview(models.Model):
    label = models.CharField(max_length=20, primary_key=True)  # Promoters, Passives, Detractors
    percentage = models.FloatField()
    count = models.IntegerField()

    class Meta:
        managed = False  # Django does not manage this table
        db_table = "nps_overview"



class NPSResponseSummary(models.Model):
    response_parsed = models.IntegerField(primary_key=True)  # Now stored as an INTEGER
    response_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "nps_responses_distribution"
        ordering = ["response_parsed"]  # Ensure order at the Django level



class MonthlySurveySummary(models.Model):
    month_year = models.CharField(max_length=7, primary_key=True)  # e.g., "01-2021"
    total = models.BigIntegerField()  # Use BigIntegerField for larger numbers
    active = models.BigIntegerField()  # Use BigIntegerField
    completed = models.BigIntegerField()  # Use BigIntegerField
    stopped = models.BigIntegerField()  # Use BigIntegerField

    class Meta:
        managed = False  # Prevent Django from trying to create or modify this table
        db_table = 'monthly_survey_summary'
        verbose_name = 'Monthly Survey Summary'
        verbose_name_plural = 'Monthly Survey Summaries'


class AvgNpsPerRegion(models.Model):
    sub_region_name = models.CharField(max_length=100)  # Corresponds to character varying(100)
    avg_nps_score = models.DecimalField(max_digits=10, decimal_places=2)  # Corresponds to numeric

    class Meta:
        managed = False  # This tells Django not to create or modify the table
        db_table = 'avg_nps_per_region_test'  # The name of the materialized view
        ordering = ['-avg_nps_score']  # Optional: to order by avg_nps_score DESC by default
