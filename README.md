d3, the graphics libary written in javascript, includes classes for drawinng/rendering graphs ('graphs' as in the things studied by graph theorists, and comprised of nodes and edges--not the things you create in MS Excel to visualize your data).

The data foramt required by the graph classes is irregular--i.e., it's not a format recognizable to graph analysis libraries, etc. Therefore, the python module here converts a graph expressed as an *adjacency matrix* to the d3 standard format.

To use it, you pass in a NumPy 2D array (which represents a graph's adjancecy matrix) or a python nested list (a list of lists, also which represents an adjacency matrix); the module transforms the graph in AM form to the JSON structure required by d3, and writes it to a JSON file.
