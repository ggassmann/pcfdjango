from django.db import models

class Subscription(models.Model):
  SUBSCRIPTION_TYPE_FREE = 0
  SUBSCRIPTION_TYPE_PLUS = 1
  SUBSCRIPTION_TYPE_PRO = 2

  SUBSCRIPTION_TYPE_CHOICES = [
    (SUBSCRIPTION_TYPE_FREE, 'Free'),
    (SUBSCRIPTION_TYPE_PLUS, 'Plus'),
    (SUBSCRIPTION_TYPE_PRO, 'Pro'),
  ]

  name = models.CharField(max_length=250)
  email_address = models.EmailField(max_length=320)
  subscription_type = models.IntegerField(
    default=SUBSCRIPTION_TYPE_FREE,
    choices=SUBSCRIPTION_TYPE_CHOICES
  )