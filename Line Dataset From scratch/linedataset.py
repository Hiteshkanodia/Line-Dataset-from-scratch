from skimage.draw import line_aa
import matplotlib.pyplot as plt 
import matplotlib as mpl
import numpy as np 
import math as mt
import cv2
import os

mpl.rcParams['savefig.pad_inches'] = 0

def creating_directory(name_of_directory,f):
	directory = name_of_directory
	if f==0:
		parent_directory = os.getcwd()
	else:
		parent_directory = os.getcwd()+"/Dataset_of_DL"
	path = os.path.join(parent_directory, directory)
	os.mkdir(path)
	return path

def name_of_image(l,w,c,d,index,d_path):
	f = []
	if l==3:
		f.append(0)
	else:
		f.append(1)
	if w==1:
		f.append(0)
	else:
		f.append(1)
	if c==(255,0,0):
		f.append(0)
	else:
		f.append(1)
	name = str(d_path)+str("/")+str(f[0])+"_"+str(f[1])+"_"+str(d)+"_"+str(f[2])+"_"+str(index)+".jpg"
	return name

def name_of_directory(l,w,c,d):
	f = []
	if l==3:
		f.append(0)
	else:
		f.append(1)
	if w==1:
		f.append(0)
	else:
		f.append(1)
	if c==(255,0,0):
		f.append(0)
	else:
		f.append(1)
	name = str(f[0])+"_"+str(f[1])+"_"+str(d)+"_"+str(f[2])
	return name

def making_dataset(length,width,color,angle):
	for l in length:
		for w in width:
			for c in color:
				for d in range(3,4):
					d_name = name_of_directory(l,w,c,d)
					d_path = creating_directory(d_name,1)
					index = 1
					for m in range(8,20):
						for n in range(8,20):
							img = np.zeros((28,28,3), dtype = np.uint8)
							x2 =  int(round(m + l*mt.cos(d*angle)))
							y2 =  int(round(n - l*mt.sin(d*angle)))
							x3 =  int(round(m - l*mt.cos(d*angle)))
							y3 =  int(round(n + l*mt.sin(d*angle)))
							cv2.line(img,(m,n),(x2,y2),c,w,8,0)
							cv2.line(img,(m,n),(x3,y3),c,w,8,0)
							name = name_of_image(l,w,c,d,index,d_path)
							plt.imshow(img)
							plt.axis('off')
							plt.savefig(name,bbox_inches='tight')
							index = index+1

length = [3,7]
width = [1,3]
color = [(255,0,0),(0,0,255)]
angle = mt.pi / 12;
creating_directory("Dataset_of_DL",0)
making_dataset(length,width,color,angle)


