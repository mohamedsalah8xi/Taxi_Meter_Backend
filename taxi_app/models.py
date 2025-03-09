from django.db import models

class Trip(models.Model):
    start_location = models.CharField(max_length=255)  # نقطة البداية
    end_location = models.CharField(max_length=255)  # نقطة النهاية
    distance = models.FloatField()  # المسافة بالكيلومترات
    fare = models.DecimalField(max_digits=10, decimal_places=2)  # تكلفة الرحلة
    start_time = models.DateTimeField(auto_now_add=True)  # وقت بدء الرحلة
    end_time = models.DateTimeField(null=True, blank=True)  # وقت انتهاء الرحلة
    
    def _str_(self):
        return f"Trip from {self.start_location} to {self.end_location}"