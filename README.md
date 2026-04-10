# <img src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Notion-logo.svg" width="30"> Notion Data Pipeline

Pipeline de datos en **Python** que extrae información desde la **API de Notion**, transforma los datos y genera un **reporte automatizado en Excel** para su posterior consumo en **Power BI**.

Este proyecto automatiza la consolidación de información sobre el progreso de creación de cursos en una plataforma **LMS**, permitiendo visualizar métricas de avance mediante un dashboard interactivo.

# 🚀 Descripción del proyecto

En muchos equipos de desarrollo de contenido educativo, la información sobre el progreso de creación de cursos se gestiona en herramientas colaborativas como **Notion**. Sin embargo, analizar estos datos requiere exportarlos manualmente y prepararlos para herramientas de visualización.

Este proyecto resuelve ese problema mediante un **pipeline automatizado de datos** que:

1. Se conecta a la **API de Notion**
2. Extrae registros desde una base de datos de cursos
3. Limpia y transforma los datos
4. Genera un **reporte estructurado en Excel**
5. Permite alimentar un **dashboard de Power BI**

El resultado es un flujo de datos automatizado que facilita el **seguimiento del progreso de creación de contenido educativo**.

# 🧠 Problema que resuelve

Antes de este pipeline:

- La información debía exportarse manualmente desde Notion
- Era necesario limpiar y estructurar los datos manualmente
- La actualización del dashboard requería preparación previa

Con este proyecto:

- Los datos se extraen automáticamente desde la API
- Se transforman y consolidan en un formato analítico
- El reporte final está listo para ser consumido por Power BI

Esto reduce significativamente el tiempo de preparación de datos y mejora la visibilidad del progreso de producción de cursos.

# ⚙️ Flujo del Pipeline

```text
Notion Database
      │
      ▼
Extracción de datos (API Notion)
      │
      ▼
Transformación y limpieza (Pandas)
      │
      ▼
Generación de reporte Excel
      │
      ▼
Dashboard en Power BI
```

# 🛠️ Tecnologías utilizadas

- **Python**
- **Pandas**
- **Requests**
- **DotEnv**
- **Notion API**
- **Power BI**

Este proyecto demuestra el uso de Python para **automatización de procesos de análisis de datos** e integración con herramientas de **Business Intelligence**.

# 📁 Estructura del proyecto

```text
notion_data_pipeline
│
├── src/
│   ├── extract_notion.py
│   ├── transform_data.py
│   └── load_excel.py
│
├── config/
│   └── config.py
│
├── data/
│   └── processed/
│          └── notion_data.xlsx
│
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

# 🔑 Configuración

Este proyecto utiliza variables de entorno para proteger credenciales de acceso a la API de Notion.

1. **Crea un archivo `.env` basado en el siguiente ejemplo:**

   ```python
   NOTION_API_KEY=your_api_key_here
   DATABASE_ID=your_database_id_here
   ```

# 📦 Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/ayorick23/notion_data_pipeline.git
   ```

2. **Entrar al directorio del proyecto:**

   ```bash
   cd notion_data_pipeline
   ```

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

# ▶️ Ejecución del pipeline

Para ejecutar el pipeline completo:

```bash
python main.py
```

Esto realizará:

1. Conexión con la API de Notion
2. Extracción de datos de la base de datos
3. Transformación de la información
4. Generación del reporte Excel

# 📊 Dashboard en Power BI

El archivo Excel generado por el pipeline es utilizado como fuente de datos para un **dashboard en Power BI** que permite visualizar:

- Progreso de creación de cursos
- Estado de desarrollo de contenidos
- Métricas de producción
- Seguimiento del avance por curso

![Captura de Dashboard](img\dashboard.png)

# 📈 Impacto del proyecto

Este pipeline permitió:

- Automatizar la generación de reportes de seguimiento de cursos
- Reducir el tiempo de preparación de datos
- Centralizar información para análisis en Power BI
- Facilitar el monitoreo del progreso de producción de contenido educativo

# 🧩 Posibles mejoras futuras

- [ ] Programar ejecución automática del pipeline (scheduler)
- [ ] Exportación adicional a formatos CSV o base de datos
- [ ] Manejo avanzado de paginación en la API de Notion
- [ ] Logs y monitoreo del pipeline

# 👨‍💻 Autor

**Dereck Méndez**

Data Analyst | Business Intelligence | Python for Data Automation

Actualmente enfocado en el desarrollo de soluciones de **automatización y análisis de datos con Python** aplicadas a procesos empresariales.
