# iarc7_image_labeling
Tool for Group Labeling Images

This tool utilizes Bottle to create a server which client computers can access and label images.

This repository is part of the Pitt RAS effort for IARC Mission 7.  For an overview of the IARC competition as well as the team's efforts and technical approaches, check out our [team website](http://pittras.org/projects/IARC/), and in particular the [technical postmortem post for the project](http://pittras.org/projects/iarc/2018/08/10/update-iarc-technical-postmortem.html).

### Info For Client Computers
There are no requirements on the client computer other than accessing the webpage. It is HIGHLY recommended that the client computer uses the CHROME browser. To label an image simply click on one corner of the bounding box you would like to draw and then click on the diagonal corner. You may start with whichever corner you prefer. Once all bounding boxes have been drawn click next or press the spacebar. If you wish to clear all selections, press 'c'.

### Info for Server Computer to use
1. Create your dataset using the make_dataset.py script. `make_dataset.py` should be run from a directory containing directories of your images and a directory called `dataset` which will contain the generated dataset
2. Copy contents of `dataset` to the static/raw directory
3. Make any necessary changes in the tool.py script
4. Run tool.py

Once all images are labelled, you should see the following:
1. static/dataset should now have all labelled images and the corresponding label text files
2. static/labels should now have all the label text files
3. static/dist should now have all the labelled images
4. static/raw should have no images
5. static/processing should have no images. If images are in this folder copy them to static/raw and run tool.py to label the remaining images

### tool.py
This script is the script used at the time of labeling to create the server. 
To change the server location edit the host parameter in the run function in the main. for local operation use "host=localhost"

### make_dataset.py
This script is used to create an image dataset from multiple folders of image files.
To change the amount of images in the dataset change the second parameter in the make() function in the main.
To change where the images from the dataset are drawn from, change the image_dirs array in the main.

### show_image.html
This template is the page accessed by the clients. If you wish to change the UI, make changes here




