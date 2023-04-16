# Image Compression and Quality Metrics

This code compresses images using the built-in compression algorithms in the pillow library and calculates quality metrics for both the PNG and JPEG formats. The quality metrics include compression ratio, mean squared error (MSE), and peak signal-to-noise ratio (PSNR).


## Installation

Before running the code, ensure that you have the following packages installed:

* NumPy
* Pillow
* scikit-image

You can install these packages by running the following command:

```
pip install numpy Pillow scikit-image
```


## Usage

1. Place the images you want to compress in the "images" folder in the same path of the python code.
2. Run the code using a Python interpreter.
3. The compressed images will be saved in the "compressed_images" folder and the quality metrics will be displayed in the console.


## Output

The output includes the following information for each image:

* PNG compression ratio, MSE, and PSNR
* JPEG compression ratio, MSE, and PSNR


