import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

#import and sort data
df = pd.read_csv('endconf_toplayer_H.csv',sep=',' ,names=['idx','x','y','z'])
sorted_df = df.sort_values(['x','y'],ascending=[True,True])

x,y,z = np.array(sorted_df['x']), np.array(sorted_df['y']), np.array(sorted_df['z'])

#return evenly spaced numbers over a specified interval
xi = np.linspace(min(x),max(x),800)
yi = np.linspace(min(y),max(y),800)


#interpolate over grid
zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

xi_grid, yi_grid = np.meshgrid(xi, yi)

ax.set_xlabel('a ($\AA$)')
ax.set_ylabel('b ($\AA$)')
ax.set_zlabel('c ($\AA$)')

ax.set_zlim([20.88,21.00])

surf = ax.plot_surface(xi_grid, yi_grid, zi,
                       linewidth=0.2, cmap='cool',
                       vmin=z.min(),vmax=z.max()) #using vmin/vmax to set colormap range (deltas)

plt.show()
