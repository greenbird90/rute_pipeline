
import folium
from ors_config import COORDINATES

def create_map(route_coords):
    avg_lat = (COORDINATES[0][1] + COORDINATES[1][1]) / 2
    avg_lon = (COORDINATES[0][0] + COORDINATES[1][0]) / 2
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=12)

    folium.Marker(location=[COORDINATES[0][1], COORDINATES[0][0]], tooltip="Kantor", icon=folium.Icon(color="blue")).add_to(m)
    folium.Marker(location=[COORDINATES[1][1], COORDINATES[1][0]], tooltip="Rumah", icon=folium.Icon(color="green")).add_to(m)

    points = [[lat, lon] for lon, lat in route_coords]
    folium.PolyLine(points, color="red", weight=4.5, opacity=0.8).add_to(m)

    m.save("rute_pipeline/output/rute_map.html")
