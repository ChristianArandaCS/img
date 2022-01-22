## img_resizer v1.0
## This algorith will resize all images in a directory
##########################################################################
##########################################################################


#import libraries
import os
import PIL
import shutil
from PIL import Image

# sets up dir's
img_loc = r"Y:\Christian\resize_imgs\01.19.2022\original"
folder_path = r"Y:\Christian\resize_imgs\01.19.2022"
script_path = os.path.abspath(os.curdir)


# get all file names from img source location
img_list = os.listdir(img_loc)
## GUI testing space

from tkinter import *
import os
from tkinter import filedialog
import PIL
import shutil
from PIL import Image

# creating main root
root = Tk()

#use to hide tkinter window
#root.withdraw()

#creating function
def selectingFolder():
    # file_path = filedialog.askdirectory()
    # sets up dir's
    img_loc = filedialog.askdirectory()
    folder_path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
    # folder_path = r"Y:\Christian\resize_imgs\01.19.2022"
    script_path = os.path.abspath(os.curdir)


    # get all file names from img source location
    img_list = os.listdir(img_loc)

    # img_list.remove('Thumbs.db')

    # copies all files from the img source to the script path
    for fname in img_list:
        shutil.copy2(os.path.join(img_loc,fname),script_path)


    # Resizes imgs
    for fname in img_list:

        fixed_height = 500
        image = Image.open(fname)
        height_percent = (fixed_height / float(image.size[1]))
        width_size = int((float(image.size[0]) * float(height_percent)))
        image = image.resize((width_size, fixed_height), PIL.Image.NEAREST)
        image.save(fname)


    # create a folder in the image file location
    labeled_imgs = os.path.join(img_loc,"resized_imgs")
    os.mkdir(labeled_imgs)

    # move all labeled images from script dir to img dir
    for fname in img_list:
        shutil.move(os.path.join(script_path,fname), labeled_imgs)


######################################################################
#creating widgets
msgBox = Label(root, text = 'Select folder location')
scriptBtn = Button(root, text="Select",command=selectingFolder)

# placing widgets
msgBox.pack()
scriptBtn.pack()

# main root
root.mainloop()
img_list.remove('Thumbs.db')

# copies all files from the img source to the script path
for fname in img_list:
    shutil.copy2(os.path.join(img_loc,fname),script_path)


# Resizes imgs
for fname in img_list:
    
    fixed_height = 500
    image = Image.open(fname)
    height_percent = (fixed_height / float(image.size[1]))
    width_size = int((float(image.size[0]) * float(height_percent)))
    image = image.resize((width_size, fixed_height), PIL.Image.NEAREST)
    image.save(fname)


# create a folder in the image file location
labeled_imgs = os.path.join(folder_path,"resized_imgs")
os.mkdir(labeled_imgs)

# move all labeled images from script dir to img dir
for fname in img_list:
    shutil.move(os.path.join(script_path,fname), labeled_imgs)



##########################################################################
##########################################################################

### "A DECISION FOR SOMETHING IS A DECISION AGAINST SOMETHING ELSE"
### sneakyfoo