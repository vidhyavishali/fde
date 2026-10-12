
from fastapi import FastAPI
from fastapi_restPostimpl import router as employee_post_router
from fastapi_RestGetimpl import router as employee_get_router


app = FastAPI()
app.include_router(employee_post_router)
app.include_router(employee_get_router)








