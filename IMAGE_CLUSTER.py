# Created by github.com/RR689695/IMAGE-CLASSIFIER/new/main
import os
import shutil
from clustimage import Clustimage

input_dir = "images"
output_dir = "grouped_faces"
os.makedirs(output_dir, exist_ok=True)

# Initialize clustimage
cl = Clustimage(method='pca', embedding='resnet50')

# Fit clustering on all images in the folder
results = cl.fit_transform(input_dir)

# results['labels'] contains cluster labels for each image
for img_path, label in zip(results['filenames'], results['labels']):
    # Ensure we have a full path
    img_path = os.path.join(input_dir, str(img_path))

    person_name = f"person_{label+1}"  # cluster labels start at 0
    person_folder = os.path.join(output_dir, person_name)
    os.makedirs(person_folder, exist_ok=True)

    # Move image into its cluster folder
    filename = os.path.basename(img_path)
    shutil.move(img_path, os.path.join(person_folder, filename))

print("✅ Images grouped into folders using clustimage.")
