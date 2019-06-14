import h5py
import numpy as np

data = {}

for field in ["density", "velocity_x", "velocity_y", "velocity_z"]:
    f = h5py.File("./dataset.h5")
    data[field] = f[field][:]
    f.close()

#data['density'] -= (data['density'].min() * 1.001)
data['density'] = (data['density']-data['density'].min())/(data['density'].max()-data['density'].min())
data['density']=np.maximum(data['density'],1e-16)

data["vx2"] = data["velocity_x"] #* (data["density"]**(-1/2))
data["vy2"] = data["velocity_y"] #* (data["density"]**(-1/2))
data["vz2"] = data["velocity_z"] #* (data["density"]**(-1/2))

data["px"] = data["density"] * data["vx2"]
data["py"] = data["density"] * data["vy2"]
data["pz"] = data["density"] * data["vz2"]

N=64
data["V"] = np.sqrt(data["vx2"]**2+data["vy2"]**2+data["vz2"]**2)
data["P"] = np.sqrt(data["px"]**2+data["py"]**2+data["pz"]**2)
#data["P"] = np.ones((N,N,N))

data["Energy"] = (
                  0.5 * data["density"] * data["V"]**2 + 
                  data["P"]/(1.001 - 1)) 

data["All"] = np.asarray((data["density"],data["px"],data["py"],data["pz"],data["Energy"]))
print(np.isnan(data["All"]).sum() / data["All"].size)

with open("UM_IC", "wb") as f:
        data["All"].astype("float32").tofile(f)

