class VatCalculator():
    
    def __init__(self, percentage):
        self._percentage = percentage
    
    def exclude(self, price):
        return price * self._percentage/(100 + self._percentage)