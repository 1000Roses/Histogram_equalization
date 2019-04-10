import cv2, os,sys				#|
import numpy as np				#|		#Import 
import collections				#|
from matplotlib import pyplot as plt		#|
#--------------------------------------------

Open_Image = sys.argv[1]					#		
assert os.path.isfile(Open_Image), '%s not found' % Open_Image	# Code to open your image
img = cv2.imread(Open_Image)					#

#----------------------------------------------
def create_histogram(img,output = "input"):
	plt.cla()
	plt.hist(img.ravel(),256,[0,256])
	plt.xlabel('Intensity')
	plt.title('%s'%output)
	plt.ylabel('Frequency')
	plt.savefig('Histogram_%s.png'%output)
#----------------------------------------------

create_histogram(img,output= "Before_Equalization")   # print histogram of image before equalization 		

z = img.ravel()
a = np.array(z)
b = collections.Counter(a) #Create dictionary
c = collections.OrderedDict(sorted(b.items())) # Sort dictionary



#--------------find cdf_min-----------------------
key_min = min(c.keys(),key = (lambda k: c[k]))	#|	# find cdf_min
cdf_min = c[key_min]				#|
#------------------------------------------------

#---------------------------------------------
AllOfPixels = img.shape[0]*img.shape[1]*3	#|	#Code to find all of Pixels in image
#---------------------------------------------

#----------------------------------------------------------------------------------------------------
k = 0;													#|																							#|																										#|
for i in c :					    #--------	VanTien	@Author	--------		#|
	if (k >= 1):											#|
		c[i] = c[i] + Temp									#|
	Temp = c[i]				    							#| 		#Code Equalization.
	k = k + 1											#|
for j in c :												#|
	c[j]= round(((c[j] - cdf_min)/(AllOfPixels - cdf_min)) * 255) #value		        	#|
	if (c[j] > 255):										#|  
		c[j] = 255										#| =====     ====    ===========
for row in range(img.shape[0]):			 							#|   ====   ====         ===
	for col in range(img.shape[1]): 								#|    ==== ====          ===
		for step in range(3):									#|     =======    <:>    ===
			img[row][col][step] = c[img[row][col][step]]					#|
#-----------------------------------------------------------------------------------------------------

create_histogram(img,output = "After_Equalization")  #print histogram of image after equalization

print("The image after histogram Equalization by VanTien")

print("Loading...Done------>Click on folder to find image after Equal <:>")
cv2.imwrite("Equalization_histogram_Of_Image.jpg",img)
