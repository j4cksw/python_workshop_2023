def make_item(json_item):
    return {
        "title": json_item["title"],
        "price": json_item["price"],
        "type": set(json_item["type"]) 
    }