import numpy as np
import yt
import h5py

def run_slice():
    with h5py.File("dataset.h5", "r") as f:
        d = f["/density"][:]

    ds = yt.load_uniform_grid({'density': d}, d.shape,
            bbox = np.array([ [ 0.0, 1.0], [0.0, 1.0], [0.0, 1.0]]))

    yt.ProjectionPlot(ds, "x", "density").save()
