from db import db
from typing import List
import uuid
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class ProjectModel(db.Model):
    __tablename__ = "Project"
    __table_args__ = {"schema": "PRJ"}

    ID = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    Created = db.Column(db.DateTime)
    Updated = db.Column(db.DateTime)
    CreatedByUserID = db.Column(UUID(as_uuid=True))
    UpdatedByUserID = db.Column(UUID(as_uuid=True))
    IsDeleted = db.Column(db.Boolean)
    ProjectNo = db.Column(db.String(50))
    ProjectNameTH = db.Column(db.String(100))
    IsActive = db.Column(db.Boolean)

    @classmethod
    def find_by_id(cls, _id: str) -> "ProjectModel":
        return cls.query.filter_by(ID=_id, isDelelted=False, isActive=True).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
