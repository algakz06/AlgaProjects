import requests

from app.config import log

notion_url = "https://api.notion.com/v1/databases/"


class Notion:
    base_url = "https://api.notion.com/v1"
    headers = {
        "Authorization": "Bearer ",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }

    def _build_headers(self, access_token: str):
        """
        Build headers with access token
        """
        headers = self.headers
        headers["Authorization"] = "Bearer " + access_token

        return headers

    def check_token(self, access_token: str) -> bool:
        """
        using method get all users for checking is token valid
        """
        url = self.base_url + "/users"
        headers = self._build_headers(access_token)

        response = requests.get(url, headers=headers)

        if response.status_code in [200, 403]:
            """
            200 - token is valid
            we use 403 status code, cause it shows that token is valid,\
            but user didnt promote access to this method
            """
            return True
        else:
            log.info(f"Token {access_token} is not valid")
            log.debug(f"Response: {response.json()}")
            return False

    def add_page_to_db(self, db_id: str, access_token: str, page_name: str):
        """
        add page to database view in Notion
        """
        url = self.base_url + "/pages"
        headers = self._build_headers(access_token)
        payload = {
            "parent": {"database_id": db_id},
            "properties": {
                "Name": {
                    "title": [
                        {
                            "text": {"content": page_name},
                        }
                    ]
                }
            },
        }

        response = requests.post(url, headers, json=payload)

        if response.status_code == 200:
            return ...
        else:
            return ...

    def get_db_data(self, db_id: str, access_token: str):
        """
        get db data from Notion

        may be used to check is user_data correct
        """
        url = f"{self.base_url}/databases/{db_id}/query"
        headers = self._build_headers(access_token)

        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            return ...
        else:
            return ...
