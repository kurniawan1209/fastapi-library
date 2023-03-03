from fastapi import APIRouter, Response, status, Path, Query
from fastapi_sqlalchemy import db
from typing import Optional
from sqlalchemy import text, and_


RETURN_FORMAT = {
    "code": "",
    "message": "",
    "detail": "",
    "datas": ""
}