# Flood Area Segmentation Using U-Net

A deep learning project for **flood area segmentation from images using a custom U-Net architecture built with TensorFlow and Keras**.

The objective of this project is to automatically identify and segment flooded regions in input images by generating a binary segmentation mask. The project uses paired RGB images and grayscale ground-truth masks, preprocesses them to a fixed resolution, trains a U-Net model, visualizes its predictions, and saves the trained model for later use.

---

## Table of Contents

* [Overview](#overview)
* [Problem Statement](#problem-statement)
* [Objective](#objective)
* [How It Works](#how-it-works)
* [Dataset](#dataset)
* [Data Preprocessing](#data-preprocessing)
* [Model Architecture](#model-architecture)
* [Training](#training)
* [Results](#results)
* [Prediction and Visualization](#prediction-and-visualization)
* [Model Saving and Loading](#model-saving-and-loading)
* [Technologies Used](#technologies-used)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Usage](#usage)
* [Important Notes](#important-notes)
* [Limitations](#limitations)
* [Future Improvements](#future-improvements)
* [License](#license)

---

## Overview

Flooding is a major natural hazard that can cause significant damage to infrastructure, agriculture, property, and human settlements. Identifying flooded regions quickly from images can support disaster assessment and response activities.

This project approaches flood detection as an **image segmentation problem** rather than simple image classification.

Instead of predicting only whether an image contains flooding, the model attempts to determine **which pixels belong to the flooded region**.

The project implements a U-Net-based semantic segmentation model that takes a `256 × 256 × 3` RGB image as input and produces a `256 × 256 × 1` binary mask as output.

### Input

An RGB image containing a potentially flooded area.

### Output

A binary segmentation mask indicating the predicted flooded region.

### Conceptual Workflow

```text
Input Image
     │
     ▼
Data Preprocessing
     │
     ▼
U-Net Model
     │
     ▼
Pixel-wise Prediction
     │
     ▼
Binary Flood Mask
```

---

## Problem Statement

Given an image of an area potentially affected by flooding, the goal is to automatically identify the pixels corresponding to the flooded area.

This is formulated as a **binary semantic segmentation** task:

* `0` represents background/non-flooded pixels.
* `1` represents flooded pixels.

The model learns this mapping from input images and their corresponding manually provided segmentation masks.

---

## Objective

The primary objectives of this project are:

1. Load paired flood images and segmentation masks.
2. Match images with their corresponding masks using common filenames.
3. Resize images and masks to a consistent resolution.
4. Normalize pixel values.
5. Split the dataset into training and testing sets.
6. Build a U-Net segmentation architecture from scratch.
7. Train the model using binary cross-entropy loss.
8. Monitor model performance using pixel-level accuracy and validation loss.
9. Generate segmentation masks for previously unseen test images.
10. Visually compare:

* Original image
* Ground-truth mask
* Predicted mask

11. Save the trained model for future use.

---

# How It Works

The complete workflow implemented in the notebook can be summarized as follows:

```text
                    ┌─────────────────────┐
                    │   Flood Dataset     │
                    │ Images + Masks      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Match Image & Mask  │
                    │ Using File Names    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Resize to 256×256   │
                    │ Normalize [0, 1]    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Train/Test Split    │
                    │ 80% / 20%           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       U-Net         │
                    │  Encoder-Decoder    │
                    │  + Skip Connections │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Binary Segmentation │
                    │ Mask Prediction     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Visualization       │
                    │ True vs Predicted   │
                    └─────────────────────┘
```

---

# Dataset

The notebook uses a dataset organized into two directories:

```text
Dataset/
├── Image/
│   ├── 0.jpg
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── ...
│
└── Mask/
    ├── 0.png
    ├── 1.png
    ├── 2.png
    ├── ...
```

Each image has a corresponding segmentation mask with the same filename stem.

For example:

```text
Image/2048.jpg
Mask/2048.png
```

The notebook identifies matching image-mask pairs by comparing filenames without their extensions.

### Dataset Statistics

The notebook successfully loaded:

* **289 images**
* **289 corresponding masks**
* **231 training samples**
* **58 test samples**

The 231/58 split corresponds to the 80/20 train-test split used in the notebook.

One image, `0.jpg`, failed to load during the execution shown in the notebook and was skipped by the loading function.

---

# Data Preprocessing

The preprocessing pipeline is implemented using OpenCV and NumPy.

## 1. Image-Mask Matching

The notebook first extracts filenames without their extensions:

```python
image_names = [os.path.splitext(f)[0] for f in os.listdir(image_dir)]
mask_names = [os.path.splitext(f)[0] for f in os.listdir(mask_dir)]
```

The intersection of these filenames is then used to identify valid image-mask pairs.

This ensures that an image is only loaded when a corresponding mask exists.

---

## 2. Image Loading

Input images are loaded using OpenCV:

```python
image = cv2.imread(image_path)
```

Masks are loaded as grayscale images:

```python
mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
```

Therefore:

* Input image: 3-channel image
* Segmentation mask: single-channel grayscale image

---

## 3. Resizing

All images and masks are resized to:

```text
256 × 256
```

This is controlled by:

```python
IMAGE_SIZE = 256
```

The input dimensions expected by the model are therefore:

```text
256 × 256 × 3
```

---

## 4. Normalization

Pixel values are normalized from:

```text
0 to 255
```

to:

```text
0 to 1
```

using:

```python
image = image / 255.0
mask = mask / 255.0
```

This normalization is applied to both the input images and segmentation masks.

---

## 5. Train-Test Split

The processed dataset is divided using:

```python
train_test_split(
    images,
    masks,
    test_size=0.2,
    random_state=42
)
```

The resulting split is:

```text
80% Training
20% Testing
```

With 289 successfully loaded samples:

```text
Training: 231 samples
Testing:   58 samples
```

The random seed is fixed at `42` to make the split reproducible.

---

# Model Architecture

The project uses a **U-Net-style encoder-decoder architecture** implemented from scratch using TensorFlow/Keras.

U-Net is designed for semantic segmentation by combining:

* Downsampling for learning high-level features
* Upsampling for recovering spatial resolution
* Skip connections for preserving spatial information

The model is created using:

```python
def unet_model(input_size=(256, 256, 3)):
```

---

## U-Net Structure

The architecture consists of three main sections:

1. Encoder / Downsampling path
2. Bottleneck
3. Decoder / Upsampling path

### High-Level Architecture

```text
Input
256 × 256 × 3
       │
       ▼
┌─────────────────┐
│ Conv 64         │
│ Conv 64         │
└────────┬────────┘
         │
         ├──────────────────────────────┐
         ▼                              │
    Max Pooling                         │
         │                              │
         ▼                              │
┌─────────────────┐                     │
│ Conv 128        │                     │
│ Conv 128        │                     │
└────────┬────────┘                     │
         │                              │
         ├──────────────────────┐       │
         ▼                      │       │
    Max Pooling                 │       │
         │                      │       │
         ▼                      │       │
┌─────────────────┐             │       │
│ Conv 256        │             │       │
│ Conv 256        │             │       │
└────────┬────────┘             │       │
         │                      │       │
         ├──────────────┐       │       │
         ▼              │       │       │
    Max Pooling         │       │       │
         │              │       │       │
         ▼              │       │       │
┌─────────────────┐     │       │       │
│ Conv 512        │     │       │       │
│ Conv 512        │     │       │       │
└────────┬────────┘     │       │       │
         │              │       │       │
         ▼              │       │       │
    Max Pooling         │       │       │
         │              │       │       │
         ▼              │       │       │
┌──────────────────────────────┐
│        Bottleneck            │
│        Conv 1024             │
│        Conv 1024             │
└──────────────┬───────────────┘
               │
               ▼
          UpSampling
               │
          + Skip Connection
               │
               ▼
          Conv 512
               │
               ▼
          UpSampling
               │
          + Skip Connection
               │
               ▼
          Conv 256
               │
               ▼
          UpSampling
               │
          + Skip Connection
               │
               ▼
          Conv 128
               │
               ▼
          UpSampling
               │
          + Skip Connection
               │
               ▼
           Conv 64
               │
               ▼
        1 × 1 Conv + Sigmoid
               │
               ▼
      256 × 256 × 1 Mask
```

---

# Encoder

The encoder progressively reduces the spatial dimensions while increasing the number of feature channels.

The convolution blocks use:

```python
Conv2D(..., activation='relu', padding='same')
```

The encoder contains four downsampling stages.

### Stage 1

```text
Conv2D: 64 filters
Conv2D: 64 filters
MaxPooling2D
```

### Stage 2

```text
Conv2D: 128 filters
Conv2D: 128 filters
MaxPooling2D
```

### Stage 3

```text
Conv2D: 256 filters
Conv2D: 256 filters
MaxPooling2D
```

### Stage 4

```text
Conv2D: 512 filters
Conv2D: 512 filters
MaxPooling2D
```

---

# Bottleneck

At the deepest point of the network, the model uses:

```text
Conv2D: 1024 filters
Conv2D: 1024 filters
```

This section captures high-level features from the input image before the decoder begins reconstructing the segmentation mask.

---

# Decoder

The decoder progressively restores the original spatial resolution.

Each decoder stage performs:

1. Upsampling
2. Concatenation with the corresponding encoder feature map
3. Two convolution layers

The decoder consists of the following feature transitions:

```text
1024 → 512
512  → 256
256  → 128
128  → 64
```

---

# Skip Connections

One of the defining characteristics of U-Net is the use of skip connections.

The decoder receives feature maps from corresponding encoder stages:

```python
u6 = Concatenate()([u6, c4])
u7 = Concatenate()([u7, c3])
u8 = Concatenate()([u8, c2])
u9 = Concatenate()([u9, c1])
```

These connections allow spatial information captured during the encoder stage to be reused during reconstruction of the segmentation mask.

This helps the network preserve spatial details while producing the final pixel-level segmentation.

---

# Output Layer

The final layer is:

```python
outputs = Conv2D(
    1,
    (1, 1),
    activation='sigmoid'
)(c9)
```

The model therefore produces a single-channel output:

```text
256 × 256 × 1
```

The sigmoid activation produces a value between `0` and `1` for each pixel.

During visualization, the predicted output is converted into a binary mask using a threshold of `0.5`:

```python
predicted_mask = (predicted_mask > 0.5).astype(np.uint8)
```

Therefore:

```text
Prediction > 0.5 → 1
Prediction ≤ 0.5 → 0
```

---

# Model Compilation

The model is compiled using the Adam optimizer:

```python
model.compile(
    optimizer=Adam(),
    loss='binary_crossentropy',
    metrics=['accuracy']
)
```

### Configuration

| Component         | Configuration        |
| ----------------- | -------------------- |
| Architecture      | U-Net                |
| Input Size        | 256 × 256 × 3        |
| Output Size       | 256 × 256 × 1        |
| Optimizer         | Adam                 |
| Loss              | Binary Cross-Entropy |
| Metric            | Accuracy             |
| Output Activation | Sigmoid              |

---

# Training

The model is trained using:

```python
history = model.fit(
    X_train,
    y_train,
    validation_data=(X_test, y_test),
    epochs=25,
    batch_size=1
)
```

### Training Configuration

```text
Epochs:              25
Batch Size:          1
Training Samples:    231
Validation Samples:   58
```

The notebook also contains a fallback mechanism that retries training with a batch size of `8` if a `ValueError` occurs with the initial batch size.

---

# Results

The recorded training run completed all 25 epochs.

The best validation accuracy visible in the notebook occurred at:

```text
Epoch: 23
Validation Accuracy: 0.8205
Validation Loss:     0.3965
```

The final epoch produced:

```text
Training Loss:       0.4068
Training Accuracy:   0.8003

Validation Loss:     0.4618
Validation Accuracy: 0.7672
```

Selected training results:

| Epoch | Training Loss | Training Accuracy | Validation Loss | Validation Accuracy |
| ----: | ------------: | ----------------: | --------------: | ------------------: |
|     1 |        0.6606 |            0.6581 |          0.5208 |              0.7590 |
|     5 |        0.5171 |            0.7312 |          0.4923 |              0.7607 |
|    10 |        0.4852 |            0.7632 |          0.4604 |              0.7804 |
|    15 |        0.4546 |            0.7699 |          0.5310 |              0.6976 |
|    20 |        0.4325 |            0.7859 |          0.4528 |              0.7882 |
|    23 |        0.4265 |            0.7945 |          0.3965 |              0.8205 |
|    25 |        0.4068 |            0.8003 |          0.4618 |              0.7672 |

The highest recorded validation accuracy was **82.05% at epoch 23**.

> **Note:** The notebook reports pixel-level accuracy and binary cross-entropy loss. It does not calculate segmentation-specific metrics such as IoU/Jaccard, Dice coefficient, precision, recall, or F1 score. Therefore, those metrics are not reported here.

---

# Prediction and Visualization

After training, the notebook evaluates predictions visually using test images.

The prediction function is:

```python
def display_predictions(model, X_test, y_test, index):
```

For each selected test image, the model generates a segmentation mask:

```python
predicted_mask = model.predict(
    np.expand_dims(X_test[index], axis=0)
)
```

The predicted probability map is converted into a binary mask using a threshold of `0.5`:

```python
predicted_mask = (predicted_mask > 0.5).astype(np.uint8)
```

The notebook displays three images side-by-side:

```text
┌──────────────────┬──────────────────┬──────────────────┐
│  Original Image  │   True Mask      │ Predicted Mask   │
└──────────────────┴──────────────────┴──────────────────┘
```

Predictions are visualized for the first five test images.

This provides a qualitative comparison between the ground-truth segmentation and the model's predicted segmentation.

---

# Model Saving

After training, the model is saved using Keras:

```python
model.save('flood_segmentation_model2.h5')
```

This creates an HDF5 model file containing the trained model.

The saved model can subsequently be loaded without retraining.

---

# Model Loading

The notebook also demonstrates loading a previously saved model:

```python
model = tf.keras.models.load_model(model_path)
```

After loading, the notebook confirms that the model was loaded successfully.

The loaded model can then be used for inference on new images.

---

# Technologies Used

The project is implemented in Python using the following libraries:

| Technology   | Purpose                                     |
| ------------ | ------------------------------------------- |
| Python       | Core programming language                   |
| TensorFlow   | Deep learning framework                     |
| Keras        | Neural network/model construction           |
| OpenCV       | Image and mask loading and resizing         |
| NumPy        | Numerical operations and array manipulation |
| Pandas       | Data manipulation                           |
| Matplotlib   | Visualization                               |
| Scikit-learn | Train-test splitting                        |

---

# Project Structure

A clean version of the repository can be organized as:

```text
flood-area-segmentation/
│
├── dataset/
│   ├── Image/
│   │   ├── 0.jpg
│   │   ├── 1.jpg
│   │   └── ...
│   │
│   └── Mask/
│       ├── 0.png
│       ├── 1.png
│       └── ...
│
├── notebooks/
│   └── flood_segmentation.ipynb
│
├── models/
│   └── flood_segmentation_model2.h5
│
├── requirements.txt
├── README.md
└── .gitignore
```

### Directory Descriptions

#### `dataset/`

Contains the input images and corresponding ground-truth segmentation masks.

#### `notebooks/`

Contains the Jupyter Notebook implementing the complete segmentation workflow.

#### `models/`

Contains the trained Keras model.

#### `requirements.txt`

Contains the Python dependencies required to reproduce the project.

#### `README.md`

Project documentation.

#### `.gitignore`

Specifies files and directories that should not be committed to Git.

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

Replace `<your-username>` and `<your-repository>` with your GitHub username and repository name.

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

Install the required Python packages:

```bash
pip install numpy pandas matplotlib opencv-python scikit-learn tensorflow
```

Alternatively, create a `requirements.txt` file containing:

```text
numpy
pandas
matplotlib
opencv-python
scikit-learn
tensorflow
```

Then install:

```bash
pip install -r requirements.txt
```

---

# Dataset Directory Configuration

The original notebook uses a local Windows path similar to:

```python
IMAGE_DIR = r"C:\Users\jash1\OneDrive\Desktop\sem 7\dl_app\image_segmentation\archive (12)\Image"
MASK_DIR = r"C:\Users\jash1\OneDrive\Desktop\sem 7\dl_app\image_segmentation\archive (12)\Mask"
```

This path will **not work on another computer**.

For the GitHub version of the project, update these paths to match the location of your dataset.

For example:

```python
IMAGE_DIR = "./dataset/Image"
MASK_DIR = "./dataset/Mask"
```

If the dataset is not included in the repository, users should obtain the dataset separately and place it in the expected directory structure.

---

# Usage

## Running the Notebook

Launch Jupyter Notebook:

```bash
jupyter notebook
```

or:

```bash
jupyter lab
```

Open:

```text
notebooks/flood_segmentation.ipynb
```

Then execute the notebook cells sequentially.

---

## Training the Model

The notebook performs the following operations:

```text
1. Import libraries
2. Configure dataset paths
3. Load image-mask pairs
4. Resize images and masks
5. Normalize pixel values
6. Split data into training and testing sets
7. Create U-Net
8. Compile model
9. Train for 25 epochs
10. Generate test predictions
11. Visualize predictions
12. Save trained model
```

---

# Using the Trained Model

Once the model has been trained and saved, it can be loaded using:

```python
import tensorflow as tf

model = tf.keras.models.load_model(
    "flood_segmentation_model2.h5"
)
```

For a new image, it should first be processed in the same way as the training data.

Example preprocessing:

```python
import cv2
import numpy as np

IMAGE_SIZE = 256

image = cv2.imread("path/to/image.jpg")

image = cv2.resize(
    image,
    (IMAGE_SIZE, IMAGE_SIZE)
)

image = image / 255.0

input_image = np.expand_dims(image, axis=0)

prediction = model.predict(input_image)

binary_mask = (
    prediction[0] > 0.5
).astype(np.uint8)
```

The resulting `binary_mask` represents the predicted segmentation.

---

# Important Notes

## Image Format

The notebook expects input images to use the `.jpg` extension:

```python
image_path = os.path.join(image_dir, file_name + ".jpg")
```

## Mask Format

The notebook expects segmentation masks to use the `.png` extension:

```python
mask_path = os.path.join(mask_dir, file_name + ".png")
```

If your dataset uses different extensions, these lines need to be modified.

## Matching Filenames

Each image and its corresponding mask must have the same filename stem.

For example:

```text
Image/2048.jpg
Mask/2048.png
```

The extension can differ, but the filename itself must match.

## Color Space

Images are loaded using OpenCV's default image-loading behavior.

The notebook does not explicitly convert the images from OpenCV's BGR representation to RGB before training.

---

# Key Implementation Details

## Input Resolution

```text
256 × 256 × 3
```

## Output Resolution

```text
256 × 256 × 1
```

## Segmentation Type

```text
Binary Semantic Segmentation
```

## Hidden-Layer Activation

```text
ReLU
```

## Output Activation

```text
Sigmoid
```

## Loss Function

```text
Binary Cross-Entropy
```

## Optimizer

```text
Adam
```

## Training Epochs

```text
25
```

## Batch Size

```text
1
```

## Train-Test Split

```text
80% Training
20% Testing
```

## Prediction Threshold

```text
0.5
```

---

# Limitations

This implementation is a baseline U-Net segmentation project and has several limitations.

### 1. Small Dataset

Only 289 image-mask pairs were successfully loaded in the notebook, with 231 used for training and 58 used for testing.

A larger and more diverse dataset would provide a stronger basis for evaluating generalization.

### 2. No Data Augmentation

The notebook does not implement augmentation techniques such as:

* Rotation
* Horizontal flipping
* Vertical flipping
* Random cropping
* Zooming
* Brightness adjustment
* Contrast adjustment

Adding augmentation could improve the model's ability to generalize to different flood scenes.

### 3. Limited Evaluation Metrics

The notebook evaluates the model using:

* Binary cross-entropy loss
* Pixel-level accuracy

However, segmentation problems are commonly evaluated using additional metrics such as:

* Intersection over Union (IoU)
* Dice coefficient
* Precision
* Recall
* F1 score

These metrics are not implemented in the current notebook.

### 4. Test Set Used as Validation Data

The notebook uses:

```python
validation_data=(X_test, y_test)
```

during model training.

Therefore, the test set is also used to monitor validation performance during training.

For a more rigorous machine learning evaluation, the dataset should ideally be divided into:

```text
Training Set
Validation Set
Test Set
```

The test set should remain completely unseen until final evaluation.

### 5. No Early Stopping

The model is trained for a fixed 25 epochs.

No early stopping callback is used to automatically stop training when validation performance stops improving.

### 6. No Model Checkpointing

The notebook saves the model after training but does not automatically save the best-performing epoch based on validation loss or another segmentation metric.

### 7. Fixed Image Size

All images are resized directly to `256 × 256`.

This provides a consistent input size but may alter the original image aspect ratio and reduce some spatial detail.

### 8. Hard-Coded Dataset Paths

The original notebook contains a machine-specific Windows path.

This must be changed before running the project on another computer.

### 9. No Deployment Interface

The notebook demonstrates training, visualization, saving, and loading the model, but does not currently provide a web or API interface for uploading an image and receiving a segmentation result.

---

# Future Improvements

The project can be extended in several ways.

## 1. Add Data Augmentation

Introduce augmentation using TensorFlow/Keras or another image augmentation pipeline.

Potential transformations include:

```text
Horizontal Flip
Vertical Flip
Rotation
Zoom
Translation
Brightness Adjustment
Contrast Adjustment
```

---

## 2. Add Dice Loss

Flood segmentation can contain significant class imbalance between flooded and non-flooded pixels.

Dice-based losses can be explored alongside binary cross-entropy.

A combined loss could also be investigated:

```text
Combined Loss = Binary Cross-Entropy + Dice Loss
```

---

## 3. Add Segmentation Metrics

Future evaluation should include:

```text
IoU / Jaccard Index
Dice Coefficient
Precision
Recall
F1 Score
```

This would provide a more informative evaluation of segmentation quality than pixel accuracy alone.

---

## 4. Create a Proper Validation Split

Instead of using the test set as validation data, the dataset could be divided into:

```text
Training
Validation
Testing
```

For example:

```text
70% Training
15% Validation
15% Testing
```

The final test set should only be evaluated after model development is complete.

---

## 5. Use Model Checkpointing

The best model can be saved automatically based on validation performance.

For example:

```python
ModelCheckpoint(
    "best_model.h5",
    monitor="val_loss",
    save_best_only=True
)
```

---

## 6. Experiment With Modern Segmentation Architectures

The baseline U-Net can be compared against architectures such as:

```text
U-Net++
Attention U-Net
DeepLabV3+
FCN
SegNet
SegFormer
```

Transfer learning using pretrained encoders could also be explored.

---

## 7. Improve Inference

A dedicated inference script could allow users to provide an image and automatically generate:

```text
Original Image
Predicted Flood Mask
Segmentation Overlay
Flooded Area Visualization
```

---

## 8. Build a Web Application

The trained model could be integrated into an application using frameworks such as:

```text
Streamlit
FastAPI
Flask
```

A possible workflow would be:

```text
Upload Flood Image
       │
       ▼
Preprocess Image
       │
       ▼
Load Trained U-Net
       │
       ▼
Generate Mask
       │
       ▼
Display Segmentation
```

---

# Reproducibility

To reproduce the experiment:

1. Install the required dependencies.
2. Obtain the image and mask dataset.
3. Organize the dataset into `Image` and `Mask` directories.
4. Ensure corresponding images and masks share the same filename.
5. Update `IMAGE_DIR` and `MASK_DIR`.
6. Set the image size to `256`.
7. Run the notebook.
8. Allow the dataset to be loaded and split.
9. Train the U-Net for 25 epochs.
10. Review the training metrics.
11. Generate predictions on test images.
12. Save the trained model.

The notebook uses:

```python
random_state=42
```

for the train-test split to make the dataset partition reproducible.

---

# Example Output

The notebook generates qualitative results consisting of:

```text
Original Image | Ground Truth Mask | Predicted Mask
```

These visualizations allow direct comparison between the actual flood segmentation and the segmentation generated by the trained U-Net model.

If you add screenshots of these results to the repository, they can be displayed here using:

```markdown
![Flood Segmentation Results](assets/results.png)
```

---

# What This Project Demonstrates

This project demonstrates an end-to-end deep learning workflow for image segmentation:

* Image dataset loading
* Image-mask pairing
* Image preprocessing
* Image normalization
* Train-test splitting
* Custom CNN architecture design
* U-Net encoder-decoder architecture
* Skip connections
* Binary semantic segmentation
* Model training
* Validation monitoring
* Segmentation prediction
* Prediction visualization
* Model saving
* Model loading for inference

---

# Conclusion

This project implements a complete baseline pipeline for **flood area segmentation using a custom U-Net architecture**.

The model learns from paired flood images and corresponding segmentation masks and produces a pixel-level prediction of flooded regions.

Using 289 successfully loaded image-mask pairs, the implementation resizes the data to `256 × 256`, trains a U-Net for 25 epochs using Adam and binary cross-entropy, and generates binary segmentation masks for test images.

The recorded training run achieved a maximum validation accuracy of **82.05% at epoch 23**. However, because the notebook does not calculate IoU, Dice, or other segmentation-specific metrics, the reported accuracy should be interpreted as pixel-level accuracy rather than a complete measure of segmentation quality.

The project provides a foundation that can be extended through data augmentation, improved loss functions, stronger evaluation methods, pretrained architectures, and deployment through a web application or API.

---

# License

This project is intended for educational and research purposes.

If the dataset used in this project has a separate license or usage restrictions, those terms should be followed independently of this repository's code license.

---

# Author

**Chirag Chaudhary**

GitHub: `https://github.com/<your-username>`

---

# Acknowledgements

This project was developed as a deep learning image segmentation project focused on identifying flooded areas from images using a U-Net architecture implemented with TensorFlow and Keras.
