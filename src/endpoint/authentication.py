from src.endpoint.base import *
from src.model.user import ModelUser

router = APIRouter(
    prefix = "/auth",
    tags = ["Authentication"]
)

