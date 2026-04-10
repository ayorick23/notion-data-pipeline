import pandas as pd

def extract_property_value(prop, id_to_name):
    """
    Extrae el valor de una propiedad de Notion según su tipo
    """

    # Obtener el tipo de la propiedad
    prop_type = prop["type"]

    match prop_type:

        case "title":
            return prop["title"][0]["plain_text"] if prop["title"] else None

        case "rich_text":
            return prop["rich_text"][0]["plain_text"] if prop["rich_text"] else None

        case "number":
            return prop["number"]

        case "unique_id":

            uid = prop["unique_id"]

            # El formato de unique_id puede variar, así que intentamos construirlo de manera legible
            if uid:
                number = uid.get("number")
                prefix = uid.get("prefix")

                if prefix:
                    return f"{prefix}-{number}"
                return str(number)

            return None

        case "select":
            return prop["select"]["name"] if prop["select"] else None

        case "multi_select":
            return ", ".join([x["name"] for x in prop["multi_select"]])

        case "date":
            return prop["date"]["start"] if prop["date"] else None

        case "checkbox":
            return prop["checkbox"]

        case "people":
            return ", ".join([p["name"] for p in prop["people"]])

        case "relation":
            ids = [r["id"] for r in prop["relation"]]
            nombres = [id_to_name.get(i, i) for i in ids]
            return ", ".join(nombres)
        
        case "status":
            return prop["status"]["name"] if prop["status"] else None

        case _:
            return None

def transform_notion_data(data):
    """
    Transforma los datos extraídos de Notion en un DataFrame de pandas
    """
    
    rows = []
    
    # Diccionario para convertir relaciones
    id_to_name = {}

    # Primero, construir el diccionario de ID a Nombre para las relaciones
    for page in data["results"]:

        page_id = page["id"]

        title_prop = page["properties"]["Nombre"]

        if title_prop["title"]:
            name = title_prop["title"][0]["plain_text"]
        else:
            name = None

        id_to_name[page_id] = name

    # Luego, construir las filas del DataFrame
    for page in data["results"]:

        properties = page["properties"]

        row = {"id": page["id"]}

        for prop_name, prop_value in properties.items():

            row[prop_name] = extract_property_value(prop_value, id_to_name)

        rows.append(row)

    # Convertir a DataFrame
    df = pd.DataFrame(rows)
    
    # Convertir la columna de fecha a formato datetime
    df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce").dt.date
    
    # Reordenar columnas
    column_order = [
            "ID",
            "Nombre",
            "Prerrequisito",
            "Categoría",
            "Departamento Principal",
            "Departamento a asignar",
            "Estado",
            "Fecha",
            "Bloqueando",
            "Bloqueado por"
        ]
        
    # Filtrar solo las columnas que existen en el DataFrame
    column_order = [c for c in column_order if c in df.columns]

    df = df[column_order]

    return df