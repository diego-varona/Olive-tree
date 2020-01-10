from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import match_template

ImagenTotal = np.asarray(Image.open('OlivoTotal.png'))
ImagenTemplate = np.asarray(Image.open('OlivoTemplate_small.png'))

image = ImagenTotal[:,:,1]
olivetree = ImagenTemplate[:,:,1]
plt.imshow(olivetree)
plt.show()

result = match_template(image, olivetree)
ij = np.unravel_index(np.argmax(result), result.shape)
x, y = ij[::-1]

fig = plt.figure(figsize=(8, 3))
ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2, adjustable='box-forced')
ax3 = plt.subplot(1, 3, 3, sharex=ax2, sharey=ax2, adjustable='box-forced')

ax1.imshow(olivetree, cmap=plt.cm.gray)
ax1.set_axis_off()
ax1.set_title('template')

ax2.imshow(image, cmap=plt.cm.gray)
ax2.set_axis_off()
ax2.set_title('imagen')

#Highlight matched region
htree, wtree = olivetree.shape
rect = plt.Rectangle((x, y), wtree, htree, edgecolor='r', facecolor='none')
ax2.add_patch(rect)

ax3.imshow(result)
ax3.set_axis_off()
ax3.set_title('`match_template`\nresult')

# Highlight matched region
ax3.autoscale(False)
ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none', markersize=10)

plt.show()

#Closer look at the match template
plt.imshow(result)
plt.figure(figsize = (10,10))

#Filter results to match similar trees
resultsfiltered = np.where(result>0.85)
resultmaximum = np.where(result>0.99)

#Show the interpreted results plus the best match
for punto in range(np.shape(resultsfiltered)[1]):
    plt.plot(resultsfiltered[1][punto], resultsfiltered[0][punto], 'o', 
         markeredgecolor='r', markerfacecolor='none', markersize=10)
    
plt.plot(resultmaximum[1][0], resultmaximum[0][0], 'o', 
         markeredgecolor='r', markerfacecolor='r', markersize=15)

plt.imshow(ImagenTotal[10:-10,10:-10,:])
plt.figure(figsize=(10,10))

