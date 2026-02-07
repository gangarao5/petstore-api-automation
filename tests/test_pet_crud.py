import allure
from data.pet_payloads import create_pet_payload
from utils.schema_validator import validate_schema

@allure.feature("Pet API")
@allure.story("CRUD Flow")
def test_pet_crud_flow(pet_client, logger, pet_schema):

    logger.info("Creating a new pet")
    payload = create_pet_payload(status="available")

    create_resp = pet_client.add_pet(payload)
    logger.info(f"POST /pet response: {create_resp.status_code}")

    assert create_resp.status_code == 200
    created_pet = create_resp.json()

    # Schema validation
    ok, error = validate_schema(created_pet, pet_schema)
    assert ok, f"Schema validation failed: {error}"

    pet_id = created_pet["id"]

    logger.info(f"Getting pet by id: {pet_id}")
    get_resp = pet_client.get_pet(pet_id)
    assert get_resp.status_code == 200

    logger.info("Updating pet status to sold")
    payload["status"] = "sold"
    update_resp = pet_client.update_pet(payload)
    assert update_resp.status_code == 200

    logger.info("Deleting pet")
    del_resp = pet_client.delete_pet(pet_id)
    assert del_resp.status_code == 200

    logger.info("Verifying pet is deleted")
    verify_resp = pet_client.get_pet(pet_id)
    assert verify_resp.status_code == 404
