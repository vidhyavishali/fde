from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_invoice import load_invoices, router as invoice_router


@asynccontextmanager
async def lifespan(application: FastAPI):
	load_invoices() #anything before yield is executed before the application starts.
	yield # This is where the application runs, and any cleanup code can be placed after this yield statement.


app = FastAPI(lifespan=lifespan)
app.include_router(invoice_router)  
