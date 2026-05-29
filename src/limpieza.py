import geopandas as gpd

def cargar_y_limpiar():

    gdf = gpd.read_file(
        "data/raw/gis_osm_roads_free_1.shp"
    )

    gdf = gdf.dropna(subset=["geometry"])

    gdf = gdf[gdf.geometry.is_valid]

    return gdf