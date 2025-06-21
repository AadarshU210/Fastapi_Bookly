from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.service import BookService
from src.db.main import get_session
from src.books.schemas import Book,BookCreateModel, BookUpdateModel, BookDetailModel
from typing import List
from src.auth.dependencies import AccessTokenBearer, RoleChecker
from src.errors import BookNotFound

book_router = APIRouter()
book_service = BookService()
access_token_bearer = AccessTokenBearer()
role_checker = Depends(RoleChecker(['admin', 'user']))
'''Since we are providing role_checker 
as a dependency in decorators it is necessary that we wrap 
the declartion where we made the 
instance of RoleChecker into Depends function. Another method we could have
done is similar to pass in function parameters like this
_:bool = Depends(role_checker)'''

@book_router.get('/', response_model = List[Book], dependencies=[role_checker])
async def get_all_books(session:AsyncSession = Depends(get_session), user_details = Depends(access_token_bearer)):
   
    print(user_details)
    books = await book_service.get_all_books(session)
    return books

@book_router.get('/user/{user_uid}', response_model = List[Book], dependencies=[role_checker])
async def get_user_book_submissions(user_uid:str, session:AsyncSession = Depends(get_session), user_details = Depends(access_token_bearer)):
   
    books = await book_service.get_user_books(user_uid, session)
    return books
  
@book_router.post('/', status_code=status.HTTP_201_CREATED, response_model=Book, dependencies=[role_checker])
async def create_a_book(book_data:BookCreateModel,session:AsyncSession = Depends(get_session), token_details:dict = Depends(access_token_bearer)) -> dict:
    user_id = token_details.get('user')['user_uid']
    new_book = await book_service.create_book(book_data,user_id, session)
    return new_book
    

@book_router.get('/{book_uid}', response_model=BookDetailModel, dependencies=[role_checker])
async def get_book(book_uid:str, session:AsyncSession = Depends(get_session), user_details = Depends(access_token_bearer)) -> dict:
    print(user_details)
    book = await book_service.get_book(book_uid, session )
    
    if book:
        return book
    else:
        raise BookNotFound()
        

@book_router.patch('/{book_uid}', response_model=Book, dependencies=[role_checker])
async def update_book(book_uid:str, book_update_data:BookUpdateModel, session:AsyncSession = Depends(get_session), user_details = Depends(access_token_bearer)) -> dict:
  
    print(user_details)
    updated_book = await book_service.update_book(book_uid, book_update_data, session)
    if updated_book is None:
        raise BookNotFound()
    else:
        return updated_book
        

@book_router.delete('/{book_uid}', status_code = status.HTTP_204_NO_CONTENT, dependencies=[role_checker])
async def delete_book(book_uid:str, session:AsyncSession = Depends(get_session),user_details = Depends(access_token_bearer)):
    
    print(user_details)
    deleted_book = await book_service.delete_book(book_uid, session)
    if deleted_book is None:
        raise BookNotFound()
    else:
        return {}
        