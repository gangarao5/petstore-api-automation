import json
import pytest
from api.pet_client import PetClient
from utils.logger import get_logger

@pytest.fixture(scope="session")
def logger():
    return get_logger()

@pytest.fixture(scope="session")
def pet_client():
    return PetClient()

@pytest.fixture(scope="session")
def pet_schema():
    with open("schemas/pet_schema.json") as f:
        return json.load(f)
