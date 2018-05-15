from django.db import models


class TimeStampedModel(models.Model):
    """Abstract Base Class Model for created_at and last_updated
     at Datetime Fields"""

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# parent model for user
class ImmiUser(TimeStampedModel):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    is_active = models.BooleanField(default=False)
    activation_token_a = models.CharField(max_length=100, blank=False)
    activation_token_b = models.CharField(max_length=100, blank=False)    

    class Meta:
        db_table = 'immi_user'


class service(TimeStampedModel):
    email = models.EmailField(max_length=255, blank=False)
    service_name = models.CharField(max_length=100, blank=False)
    service_request_number = models.CharField(max_length=100, blank=False)
    payment_status = models.BooleanField(default=False)
    action_status = models.BooleanField(default=False)

    class Meta:
        db_table = 'service'


class ImmiDocumentUser(TimeStampedModel):
    name = models.FileField()
    service_request_number = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = 'document_user'


class ImmiDocumentImmi(TimeStampedModel):
    name = models.FileField()
    service_request_number = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = 'immi_immi'

class Transactions(TimeStampedModel):
    email = models.EmailField(max_length=255, blank=False)
    service_request_number = models.CharField(max_length=100, blank=False)
    amount = models.FloatField()

    class Meta:
        db_table = 'transactions'