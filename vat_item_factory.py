class VATItemFactory():

    def __init__(self, whitelist, vat_calculator) -> None:
        self._whitelist = whitelist
        self._vat_calculator = vat_calculator
    
    def make_vat_item(self, item):
        return {
            "title": item["title"],
            "price": item["price"],
            "vat": 0 if self._whitelist.intersection(item["type"]) 
                else self._vat_calculator.exclude(item["price"])
        }