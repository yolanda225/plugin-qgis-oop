# QGIS Plugin OOP

This Plugin is developed as part of a course on Object Oriented Programming (OOP) at ENSG, year 2025-2026.

The Plugin calculates a polygon from a starting point inserted by the user.
The result represents a geolocated surface where all points inside of the polygon can be reached in a certain time/distance. 
For the implementation, the geoportal service of IGN is used:
https://geoservices.ign.fr/services-geoplateforme-itineraire

The IGN Geoportal isochrone API can be tested here:
https://www.geoportail.gouv.fr/depot/swagger/itineraire.html#/Utilisation/isochrone


## How to use
- Clone the repository and move the folder (or create a link) to the plugin directory of QGIS e.g. at 
```/home/user/.local/share/QGIS/QGIS3/profiles/default/python/plugins```
- Add the Plugin to your QGIS Project via Plugins/ Manage and Install Plugins
- When running the Plugin, select first a resource (all other drop boxes are populated depending on the resource!)
- Select all other parameters and execute

## To note
Calculations with to small or big values (e.g. distance of 1m, time of 300h) get a code of 404 from IGN Geoportal and cause an error message after the execution in QGIS

## Documentation
![Alt text](diagrams/class_diagram.png)
![Alt text](diagrams/activity_diagram.png)
![Alt text](diagrams/use_case_diagram.png)
