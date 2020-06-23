from django.db import models

class Poll(models.Model):
    question = models.TextField();
    option_one = models.CharField(max_length = 30)
    option_two = models.CharField(max_length = 30)
    option_three = models.CharField(max_length = 30)
    option1_count = models.IntegerField(default = 0)
    option2_count = models.IntegerField(default = 0)
    option3_count = models.IntegerField(default = 0)

    def total(self):
        return self.option1_count + self.option2_count + self.option3_count