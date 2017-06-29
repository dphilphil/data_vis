import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

#import and sort data
df = pd.read_csv('fil.csv',sep=',' ,names=['x','y','z'])
sorted_df = df.sort_values(['x','y'],ascending=[True,True])

x,y,z = np.array(sorted_df['x']), np.array(sorted_df['y']), np.array(sorted_df['z'])

#return evenly spaced numbers over a specified interval
xi = np.linspace(x.min(),x.max(),800 )
yi = np.linspace(y.min(),y.max(),800 )

#interpolate over grid
zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

xi_grid, yi_grid = np.meshgrid(xi, yi)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_zlim([0.695,0.715])

surf = ax.plot_surface(xi_grid, yi_grid, zi,
                       linewidth=0.2, cmap='cool',
                       vmin=z.min(),vmax=z.max()) #using vmin/vmax to set colormap range (deltas)

plt.show()
