from datetime import datetime
from src.endpoint.base import *
from src.model.book import ModelBook, ModelBookType
from src.schema.book import SchemaBook, SchemaBookUpdate, SchemaBookType, SchemaBookTypeUpdate

router = APIRouter(
    prefix = "/book",
    tags = ["Books"]
)


@router.post("/create-book-type", status_code=200)
async def create_book_type(payload: SchemaBookType, response=Response):
    result = RETURN_FORMAT
    try:
        book_type = ModelBookType(**payload.dict())
        book_type.created_by = ""
        db.session.add(book_type)
        db.session.commit()

        result["code"] = 200
        result["message"] = "success"
        
    except Exception as error:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        result["code"] = 500
        result["message"] = error

    return result



@router.update("/update-book-type/{pk}", status_code=200)
async def update_book_type(pk: str, payload: SchemaBookTypeUpdate, response=Response):
    result = RETURN_FORMAT

    if pk:
        try:
            book_type = db.session.get(ModelBookType, pk)

            if not book_type:
                response.status_code = status.HTTP_404_NOT_FOUND
                result["code"] = "404"
                result["message"] = "Data Not Found"

            else:
                for key, value in payload.dict().items():
                    setattr(book_type, key, value)
                book_type.last_update_date = datetime.now()
                book_type.last_update_by = ""

                db.session.add(book_type)
                db.session.commit()

                result["code"] = "200"
                result["message"] = "Success"
        
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            result["code"] = "500"
            result["message"] = "Internal Server Error"
            result["detail"] = error
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        result["code"] = "400"
        result["message"] = "Bad Request"
        result["detail"] = "Please enter id from the data"

    return result



@router.delete("/delete-book-type/{pk}", status_code=200)
async def delete_book_type(pk: str, response: Response):
    result = RETURN_FORMAT

    if pk:
        book_type = db.session.get(ModelBookType, pk)

        if not book_type:
            response.status_code = status.HTTP_404_NOT_FOUND
            result["code"] = "404"
            result["message"] = "Data Not Found"
        
        else:
            book_type.active_flag = False
            book_type.inactive_date = datetime.now()
            book_type.inactive_by = ""
            
            db.session.add(book_type)
            db.session.commit()

            result["code"] = "200"
            result["message"] = "Success"

    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        result["code"] = "400"
        result["message"] = "Bad Request"
        result["detail"] = "Please enter id from the data"

    return result



@router.get("/get-book-type/", status_code=200)
async def get_book_type(pk: Optional[str] = None, is_active: str = Query("y", description="Default input is Y"), response=Response):
    try:
        result = RETURN_FORMAT
        is_active = True if is_active.lower() == "y" or is_active is None else False

        if pk:
            book_type = db.session.query(ModelBookType).filter(ModelBookType.type_id == pk, ModelBookType.active_flag == is_active).all()
        else:
            book_type = db.session.query(ModelBookType).filter(ModelBookType.active_flag == is_active).all()
        
        if book_type:
            result["code"] = "200"
            result["message"] = "Data Not Found"
            result["data"] = book_type
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            result["code"] = "404"
            result["message"] = "Data Not Found"
    
    except Exception as error:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        result["code"] = "500"
        result["message"] = "Internal Server Error"
        result["detail"] = error

    return result