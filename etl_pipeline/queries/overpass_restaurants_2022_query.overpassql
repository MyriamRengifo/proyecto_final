[out:json][timeout:180];
// Definir el área de búsqueda como Florida
area["name"="Florida"]->.searchArea;

// Obtener nodos, caminos y relaciones de restaurantes
(
  node["amenity"="restaurant"](area.searchArea);
  way["amenity"="restaurant"](area.searchArea);
  relation["amenity"="restaurant"](area.searchArea);
);
out center;
