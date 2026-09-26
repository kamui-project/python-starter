import os


def database_url():
    url = os.environ.get("DATABASE_URL", "sqlite:///local.db")
    # Use the installed driver regardless of SQLAlchemy's version-specific default.
    if url.startswith("postgresql://"):
        return url.replace("postgresql://", "postgresql+psycopg2://", 1)
    return url


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(32).hex())
    SQLALCHEMY_DATABASE_URI = database_url()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
