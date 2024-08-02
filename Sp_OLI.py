import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#plt.style.use(['dark_background'])

Wavelength, CoastalAerosol,Blue,Green,Red,NIR,SWIR1,SWIR2= np.loadtxt('Spectrometer_DataOLI.txt', unpack=True,skiprows=10)

fig = plt.figure()
ax = fig.add_subplot(111)

# Plot markers
ax.plot(Wavelength, CoastalAerosol, c='#9df2ff', lw=1.5,
        mfc='#9df2ff', mec='#9df2ff')
ax.plot(Wavelength, Blue, c='#009deb', lw=1.5,
        mfc='#009deb', mec='#009deb')
ax.plot(Wavelength, Green,c='#05cb36', lw=1.5,
        mfc='#05cb36', mec='#05cb36')
ax.plot(Wavelength, Red, c='#e20000', lw=1.5,
        mfc='#e20000', mec='#e20000')
ax.plot(Wavelength, NIR, c='#ac0000', lw=1.5,
        mfc='#ac0000', mec='#ac0000')
ax.plot(Wavelength, SWIR1, c='#8b216b', lw=1.5,
        mfc='#8b216b', mec='#8b216b')
ax.plot(Wavelength, SWIR2, c='#09688b', lw=1.5,
        mfc='#09688b', mec='#09688b')

#===============Legend guide
ax.legend(["CoastalAerosol", "Blue","Green","Red","NIR","SWIR1","SWIR2"],
          fontsize=5,ncol=7,loc="upper right")
#===============

ax.set_xlabel('Wavelength(μm)',size=8,weight='bold')
ax.set_ylabel('Reflectance',size=8,weight='bold')
plt.figtext(0.25, 0.92, '©2024 Morteza Sharif',size=8,weight='bold')#,rotation=-45
plt.figtext(0.25, 0.89,'Spectral radiance responses of the Operational Land Imager (OLI)',size=8,weight='bold')



plt.show()
