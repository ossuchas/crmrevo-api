from flask_restful import Resource, reqparse
from requests import Response, post
import json


class Customer(Resource):
    @classmethod
    def post(cls):

        url = "https://identity-api-crmrevo.apthai.com/api/Token/ClientLogin"
        payload = {
            "client_id": "crmdigital",
            "client_secret": "pVcySkP6M2QFYvJm5h7fCjSQPoJkUIOmA1OBqZebj4orj8OX6E1U4xViZTu7VBxGKXcvmEiyipm7PO8HQfNPqZGv6v6WTQ"
        }
        headers = {"Content-Type": "application/json"}
        response = post(url, data=json.dumps(payload), headers=headers)
        response_data = response.json()
        access_token = response_data["token"]

        url2 = r"https://xternalproject-api-crmrevo.apthai.com/api/ExternalProject/Equestionnaire/ListCustomer"
        payload = {
            "client_id": "crmdigital",
            "client_secret": "pVcySkP6M2QFYvJm5h7fCjSQPoJkUIOmA1OBqZebj4orj8OX6E1U4xViZTu7VBxGKXcvmEiyipm7PO8HQfNPqZGv6v6WTQ"
        }
        token = f"Bearer {access_token}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": token
        }

        payload = {
            "firstNameTH": "จินตนา",
            "lastNameTH": "อินทะเสย์",
            "email": "",
            "phoneNumber": "",
            "projectNo": "70002",
            "employeeNo": "AP004810"
        }

        response = post(url2, data=json.dumps(payload), headers=headers)
        response_data = response.json()

        return {"status": "Success", "access": access_token, "result": response_data}, 200
