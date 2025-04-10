from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import create_tables
import os
from controllers.home_controller import router as home_router

app = FastAPI(title="Note Taker API")

# Create database tables on startup
create_tables()

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo rotas
app.include_router(home_router)
