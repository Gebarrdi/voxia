# main.py — punto de entrada de la aplicación FastAPI
# Aquí se configura y arranca todo el backend

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.routers import candidatos, temas, comparar, ai

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API para análisis electoral con IA",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://voxia-five.vercel.app",  # ← agrega tu URL de Vercel
        "https://*.vercel.app",  # ← permite todos los subdominios
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra los routers
app.include_router(candidatos.router)
app.include_router(temas.router)
app.include_router(comparar.router)
app.include_router(ai.router)


@app.get("/api/health")
async def health_check():
    return {
        "status": "ok",
        "app": settings.app_name,
        "version": settings.app_version
    }


@app.get("/")
async def root():
    return {"mensaje": "Bienvenido a VoxIA 🗳️"}
