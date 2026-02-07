import allure

@allure.feature("Pet API")
@allure.story("Negative Tests")
def test_get_pet_invalid_id(pet_client):
    resp = pet_client.get_pet(0)
    assert resp.status_code in [400, 404]

def test_delete_pet_invalid_id(pet_client):
    resp = pet_client.delete_pet(0)
    assert resp.status_code in [400, 404]
