from vat_calculator import VatCalculator
from vat_item_factory import VATItemFactory


def tax_report(items, vat_item_factory: VATItemFactory):
    vat_items = [vat_item_factory.make_vat_item(item) for item in items]
    total_vat = sum(vat_item["vat"] for vat_item in vat_items)
    return {
        "items": vat_items,
        "total_vat": total_vat
    }

if __name__ == "__main__":
    report = tax_report([], VATItemFactory({ "book", "otop"}, VatCalculator(7)))
    print("""
    {items}
    total tax: {total_vat: .2f}
          """.format(items=report["items"], total_vat=report["total_vat"]))