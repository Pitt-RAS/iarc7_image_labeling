# iarc7_image_labeling
Tool for Group Labeling Images

This tool utilizes Bottle to create a server which client computers can access and label images. 

### Info For Client Computers
There are no requirements on the client computer other than accessing the webpage. It is HIGHLY recommended that the client computer uses the CHROME browser. To label an image simply click on one corner of the bounding box you would like to draw and then click on the diagonal corner. You may start with whichever corner you prefer. Once all bounding boxes have been drawn click next or press the spacebar. If you wish to clear all selections, press 'c'.

### Info for Server Computer to use
1. Create your dataset using the make_dataset.py script
2. Verify all images are in the static/raw directory
3. Make any necessary changes in the tool.py script
4. Run tool.py

### tool.py
This script is the script used at the time of labeling to create the server. 
To change the server location edit the host parameter in the run function in the main. for local operation use "host=localhost"

### make_dataset.py
This script is used to create an image dataset from multiple folders of image files.
To change the amount of images in the dataset change the second parameter in the make() function in the main.
To change where the images from the dataset are drawn from, change the image_dirs array in the main.

### show_image.html
This template is the page accessed by the clients. If you wish to change the UI, make changes here




