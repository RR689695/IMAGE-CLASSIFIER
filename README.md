# IMAGE-CLASSIFIER

A Python project for **unsupervised image grouping and classification**.  
This tool automatically scans a folder of images, extracts features, and groups them into clusters (e.g., `person_1`, `person_2`, …) using [clustimage](https://github.com/erdogant/clustimage).

---

## 🚀 Features
- Automatically detects similarity between images.
- Groups images into folders based on clusters.
- Supports multiple embeddings (ResNet50, VGG16, PCA).
- Works with large datasets (hundreds of images).
- Easy to extend for face recognition or dataset preparation.

---

## 📦 Installation

Clone the repository:
```bash
git clone https://github.com/RR689695/IMAGE-CLASSIFIER.git
cd IMAGE-CLASSIFIER

Create a virtual environment (recommended):
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Linux/Mac

Install dependencies:

bash
pip install -r requirements.txt

🛠 Usage
Place your images inside the images/ folder, then run:

bash
python group_images.py
This will:

Read all images from images/

Cluster them using clustimage

Move them into grouped_faces/ with subfolders:

Code
grouped_faces/
  person_1/
  person_2/
  person_3/
📂 Project Structure
Code
IMAGE-CLASSIFIER/
│
├── images/              # Input images
├── grouped_faces/       # Output grouped folders
├── group_images.py      # Main script
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
⚙️ Configuration
You can tweak clustering by editing group_images.py:

Change embedding model: embedding='resnet50' → 'vgg16' or 'pca'

Fix number of clusters: cl.cluster(method='kmeans', n_clusters=5)

Adjust the similarity threshold for stricter/looser grouping.

📖 Example Output
After running the script:

Code
grouped_faces/
   person_1/
       img1.jpg
       img2.jpg
   person_2/
       img3.jpg
🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License
This project is licensed under the MIT License.
