from flask import Flask, request
from item import make_item
from tax_report import tax_report
from vat_calculator import VatCalculator
from vat_item_factory import VATItemFactory

app = Flask(__name__)

item_list = []
whitelist = { "book", "stationary", "otop" }
vat_table = [ { "percentage": 7 } ]


@app.route("/")
def index():
    return "Hello Flask"


@app.route("/items/report")
def get_vat_report():
    return tax_report(item_list, VATItemFactory(whitelist, VatCalculator(vat_table[-1]["percentage"])))


@app.route("/items", methods=["PUT", "DELETE"])
def items():
    global item_list
    if request.method == "PUT":
        item_list.append(make_item(request.json))
        return "", 201
    
    item_list = []
    return "", 200


@app.route("/whitelist", methods=["PUT", "DELETE"])
def whitelist_resource():
    global whitelist
    if request.method == "PUT":
        whitelist.add(request.json["type"])
        return "", 201
    
    whitelist = set()
    return "", 200

@app.route("/vat", methods=["PUT", "DELETE"])
def vat_resource():
    global vat_table
    if request.method == "PUT":
        vat_table.append({ "percentage": request.json["percentage"] })
        return "", 201
    vat_table = []
    return "", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)