import requests

def extract_notion_data(token, database_id):
    """
    Extrae datos de una base de datos de Notion usando la API
    """

    # Construir la URL de la API para consultar la base de datos
    url = f"https://api.notion.com/v1/databases/{database_id}/query"

    # Configurar los encabezados de la solicitud con el token de autenticación
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28"
    }

    # Manejar paginación para obtener todos los resultados
    all_results = []
    has_more = True
    next_cursor = None

    while has_more:

        payload = {}

        # Si hay un cursor para la siguiente página, agregarlo al payload
        if next_cursor:
            payload["start_cursor"] = next_cursor

        # POST a la API de Notion
        response = requests.post(url, headers=headers, json=payload)

        data = response.json()

        # Extraer los resultados de la respuesta y agregarlos a la lista total
        results = data["results"]

        # Agregar los resultados actuales a la lista total
        all_results.extend(results)

        # Verificar si hay más resultados para paginar
        has_more = data["has_more"]
        next_cursor = data["next_cursor"]

    return {"results": all_results}