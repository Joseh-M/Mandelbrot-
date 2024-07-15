#!python

from PIL import Image

#%%time

image = Image.effect_mandelbrot((5200, 4400), (-2,-1.1,0.6,1.1),400)
image.save('mandelbrot400.jpg')
