import numpy as np
import yt
import h5py

def run_slice():
    with h5py.File("den_init", "r") as f:
        d = f["/dataset_2"][:]

    ds = yt.load_uniform_grid({'density': d}, d.shape,
            bbox = np.array([ [ 0.0, 1.0], [0.0, 1.0], [0.0, 1.0]]))

    yt.SlicePlot(ds, "x", "density").save()
