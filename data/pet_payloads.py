import random

def create_pet_payload(status="available"):
    pet_id = random.randint(100000, 999999)

    return {
        "id": pet_id,
        "category": {"id": 1, "name": "Dogs"},
        "name": f"Dog_{pet_id}",
        "photoUrls": ["https://example.com/dog.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": status
    }
