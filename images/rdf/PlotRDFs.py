import sys, glob, operator
from ColumnDataFile import ColumnDataFile as CDF
import matplotlib.pyplot as plt
from pylab import *
import PlotUtility
import numpy
import Smoothing


def fixPlot(axs):
	axs.set_xlabel(r'r ($\AA$)', fontsize='36')
	xlim(0.5,5.0)
	ylim(0.0,2.0)
	xticks([1,2,3,4,5],fontsize=36)
	yticks([0.5,1,1.5], fontsize=36)

files = ['malonic-rdf-alcO-cp2k.dat', 'malonic-rdf-carbO-cp2k.dat', 'MalonicRDF-rdf-alcO-oldparms.dat', 'MalonicRDF-rdf-carbO-oldparms.dat', 'malonic-rdf-alcO-amber.dat', 'malonic-rdf-carbO-amber.dat', 'MalonicRDF-rdf-alcO-newparms.dat', 'MalonicRDF-rdf-carbO-newparms.dat', 'MalonicRDF-rdf-alcO-1.dat', 'MalonicRDF-rdf-carbO-1.dat'] 
cdfs = [CDF(f) for f in files]

fig = plt.figure(num=1, facecolor='w', edgecolor='w', frameon=True)
fig.subplots_adjust(left=0.06, right=0.97)

axs1 = fig.add_subplot(1,2,1)
fixPlot(axs1)
axs2 = fig.add_subplot(1,2,2)
fixPlot(axs2)

for c in range(len(cdfs)):
	x_data = numpy.array(cdfs[c][0])
	y_data = numpy.array(cdfs[c][1])

	if c == 1:
		y_data = y_data * 0.8

	axs = axs1
	if (c+1)%2 == 0:
		axs = axs2

	name = files[c].split('.')[-2].split('-')[-1]
	sys = files[c].split('-')[2]
	axs.plot (x_data, y_data, linewidth=3.0, label=name+sys)

	minorLocator = MultipleLocator(0.25)
	axs.yaxis.set_minor_locator(minorLocator)

	#if c < 2:
	#else:
		#xticks([1,2,3,4,5],fontsize=42)
		#yticks([0.5,1,1.5], fontsize=42)
	#if c > 1:
	#axs.set_ylabel(r'g(r)', fontsize='54')

PlotUtility.ShowLegend(axs1)
PlotUtility.ShowLegend(axs2)
plt.show()
