// Comando para cargar datos OSM en la base de datos
osm2pgsql --create --database=overpass --style=default.style --slim florida-2015.osm.pbf

// Consulta Overpass para obtener parques de diversiones y centros comerciales en Florida para 2023
[out:json][timeout:180];
// Definimos el área de búsqueda como Florida
area["name"="Florida"]->.searchArea;

// Obtenemos los nodos, caminos y relaciones de parques de diversiones y centros comerciales
(
  node["leisure"="theme_park"](area.searchArea);
  way["leisure"="theme_park"](area.searchArea);
  relation["leisure"="theme_park"](area.searchArea);
  
  node["shop"="mall"](area.searchArea);
  way["shop"="mall"](area.searchArea);
  relation["shop"="mall"](area.searchArea);
);
out center;

