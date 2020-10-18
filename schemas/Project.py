from ma import ma
from models.Project import ProjectModel


class ProjectSchema(ma.ModelSchema):
    class Meta:
        model = ProjectModel
