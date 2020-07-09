import imageio
import os
filenames = os.listdir('path/to/folder/')
images = []
for filename in filenames:
    images.append(imageio.imread('path/to/folder/'+filename))
    print(filename)
imageio.mimsave('path/to/folder/movie.gif', images)
    
