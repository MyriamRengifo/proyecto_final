[out:json][timeout:180];
// Definimos el área de búsqueda como Florida
area["name"="Florida"]->.searchArea;

// Obtenemos los nodos, caminos y relaciones de unidades educativas
(
  node["amenity"="school"](area.searchArea);
  way["amenity"="school"](area.searchArea);
  relation["amenity"="school"](area.searchArea);
);
out center;
