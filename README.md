# Rutas Óptimas en Red Vial Urbana

Proyecto de análisis de redes viales urbanas utilizando teoría de grafos y datos reales de OpenStreetMap/Geofabrik para Bolivia.

## Objetivos

El proyecto busca modelar una red vial urbana como un grafo dirigido ponderado para realizar análisis de rutas óptimas y conectividad.

### Objetivos principales

* Alcance vehicular dentro de 5 km.
* Identificación de islas viales.
* Cálculo del diámetro vial.
* Construcción de árbol de expansión mínima (MST).
* Comparación de rutas por distancia y tiempo.

---

# Dataset

Fuente:

* https://download.geofabrik.de/south-america/bolivia.html

Archivos utilizados:

* bolivia-latest-free.shp.zip
* bolivia-latest.osm.pbf

---

# Estructura del Proyecto

```text
proyecto_rutas/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── clean/
│
├── docs/
├── resultados/
│
├── src/
│   ├── main.py
│   ├── limpieza.py
│   ├── construir_grafo.py
│   ├── algoritmos.py
│   ├── analisis.py
│   ├── visualizacion.py
│   └── utils.py
│
├── requirements.txt
└── README.md
```

---

# Instalación

## Crear entorno virtual

```bash
py -3.11 -m venv venv
```

## Activar entorno virtual

### CMD

```bash
venv\Scripts\activate
```

### PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

---

# Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución

```bash
python src/main.py
```

---

# Tecnologías Utilizadas

* Python
* NetworkX
* Pandas
* GeoPandas
* Matplotlib
* Shapely

---

# Funcionalidades

## Limpieza de Datos

* Eliminación de valores inválidos.
* Corrección de velocidades faltantes.
* Normalización de atributos.
* Validación de nodos y aristas.

## Construcción del Grafo

* Grafo dirigido.
* Aristas ponderadas por distancia.
* Soporte para restricciones de sentido vial.

## Análisis Implementados

* Dijkstra
* Bellman-Ford
* BFS
* MST
* Componentes conexas

---

# Resultados Esperados

* Número de nodos alcanzables.
* Tamaño de componente gigante.
* Tiempo de ejecución de algoritmos.
* Comparación de rendimiento.

---
