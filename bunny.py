#import modules required in the project
import random
from PIL import Image
import numpy as np

#generates unique id
import uuid 

import os
# import bunny pixel array tables for random rolls
import bunny_array as b

id=uuid.uuid1() #generates unique id

# Roll for bunny type
for y in range(150):
  y = random.randint(0, 100) #will generate random integer in the range of 0 and 100

  if y in range(0, 30):        
    array = b.sassy_bun  # sassy bunny array

  elif y in range(30, 60):    
    array = b.cute_bun     # cute bunny array
  elif y in range(60, 90):                      
    array = b.eyepatch_bun   # pirate bunny array
  elif y in range(90, 120):                      
    array = b.mask_bun   # mask bunny array
  else:
    array=b.basic_bun  #basic  bunny


# dtype=np.uint8 converts array  RGB values to integers 

arr = np.array(array, dtype=np.uint8)

#PIL is used to create an image
bunny_image = Image.fromarray(arr)

#final dimensions of the image, original pixels are 24*24 or 32*32
dimensions = (480,480)
bunny_image = bunny_image.resize(dimensions, resample=0)

# # save image
# # path="/Users/mehra/Desktop/bunny_images/"
# dirname = os.path.dirname("bunny_images")
# print(dirname)

path="/home/runner/nft/bunny_images/"

imgname = path + "bunny image "+str(id)+'.png'
bunny_image.save(imgname)


#count the number of image generated
totalImg = 0


for base,dirs,files in os.walk(path):
  print('Searching in : ',base)
  for Images in files:
    totalImg += 1

c=len(os.listdir(path))
print(c)
print('Total number of Bunny images generated so far',totalImg)



