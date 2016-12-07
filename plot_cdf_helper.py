# Use to help plot CDFs
#
# Author: Ian W. Stephens

import numpy as np
import matplotlib.pyplot as plt

#Make the pdf points
def xy_cdf(vector):
	sorted_data = np.sort(vector)
	yvals=np.arange(len(sorted_data))/float(len(sorted_data))
	return sorted_data,yvals

#draw step points
def plot_cdf_step(vector,linewidth=4,xmin=0,xmax=90,autoaxis=True,color='k',linestyle='-'):
	x,y = xy_cdf(vector)
	if autoaxis:
		plt.ylim(-0.02,1.02)
		x_inc = 0.02*(xmax - xmin)
		plt.xlim(xmin-x_inc,xmax+x_inc)
	
	array_length = len(x)
	for i in range(array_length):
		if i==0:
			plt.plot([xmin,x[0]],[0,0],c=color,lw=linewidth,ls=linestyle)
			plt.plot([x[0],x[0]],[0,y[0]],c=color,lw=linewidth,ls=linestyle)
		else:
			plt.plot([x[i-1],x[i]],[y[i-1],y[i-1]],c=color,lw=linewidth,ls=linestyle)
			plt.plot([x[i],x[i]],[y[i-1],y[i]],c=color,lw=linewidth,ls=linestyle)
		if i==array_length-1:
			plt.plot([x[i],x[i]],[y[i],1],c=color,lw=linewidth,ls=linestyle)
			plt.plot([x[i],xmax],[1,1],c=color,lw=linewidth,ls=linestyle)
