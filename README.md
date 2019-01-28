# archipelago
a simple class for plotting a scatter plot matrix for visualizing multidimensional data


# To Use
```python
import scama.scama as arc
arc(data=[data])
```

where [data] is a numpy-type or numpy-compatible object of shape NxM,

with the N rows the samples, the first M-1 columns the feature values, and the last column the labels.

A default test data is provided in test/data.npy and is used if [data] is left empty.

Modify parameters in params.py

# Requirements

numpy

matplotlib

