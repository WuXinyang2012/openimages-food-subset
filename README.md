Open Images dataset V4 is a dataset of ~9 million images that have been annotated with image-level labels and object bounding boxes. The training set of V4 contains 14.6M bounding boxes for 600 object classes on 1.74M images.    

In our Smartkitchen project, we only need the images of food category and its sub categories. This repository stores the script for downloading only needed image subsets from the whole dataset.   

Usage:  

For using the downloading tools, you need to first set up gsutil with Google Cloud SDK and require an account access at CVDFoundation(http://www.cvdfoundation.org/datasets/open-images-dataset/signup.html).
 
The introduction for installing gsutil: https://cloud.google.com/storage/docs/gsutil_install#deb.  

Warning: On some Linux distributions, like Ubuntu LTS, another tool named gsutil, by GrandStream BudgeTone, is pre-installed. If you run this command instead of the Cloud Storage gsutil, it will likely print an error message. Notice that they are totally two different tools.  

After setting up the SDK, you can just navigate to different directories and execute the scripts. The images will be downloaded into corresponding food directory (without subclass hierachy). 

Notice: the csv files for train dataset is too huge (~ 2Gb) to upload. So you need to prepare them yourself in: https://storage.googleapis.com/openimages/web/download.html.

You can also check some other desired classes in class-descriptions-boxable.csv, and their hierachy in bbox_labels_600_hierarchy.json.
