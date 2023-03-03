from src.endpoint.base import *
from src.model.user import ModelUser, ModelUserRole
from src.schema.user import SchemaUser, SchemaUserUpdate, SchemaUserRole, SchemaUserRoleUpdate

router = APIRouter(
    prefix = "/user",
    tags = ["User"]
)

