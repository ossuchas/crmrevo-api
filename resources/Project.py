from flask_restful import Resource


from models.Project import ProjectModel
from schemas.Project import ProjectSchema

proj_schema = ProjectSchema()
proj_list_schema = ProjectSchema(many=True)


class Project(Resource):
    @classmethod
    def get(cls, guid: str):
        objs = ProjectModel.find_by_ref_id(guid)
        if objs:
            return proj_schema.dump(objs), 200

        return {"message": "No Data Found"}, 404

