import sys, glob, operator
from ColumnDataFile import ColumnDataFile as CDF
import matplotlib.pyplot as plt
from pylab import *
import PlotUtility
import numpy
import Smoothing

#files = ['malonic-rdf-alcO-cp2k.dat', 'malonic-rdf-carbO-cp2k.dat', 'malonic-rdf-alcO-amber.dat', 'malonic-rdf-carbO-amber.dat']
files = ['malonic-rdf-alcO-cp2k.dat', 'malonic-rdf-carbO-cp2k.dat', 'MalonicRDF.alcO-H.surface.dat', 'MalonicRDF.carbO-H.surface.dat']
cdfs = [CDF(f) for f in files]

fig = plt.figure(num=1, facecolor='w', edgecolor='w', frameon=True)
fig.subplots_adjust(left=0.06, right=0.97, hspace=0.0)

axs = fig.add_subplot(1,2,1)
x_data = numpy.array(cdfs[0][0])
y_data = numpy.array(cdfs[0][1])
axs.plot (x_data, y_data, linewidth=3.0, color='k', label=str(c+1))
for c in range(len(cdfs)):
	if c < 2:
		y_data = y_data * 0.8
	minorLocator = MultipleLocator(0.25)
	axs.yaxis.set_minor_locator(minorLocator)

	#PlotUtility.ShowLegend(axs)

	if c < 2:
		xticks([1,2,3,4,5],fontsize=0)
		yticks([0.5,1,1.5], fontsize=42)
	else:
		xticks([1,2,3,4,5],fontsize=42)
		yticks([0.5,1,1.5], fontsize=42)
	if c > 1:
		axs.set_xlabel(r'r ($\AA$)', fontsize='42')

	xlim(0.5,5.0)
	ylim(0.0,2.0)
	#axs.set_ylabel(r'g(r)', fontsize='54')

plt.show()
