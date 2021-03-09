from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import imageio

filename = input("Please input image filename, e.g. 'myImage.png' ")
filename_without_extension = filename[:len(filename)-4]

img = plt.imread(f'Images/{filename}').astype(np.float64)
rows, cols, colors = img.shape

#Define the catmap
def catmap(x, y, k):
  return ((2*x + y) % k, (x + y) % k)

images = [img]

#Initialise i
i=0

#Iterate images until we arrive back at original image
while ssim(img, images[i], data_range=images[i].max() - images[i].min(), multichannel=True) < 0.99 or i==0:
  #Create placeholder array with same dimensions as the given image
  newImg = np.zeros(img.shape)

  #Loop over all pixels in the image
  for x in range(cols):
    for y in range(rows):
      #Assign old pixel color to variable called oldVal
      oldVal = images[i][x, y]
      #Use catmap function to find the updated coordinates
      newCoords = catmap(x, y, cols)
      #Assign updated coordinates the color of the previous iterate
      newImg[newCoords[0], newCoords[1]] = oldVal
  
  images.append(newImg)
  print(f"i = {i}")
  i+=1

""" Uncomment this to show PyPlot Plot

#Create figure
fig = plt.figure(figsize=(12, 8))

#Plot images
for i in range(len(images)):
  fig.add_subplot(#columns, #rows, i+1)
  plt.axis('off')
  plt.imshow(images[i])

plt.show()

"""
period = len(images)

imageio.mimsave(f'GIFs/{filename_without_extension}.gif', images)
textFile = open(f"ImagePeriods/{filename_without_extension}.txt", "w")
textFile.write(f"{filename} has an Arnold Cat Map period of period: {period}.")
textFile.close()

print(f"{filename} has an Arnold Cat Map period of period: {period}.")
print(f"A GIF animation has been created and the file can be found at: 'GIFs/{filename_without_extension}.gif'!")