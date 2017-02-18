import scipy.misc

path= '/home/dan/Pictures/wood_ring.png'
image=scipy.misc.imread(path)
scipy.misc.imsave('/home/dan/Pictures/wood_ring2.png',image)
