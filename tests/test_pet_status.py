import allure

@allure.feature("Pet API")
@allure.story("Find by Status")
def test_find_pets_by_status(pet_client, logger):

    resp = pet_client.find_by_status("available")
    assert resp.status_code == 200

    pets = resp.json()
    assert isinstance(pets, list)

    # Validate that at least one pet has status available
    if pets:
        assert pets[0]["status"] == "available"
