### CMPT-353-Final-Project


link for Final Report（google doc）:
  https://docs.google.com/document/d/1Au4LTnuOcqqJmp4jOZMuyPX0QGH7_TZpCVE1aLEgMeU/edit?usp=sharing

### Code for getting data from Overpass Turbo:
[out:json][timeout:25];
// fetch area “Burnaby” to search in
{{geocodeArea:Burnaby}}->.searchArea;
// gather results
(
  // query part for: “amenity= and building=* and shop=* and leisure=*”
  node["amenity"](area.searchArea);
  node["building"](area.searchArea);
  node["shop"](area.searchArea);
  node["leisure"](area.searchArea);
  way["amenity"](area.searchArea);
  way["building"](area.searchArea);
  way["shop"](area.searchArea);
  way["leisure"](area.searchArea);
  relation["amenity"](area.searchArea);
  relation["building"](area.searchArea);
  relation["shop"](area.searchArea);
  relation["leisure"](area.searchArea);
);
// print results
out body;
>;
out skel qt;
