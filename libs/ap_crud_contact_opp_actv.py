from requests import Response, put, post
import json

from config import CRM_GETTOKEN_URL, CRM_CLIENT_ID, CRM_CLIENT_SECRET, CRM_API_PROC


class CRMException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class CRMCreateContactOppAct:

    @classmethod
    def crmsubmit_tran(cls, trns_id: str) -> Response:
        # url = "http://crmrevo-identity-api-crmrevo-test.devops-app.apthai.com/api/Token/ClientLogin"
        # payload = {
        #     "client_id": "crmdigital",
        #     "client_secret": "pVcySkP6M2QFYvJm5h7fCjSQPoJkUIOmA1OBqZebj4orj8OX6E1U4xViZTu7VBxGKXcvmEiyipm7PO8HQfNPqZGv6v6WTQ"
        # }
        # headers = {"Content-Type": "application/json"}
        # response = post(url, data=json.dumps(payload), headers=headers)
        # response_data = response.json()
        # access_token = response_data["token"]
        #
        # token = f"Bearer {access_token}"
        # url = f"http://test-xternalproject-api-crmrevo.apthai.com/api/ExternalProject/EQuestionnaire/MappingContact/{trns_id}"

        url = CRM_GETTOKEN_URL
        payload = {
            "client_id": CRM_CLIENT_ID,
            "client_secret": CRM_CLIENT_SECRET
        }
        headers = {"Content-Type": "application/json"}
        response = post(url, data=json.dumps(payload), headers=headers)
        response_data = response.json()
        access_token = response_data["token"]

        token = f"Bearer {access_token}"
        url = f"{CRM_API_PROC}{trns_id}"

        headers = {
            "Content-Type": "application/json",
            "Authorization": token
        }

        response = put(url=url, data=None, headers=headers)

        if response.status_code != 200:
            raise CRMException("Call API CRM Error Occurred.")

        return response
        # response_data = response.json()
        # return response_data["contact_ref_guid"]
