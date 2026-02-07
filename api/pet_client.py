from api.base_client import BaseClient
from config.settings import BASE_URL

class PetClient(BaseClient):

    def __init__(self):
        super().__init__(BASE_URL)

    def add_pet(self, payload):
        return self.post("/pet", json=payload)

    def get_pet(self, pet_id):
        return self.get(f"/pet/{pet_id}")

    def update_pet(self, payload):
        return self.put("/pet", json=payload)

    def delete_pet(self, pet_id):
        return self.delete(f"/pet/{pet_id}")

    def find_by_status(self, status):
        return self.get("/pet/findByStatus", params={"status": status})
