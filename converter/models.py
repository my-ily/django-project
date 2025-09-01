# converter/models.py
from django.db import models

class ConversaionHistory(models.Model):
    amount = models.FloatField()
    from_currancy = models.CharField(max_length=10)
    to_currancy = models.CharField(max_length=10)
    converted_amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} {self.from_currancy} -> {self.to_currancy}"
