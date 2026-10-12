"""Database connection settings for the school demonstration project."""
import os
from pathlib import Path

from dotenv import load_dotenv
import mysql.connector

PROJECT_ROOT = Path(__file__).resolve().parent
load_dotenv(PROJECT_ROOT / ".env")


def connect_db():
    """Open a connection using settings from the local .env file."""
    password = os.getenv("DB_PASSWORD", "")
    if not password:
        raise RuntimeError("Set DB_PASSWORD in a local .env file first.")
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=password,
        database=os.getenv("DB_NAME", "orphanage_class12_demo_v2"),
    )
