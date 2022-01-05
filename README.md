# Relative Neighborhood Graph

Compute the Relative Neighborhood Graph from a NumPy distance matrix input. 

[https://pypi.org/project/relativeNeighborhoodGraph/] (https://pypi.org/project/relativeNeighborhoodGraph/)

## Instructions

1. Install:

```
pip install relativeNeighborhoodGraph
```

2. Compute the Relative Neighborhood Graph from a NumPy distance matrix input.

```python
from relativeNeighborhoodGraph import returnRNG

RNG = returnRNG.returnRNG(distance_matrix)
```

3. The resulting Relative Neighborhood Graph is returned as a Pandas DataFrame which may be used for visualisation. For example:

![Example Graph](https://user-images.githubusercontent.com/50828923/148155321-71740f52-26cc-4da2-9314-5e6afea6e32e.png)
