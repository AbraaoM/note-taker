from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import create_tables
import os
from controllers.notes_controller import router as notes_router

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
app.include_router(notes_router)
