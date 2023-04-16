# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image
from skimage import metrics
import time
import os
import shutil

images_names_list = []
images_names_list_without_ext = []
images_names_list_png= []
images_names_list_jpg= []
images_names_list_webp= []

def ShowOutputs(images_names_list_without_ext, png_cr, png_mse, png_psnr, jpg_cr, jpg_mse, jpg_psnr, webp_cr, webp_mse, webp_psnr ):
    print("===============")
    print("PNG compression for the", images_names_list_without_ext[i], "image:\n")
    print('Compression Ratio:', png_cr)
    print('mse', png_mse)
    print('PSNR:', png_psnr)
    print("-----------------")
    print("JPEG compression for the", images_names_list_without_ext[i], "image:\n")
    print('Compression Ratio:', jpg_cr)
    print('mse', jpg_mse)
    print('PSNR:', jpg_psnr)
    print("-----------------")
    print("WebP compression for the", images_names_list_without_ext[i], "image:\n")
    print('Compression Ratio:', webp_cr)
    print('mse', webp_mse)
    print('PSNR:', webp_psnr)
    print("===============")
    

if not os.path.exists('compressed_images'):
    os.mkdir('compressed_images')

# Get all image file names from the "images" folder
image_folder_path = 'images/'
image_files = [f for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))]

number_of_images = len(image_files)

for i in range(number_of_images):
    image_path = image_folder_path + image_files[i]
    images_names_list.append(image_path)

for i in range(number_of_images):
    image = Image.open(images_names_list[i])
    images_names_list_without_ext.append(image_files[i].split('.')[0])
    images_names_list_png.append('compressed_images/' + images_names_list_without_ext[i] + ' _compressed' + '.png')
    images_names_list_jpg.append('compressed_images/' + images_names_list_without_ext[i] + ' _compressed' + '.jpg')
    images_names_list_webp.append('compressed_images/' + images_names_list_without_ext[i] + ' _compressed' + '.webp')
    image.save(images_names_list_png[i])
    image.save(images_names_list_jpg[i])
    image.save(images_names_list_webp[i])

#---------------------
# image quality metrics
#---------------------
for i in range(number_of_images):
    
    # get the size of the images
    refference_size = os.path.getsize(images_names_list[i])
    png_compressed_size = os.path.getsize(images_names_list_png[i])
    jpg_compressed_size = os.path.getsize(images_names_list_jpg[i])
    webp_compressed_size = os.path.getsize(images_names_list_webp[i])
    
    # Calculate the compression ratio
    png_cr = refference_size / png_compressed_size
    jpg_cr = refference_size / jpg_compressed_size
    webp_cr = refference_size / webp_compressed_size
    
    # Open the images
    refference_img = Image.open(images_names_list[i])
    png_img = Image.open(images_names_list_png[i])
    jpg_img = Image.open(images_names_list_jpg[i])
    webp_img = Image.open(images_names_list_webp[i])
    
    # Converting the images into numpy arrays
    png_img_array = np.asarray(png_img)
    jpg_img_array = np.asarray(jpg_img)
    webp_img_array = np.asarray(webp_img)
    refference_img_array = np.asarray(refference_img)
    
    # Calculate mse
    png_mse = metrics.mean_squared_error(refference_img_array, png_img_array)
    jpg_mse = metrics.mean_squared_error(refference_img_array, jpg_img_array)
    webp_mse = metrics.mean_squared_error(refference_img_array, webp_img_array)
    
    # Calculate PSNR
    png_psnr = metrics.peak_signal_noise_ratio(refference_img_array, png_img_array, data_range=None)
    jpg_psnr = metrics.peak_signal_noise_ratio(refference_img_array, jpg_img_array, data_range=None)
    webp_psnr = metrics.peak_signal_noise_ratio(refference_img_array, webp_img_array, data_range=None)

    # Showing Output
    ShowOutputs(images_names_list_without_ext, png_cr, png_mse, png_psnr, jpg_cr, jpg_mse, jpg_psnr, webp_cr, webp_mse, webp_psnr )