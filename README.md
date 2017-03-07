##Google Street View
Experiments with StreetView API.

Testing the ability of google street view to return images in a given coordinates.

As we don't know the street numbers in the street, a simple heuristics is implemented:
start from 1

if the new returned coordinates for the number are unique then record the point/ if not ignore

if there are to many duplicite points, break
