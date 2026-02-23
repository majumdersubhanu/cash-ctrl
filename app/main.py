from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.api.v1.router import api_router
from app.core.auth import auth_backend
from app.core.logging import setup_logging
from app.core.users import fastapi_users
from app.db.init_db import init_db
from app.db.session import engine
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.api.middleware import LoggingMiddleware
from app.core.security import limiter
