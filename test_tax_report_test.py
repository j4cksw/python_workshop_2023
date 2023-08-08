from tax_report import tax_report
from vat_calculator import VatCalculator
from vat_item_factory import VATItemFactory



def test_empty_input():
    assert tax_report([], VATItemFactory((), VatCalculator(7))) == { "items": [], "total_vat": 0 }

def test_one_input():
    assert tax_report([
        { "title": "UFO", "price": 100, "type": set() }
    ], VATItemFactory(set(), VatCalculator(7))) == { "items": [
        { "title": "UFO", "price": 100, "vat": 6.542056074766355 }
    ], "total_vat": 6.542056074766355 }

def test_two_input():
    assert tax_report([
        { "title": "UFO", "price": 100, "type": set() },
        { "title": "UFO", "price": 100, "type": set() },
    ], VATItemFactory(set(), VatCalculator(7))) == { "items": [
        { "title": "UFO", "price": 100, "vat": 6.542056074766355 },
        { "title": "UFO", "price": 100, "vat": 6.542056074766355 },
    ], "total_vat": 13.08411214953271 }

def test_one_input_with_exempted():
    assert tax_report([
        { "title": "Python the hards way", "price": 100, "type": { "book" } },
    ], VATItemFactory({ "book" }, VatCalculator(7))) == { "items": [
        { "title": "Python the hards way", "price": 100, "vat": 0 },
    ], "total_vat": 0 }

def test_two_input_with_one_exempted():
    assert tax_report([
        { "title": "Python the hards way", "price": 100, "type": { "book" } },
        { "title": "UFO", "price": 100, "type": set() },
    ], VATItemFactory({ "book" }, VatCalculator(7))) == { "items": [
        { "title": "Python the hards way", "price": 100, "vat": 0 },
        { "title": "UFO", "price": 100, "vat": 6.542056074766355 },
    ], "total_vat": 6.542056074766355 }