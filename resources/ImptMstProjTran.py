import traceback
from flask_restful import Resource, reqparse
from flask import request
from datetime import datetime
from flask_jwt_extended import (
    jwt_required,
    get_raw_jwt
)
from blacklist import BLACKLIST


from models.ImptMstProjTran import ImptMstProjTranModel
from schemas.ImptMstProjTran import ImptMstProjTranModelSchema

logs_schema = ImptMstProjTranModelSchema()
logs_list_schema = ImptMstProjTranModelSchema(many=True)


class ImptMstProjTran(Resource):
    @classmethod
    def get(cls, guid: str):
        objs = ImptMstProjTranModel.find_by_ref_id(guid)
        if objs:
            return logs_schema.dump(objs), 200

        return {"message": "No Data Found"}, 404
