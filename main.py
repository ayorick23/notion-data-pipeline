from src.extract_notion import extract_notion_data
from src.transform_data import transform_notion_data
from src.load_excel import save_excel
from config.config import Settings

def main():
    
    # Validar configuración
    Settings.validate()
    
    # Extraer
    raw_data = extract_notion_data(
        token=Settings.NOTION_API_KEY,
        database_id=Settings.NOTION_DATABASE_ID
    )

    # Transformar
    df = transform_notion_data(raw_data)

    # Cargar
    save_excel(df, Settings.OUTPUT_PATH)
    
    print(f"Datos exportados exitosamente a {Settings.OUTPUT_PATH}")

if __name__ == "__main__":
    
    main()