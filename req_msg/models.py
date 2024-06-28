from django.db import models

class WaterHumidity(models.Model):
    humidity = models.FloatField() #para armazenar o valor da umidade da água.
    timestamp = models.DateTimeField(auto_now_add=True) #que armazena os dados e a hora em que a leitura foi registrada automaticamente

    def __str__(self):
        return f'Humidity: {self.humidity}%, Timestamp: {self.timestamp}'