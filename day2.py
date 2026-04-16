from typing import Any


def calculate_discount(price: float, discount_percent: int) -> float | None:
    if discount_percent < 0 or discount_percent > 100:
        return None
    return price - (price * discount_percent / 100)


def get_most_expensive(products: list[dict[str, Any]]) -> dict[str, Any] | None:
    if not products:
        return None
    return max(products, key=lambda p: p["price"])


def filter_by_category(
    products: list[dict[str, Any]], category: str
) -> list[dict[str, Any]]:
    return [p for p in products if p["category"] == category]


def summarize_cart(items: list[dict[str, Any]]) -> dict[str, Any]:
    total = 0
    names = []
    for item in items:
        total += item["price"] * item["quantity"]
        names.append(item["name"])
    return {"total": total, "items": names, "count": len(items)}


# Test it
products = [
    {"name": "Laptop", "price": 1200.0, "category": "electronics"},
    {"name": "Phone", "price": 800.0, "category": "electronics"},
    {"name": "Desk", "price": 350.0, "category": "furniture"},
]

cart = [
    {"name": "Laptop", "price": 1200.0, "quantity": 1},
    {"name": "Phone", "price": 800.0, "quantity": 2},
]

print(calculate_discount(1200.0, 15))
print(get_most_expensive(products))
print(filter_by_category(products, "electronics"))
print(summarize_cart(cart))
