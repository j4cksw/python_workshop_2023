import pytest
from app import app

@pytest.fixture
def setup(request):
    response = app.test_client().delete("/items")
    assert response.status_code == 200
    # response = app.test_client().delete("/whitelist")
    # assert response.status_code == 200


def test_index(setup):
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.get_data() == b"Hello Flask"


def test_empty_vat_report(setup):
    response = app.test_client().put("/vat", json={ "percentage": 7 })
    assert response.status_code == 201

    response = app.test_client().get("/items/report")
    assert response.status_code == 200
    assert response.get_json() == { "items": [], "total_vat": 0 }


def test_one_item_in_vat_report(setup):
    response = app.test_client().put("/items", json={"title": "Python stressed", "type": ["book"], "price": 100 })
    assert response.status_code == 201

    response = app.test_client().get("/items/report")
    assert response.status_code == 200
    assert response.get_json() == { "items": [{"title": "Python stressed", "price": 100, "vat": 6.542056074766355 } ], "total_vat": 6.542056074766355 }


def test_two_items_in_vat_report(setup):
    response = app.test_client().put("/vat", json={ "percentage": 7 })
    assert response.status_code == 201

    response = app.test_client().put("/items", json={"title": "Python stressed", "type": ["book"], "price": 100 })
    assert response.status_code == 201
    response = app.test_client().put("/items", json={"title": "Python stressed", "type": ["book"], "price": 100 })
    assert response.status_code == 201

    response = app.test_client().get("/items/report")
    assert response.status_code == 200
    assert response.get_json() == { "items": [{"title": "Python stressed", "price": 100, "vat": 6.542056074766355 }, {"title": "Python stressed", "price": 100, "vat": 6.542056074766355 } ], "total_vat": 13.08411214953271 }


def test_vat_exempted_item_in_text_report(setup):
    # response = app.test_client().put("/whitelist", json={ "type": "book" })
    # assert response.status_code == 201

    response = app.test_client().put("/items", json={"title": "Python stressed", "type": ["book"], "price": 100 })
    assert response.status_code == 201

    response = app.test_client().get("/items/report")
    assert response.status_code == 200
    assert response.get_json() == { "items": [{"title": "Python stressed", "price": 100, "vat": 0 } ], "total_vat": 0 }


def test_vat_percentage(setup):
    response = app.test_client().put("/vat", json={ "percentage": 10 })
    assert response.status_code == 201

    response = app.test_client().put("/items", json={"title": "Python stressed", "type": ["book"], "price": 100 })
    assert response.status_code == 201

    response = app.test_client().get("/items/report")
    assert response.status_code == 200
    assert response.get_json() == { "items": [{"title": "Python stressed", "price": 100, "vat": 9.090909090909092 } ], "total_vat": 9.090909090909092 }