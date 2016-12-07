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


Planckbfield_outflow = [89.46343631,9.627169873,18.29036448,16.56591449,79.52273318,70.28071009,85.97690602,70.89686929,83.09395873,28.91683933,42.99751578,7.991303071,82.01143297,11.82945953,89.87948798,30.78246256,20.87269876,75.14055893,24.66585195,57.12852247,44.11533186,60.73374176,78.92761961,48.50555322,67.33216873,47.0963099,42.90367083,17.84527042,3.050197876,49.50036897,34.49955444,26.88669482,9.592527646,55.14902962,37.10347552,25.36192456,59.64884297,49.33736739,6.277684167,3.830804936,4.036796438,5.997201254,33.71159556,66.64824395,9.717409867,31.94147714,7.337053257,27.93008662,83.99122397,5.462087086,36.17065691,54.17337263,38.14615443,8.147701245,2.872996995,21.5021178,84.3743922]
plot_cdf_step(Planckbfield_outflow)
