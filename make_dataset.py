import numpy as np
import glob
import random
import shutil
def make(image_dirs, n, out_dir):
    per_dir = n / len(image_dirs)
    count = 0
    for raw_dir in image_dirs:
        images = glob.glob(raw_dir+'/*.jpg')
        random.shuffle(images)
        chosen_images = images[:per_dir]
        for image in chosen_images:
            shutil.copy(image, out_dir+'/'+str(count)+'.jpg')
            count += 1

if __name__ == "__main__":
    image_dirs = ['data_28july_1','data_3aug_5', 'data_3aug_7',
                               'data_3aug_3', 'data_3aug_6']
    make(image_dirs, 3000,'dataset')
