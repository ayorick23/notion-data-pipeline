import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Settings:
    NOTION_API_KEY = os.getenv("NOTION_API_KEY")
    NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
    OUTPUT_PATH = os.getenv("OUTPUT_PATH")

    @staticmethod
    def validate():
        missing = []
        
        if not Settings.NOTION_API_KEY:
            missing.append("NOTION_API_KEY")
        if not Settings.NOTION_DATABASE_ID:
            missing.append("NOTION_DATABASE_ID")

        if missing:
            raise ValueError(f"Faltan variables de entorno: {', '.join(missing)}")