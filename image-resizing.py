# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 11:30:19 2022

@author: Mary Beth Cassity
"""
from PIL import Image 
import os

im_path = "path\to\im\dir" #path to current im folder
cropped_path = "path\to\im\dir" #path to cropped im folder 
resized_path = "path\to\im\dir" #path to resized im folder 

os.path.exists(im_path) #just checking if the path exists -- you can comment this out 
os.path.exists(cropped_path) #just checking if the path exists -- you can comment this out 

for ii in os.listdir(im_path):
    file_name = os.path.basename(ii)
    old_path = os.path.join(im_path,file_name)
    new_path = os.path.join(cropped_path,file_name)
    image = Image.open(old_path)
    height = image.height
    width = image.width
    
    if (width % 2) == 1:
        width = width - 1
    
    if (height % 2) == 1:
        height = height -1
        
    if(width<height):
        orig_height = height
        new_height = width 
        left = 0
        upper = 0.5*orig_height - 0.5*new_height
        right = width
        lower = 0.5*orig_height + 0.5*new_height 
        image.crop((left, upper, right, lower))
    
    if(height<width):
        orig_width = width
        new_width = height 
        left = 0.5*orig_width - 0.5*new_width
        upper = 0
        right = 0.5*orig_width + 0.5*new_width
        lower = height
        cropped_im = image.crop((left, upper, right, lower))
    
    
    cropped_im.save(new_path)

smallest_height = 9000 #this number is a placeholder -- edit for specific use

for ii in os.listdir(cropped_path):
    file_name = os.path.basename(ii)
    old_path = os.path.join(cropped_path,file_name)
    image = Image.open(old_path)
    height = image.height
    
    if (height < smallest_height):
        smallest_height = height
        print(smallest_height) #checking the smallest dimesion-- you can comment this out

for ii in os.listdir(cropped_path):
    file_name = os.path.basename(ii)
    old_path = os.path.join(cropped_path,file_name)
    new_path = os.path.join(resized_path,file_name)
    image = Image.open(old_path)
    image.thumbnail((smallest_height, smallest_height))
    
    image.save(new_path)
    
    
