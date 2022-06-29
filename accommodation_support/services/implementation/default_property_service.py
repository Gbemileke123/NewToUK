import uuid

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from NewToUk.shared.models.BaseResponse import BaseResponse
from accommodation_support.dto.property_dto import EditDto, CreateDto, CreatePropertyResponseModel, \
    GetPropertyResponseModel, ListPropertyResponseModel, EditPropertyResponseModel
from accommodation_support.repositories.interface.property_repository import PropertyRepository
from accommodation_support.services.interface.property_service import PropertyService


class DefaultPropertyService(PropertyService):
    repository: PropertyRepository

    def __init__(self, repository):
        self.repository = repository

    def create(self, model: CreateDto) -> CreatePropertyResponseModel | BaseResponse:
        try:
            result = self.repository.create(model)
            if result:
                return CreatePropertyResponseModel(
                    status=True,
                    message="Property Created Successfully",
                    property_id=result
                )
            else:
                return CreatePropertyResponseModel(
                    status=False,
                    message="Property Created Unsuccessfully",
                    property_id=None
                )
        except (Exception, ObjectDoesNotExist, MultipleObjectsReturned) as ex:
            return BaseResponse(
                status=False,
                message="An error occurred while creating property",
            )

    def search(self, filter: str) -> ListPropertyResponseModel | BaseResponse:
        try:
            result = self.repository.search(filter)
            if result:
                return ListPropertyResponseModel(
                    status=True,
                    message="Successful",
                    properties=result
                )
            else:
                return ListPropertyResponseModel(
                    status=True,
                    message="Unsuccessful",
                    properties=[]
                )
        except (Exception,):
            return BaseResponse(
                status=True,
                message="An error occurred",
            )

    def edit(self, id: uuid.UUID, model: EditDto) -> EditPropertyResponseModel | BaseResponse:
        try:
            result = self.repository.edit(id, model)
            if result:
                return EditPropertyResponseModel(
                    status=True,
                    message="Successful",
                    property_id=result
                )
            else:
                return EditPropertyResponseModel(
                    status=True,
                    message="Unsuccessful",
                    property_id=None
                )
        except (Exception,):
            return BaseResponse(
                status=True,
                message="An error occurred",
            )

    def list(self) -> ListPropertyResponseModel | BaseResponse:
        try:
            result = self.repository.list()
            if result:
                return ListPropertyResponseModel(
                    status=True,
                    message="Successful",
                    properties=result
                )
            else:
                return ListPropertyResponseModel(
                    status=True,
                    message="Unsuccessful",
                    properties=[]
                )
        except (Exception,):
            return BaseResponse(
                status=True,
                message="An error occurred",
            )

    def get(self, id: uuid.UUID) -> GetPropertyResponseModel | BaseResponse:
        try:
            result = self.repository.get(id)
            if result:
                return GetPropertyResponseModel(
                    status=True,
                    message="Successful",
                    property=result
                )
            else:
                return GetPropertyResponseModel(
                    status=True,
                    message="Unsuccessful",
                    property=None
                )
        except (Exception,):
            return BaseResponse(
                status=True,
                message="An error occurred",
            )