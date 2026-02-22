# InverTrack-Chile: Analizador de Portafolio Automatizado

**InverTrack-Chile** es una solución profesional desarrollada en Python para la valoración de activos financieros en tiempo real. Este software permite transformar un archivo estático de transacciones en un reporte financiero detallado, integrando datos de mercados globales de forma automatizada.



## Arquitectura y Diseño
El proyecto sigue una estructura modular para facilitar el mantenimiento y la escalabilidad, cumpliendo con el principio de **Responsabilidad Única (SRP)**:

1.  **`scraper.py` (Capa de Datos):** * Gestiona la conexión con la API de `yfinance`.
    * Implementa lógica de extracción precisa mediante series temporales e indexación con `.iloc`.
    * Incluye validación de integridad para detectar respuestas vacías de la API.

2.  **`logic.py` (Capa de Negocio):**
    * Orquestador principal que utiliza la librería **Pandas**.
    * **Habilidad Pro:** Implementa procesamiento vectorizado mediante el método `.apply()`, inyectando precios en tiempo real de forma masiva sin usar bucles `for`.
    * Automatiza el cálculo de patrimonio total y la exportación de reportes con marcas de tiempo dinámicas (`datetime`).

3.  **`main.py` (Interfaz de Usuario):**
    * Proporciona una interfaz CLI para consultas rápidas de activos individuales y selección de tipo de dato (Apertura/Cierre).



##  Habilidades Técnicas Demostradas
* **Manipulación de Datos:** Uso avanzado de DataFrames de Pandas (Lectura, creación de columnas calculadas y agregaciones).
* **Consumo de APIs:** Integración y limpieza de datos bursátiles externos.
* **Automatización:** Generación de reportes dinámicos con codificación `utf-8-sig` para compatibilidad total con Excel.
* **Clean Code:** Estructura organizada de carpetas (`src/`, `data/`), nombres descriptivos y modularización.

##  Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/InverTrack-Chile.git](https://github.com/tu-usuario/InverTrack-Chile.git)
    ```
2.  **Instalar dependencias:**
    ```bash
    pip install pandas yfinance
    ```
3.  **Configurar activos:**
    Asegúrate de tener tu archivo en `data/mis_activos.csv` con las columnas: `ticket`, `cantidad`, `precio_compra`.
4.  **Ejecutar el reporte:**
    ```bash
    python src/logic.py
    ```

---
*Nota: Este proyecto fue desarrollado con fines educativos para demostrar el dominio de librerías de análisis de datos en Python.*