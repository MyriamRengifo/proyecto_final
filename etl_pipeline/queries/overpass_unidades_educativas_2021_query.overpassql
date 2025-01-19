// Comando para cargar datos OSM en la base de datos
osm2pgsql --create --database=overpass --style=default.style --slim florida-2021.osm.pbf

// Consulta Overpass para obtener unidades educativas en Florida
[out:json][timeout:180];
// Definimos el área de búsqueda como Florida en un servidor local
area["name"="Florida"]->.searchArea;

// Obtener nodos, caminos y relaciones de unidades educativas
(
  node["amenity"="school"](area.searchArea);
  way["amenity"="school"](area.searchArea);
  relation["amenity"="school"](area.searchArea);
);
out center;