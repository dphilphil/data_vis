#global library
import pandas as pd

def datamine_shortestHH():
  import numpy as np

  #blank numpy array
  output = np.array([])

  #import H on surface and in NH3 separately
  HinSurfaceLayer = pd.read_csv('HinTopLayer.dat', sep=r"\s+", names=['atom','x1','y1','z1'])
  HinAmmonia = pd.read_csv('HinNH3.dat', sep=r"\s+", names=['atom','x2','y2','z2'])

  #no of timesteps in MD (3 Hs in Ammonia per timestep)
  tsteps = len(HinAmmonia)/3

  for i in range(tsteps):
    #index of H1, H2, H3 in NH3S
    n = 3*i
    m = n + 1
    w = n + 2

    #[row,column]
    H1x, H1y, H1z = HinAmmonia.iloc[n,1] , HinAmmonia.iloc[n,2], HinAmmonia.iloc[n,3]
    H2x, H2y, H2z = HinAmmonia.iloc[m,1] , HinAmmonia.iloc[m,2], HinAmmonia.iloc[m,3]
    H3x, H3y, H3z = HinAmmonia.iloc[w,1] , HinAmmonia.iloc[w,2], HinAmmonia.iloc[w,3]

    #index of surface H
    p = i*50
    q = p + 50

    #Surface H for the corresponding to timestep
    HSx = HinSurfaceLayer.iloc[p:q,1]
    HSy = HinSurfaceLayer.iloc[p:q,2]
    HSz = HinSurfaceLayer.iloc[p:q,3]

    #calc H-H bond lengths for each of the 3H in NH3 to all H on surface
    HH1 = np.sqrt(((HSx - H1x)**2) + ((HSy-H1y)**2) + ((HSz-H1z)**2))
    HH2 = np.sqrt(((HSx - H2x)**2) + ((HSy-H2y)**2) + ((HSz-H2z)**2))
    HH3 = np.sqrt(((HSx - H3x)**2) + ((HSy-H3y)**2) + ((HSz-H3z)**2))

    #Determine the shortest H-H distance for each H in NH3 to the surface. Make a list
    HHminlist = [min(HH1), min(HH2), min(HH3)]

    #Find the overall shortest H-H distance from any H on NH3 to the surface
    minval = min(HHminlist)
    #Append shortest H-H distance
    output = np.append(output, minval)

  #Legacy. Reshape not strictly required
  output.reshape(-1,1)
  np.savetxt('ShortestHH_2dp.dat',output, fmt="%0.2f") #format used to round values for histogram

def datamine_NH():
  import numpy as np

  #blank numpy arrays
  NH1, NH2, NH3 = np.array([]), np.array([]), np.array([])

  #import H on surface and in NH3 separately
  NinAmmonia = pd.read_csv('NinNH3.dat', sep=r"\s+", names=['atom','x1','y1','z1'])
  HinAmmonia = pd.read_csv('HinNH3.dat', sep=r"\s+", names=['atom','x2','y2','z2'])

  for i in range((len(NinAmmonia))):
    #index of H1, H2, H3 in NH3S
    n = 3*i
    m = n + 1
    w = n + 2

    #[row,column]
    H1x, H1y, H1z = HinAmmonia.iloc[n,1] , HinAmmonia.iloc[n,2], HinAmmonia.iloc[n,3]
    H2x, H2y, H2z = HinAmmonia.iloc[m,1] , HinAmmonia.iloc[m,2], HinAmmonia.iloc[m,3]
    H3x, H3y, H3z = HinAmmonia.iloc[w,1] , HinAmmonia.iloc[w,2], HinAmmonia.iloc[w,3]

    #N in Ammonia
    Nx, Ny, Nz = NinAmmonia.iloc[i,1], NinAmmonia.iloc[i,2], NinAmmonia.iloc[i,3]
    
    #calc N-H bond lengths for each of the 3H in NH3 and append
    NH1 = np.append( NH1, np.sqrt((Nx - H1x)**2 + (Ny-H1y)**2 + (Nz-H1z)**2) )
    NH2 = np.append( NH2, np.sqrt((Nx - H2x)**2 + (Ny-H2y)**2 + (Nz-H2z)**2) )
    NH3 = np.append( NH3, np.sqrt((Nx - H3x)**2 + (Ny-H3y)**2 + (Nz-H3z)**2) )

  #savefiles
  np.savetxt('NH1_BondLength.dat', NH1, fmt="%0.2f") #round
  np.savetxt('NH2_BondLength.dat', NH2, fmt="%0.2f")
  np.savetxt('NH3_BondLength.dat', NH3, fmt="%0.2f")
  
def histogram():
  rawdata = pd.read_csv('ShortestHH_2dp.dat',names=['HH'])
  rawdata['Freq'] = rawdata.groupby('HH')['HH'].transform('count') #group same values and count frequency
  rawdata = rawdata.drop_duplicates(subset=['HH']) #remove duplicate rows using column 'HH' to find them
  rawdata.to_csv('ShortestHH_2dp.histo', index=False, header=False)
