# Flood Area Segmentation Using U-Net

## Overview

This project focuses on **flood area segmentation using a U-Net deep learning model**.

The objective is to identify flooded regions in an image by generating a pixel-level segmentation mask rather than simply classifying an image as flooded or non-flooded.

The project uses paired flood images and corresponding ground-truth masks, preprocesses them to a fixed resolution, trains a U-Net model using TensorFlow and Keras, and visualizes the predicted segmentation masks.

---

## Problem

Flood detection from images can be approached as an image classification problem, but classification only indicates whether flooding is present.

This project instead treats the problem as **image segmentation**, where the model attempts to identify the specific pixels corresponding to the flooded region.

---

## Objective

The main objectives of the project were to:

- Load flood images and their corresponding segmentation masks.
- Preprocess the images and masks into a consistent format.
- Train a U-Net model for binary image segmentation.
- Predict flooded regions from previously unseen images.
- Compare predicted masks with the ground-truth masks.
- Save the trained model for future use.

---

## Workflow

The overall workflow of the project is:

~~~text
Flood Images + Ground-Truth Masks
              |
              v
       Image-Mask Matching
              |
              v
      Resize to 256 × 256
              |
              v
       Normalize Images
              |
              v
        Train/Test Split
              |
              v
          U-Net Model
              |
              v
       Model Training
              |
              v
      Flood Mask Prediction
              |
              v
       Prediction Visualization
              |
              v
        Save Trained Model
~~~

---

## Dataset

The dataset consists of paired images and segmentation masks.

The images and masks are stored separately:

~~~text
dataset/
├── Image/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
│
└── Mask/
    ├── image1.png
    ├── image2.png
    └── ...
~~~

The project matches images and masks using their filenames.

A total of **289 image-mask pairs** were successfully loaded in the notebook.

The data was divided into:

- **231 training samples**
- **58 test samples**

using an 80/20 split.

---

## Data Preprocessing

The images and masks are resized to:

~~~text
256 × 256
~~~

The input images are represented as RGB images with three channels:

~~~text
256 × 256 × 3
~~~

The masks are single-channel images:

~~~text
256 × 256 × 1
~~~

Pixel values are normalized from the range `0-255` to `0-1`.

The dataset is then split into training and testing sets using a fixed random state of `42`.

---

## Model Architecture

The project uses a **U-Net architecture** implemented using TensorFlow and Keras.

U-Net follows an encoder-decoder structure:

~~~text
Input Image
     |
     v
Encoder
     |
     v
Bottleneck
     |
     v
Decoder
     |
     v
Segmentation Mask
~~~

The encoder progressively reduces the spatial dimensions while increasing the number of feature maps.

The decoder then restores the spatial resolution.

The model uses **skip connections** between corresponding encoder and decoder layers to retain spatial information that can be useful for accurate segmentation.

The convolutional blocks use ReLU activation, while the final output layer uses a sigmoid activation to produce a binary segmentation mask.

---

## Training

The model was compiled using:

- **Optimizer:** Adam
- **Loss Function:** Binary Cross-Entropy
- **Metric:** Accuracy

The model was trained for:

- **25 epochs**
- **Batch size:** 1

The training set contained 231 samples, while the 58 test samples were used as validation data during training.

---

## Results

The training run completed all 25 epochs.

The highest validation accuracy recorded during training was:

~~~text
Validation Accuracy: 82.05%
Epoch: 23
Validation Loss: 0.3965
~~~

At the final epoch:

~~~text
Training Accuracy:   80.03%
Validation Accuracy: 76.72%
Training Loss:       0.4068
Validation Loss:     0.4618
~~~

The notebook also generates visual comparisons between the original image, ground-truth mask and predicted mask.

> The current implementation evaluates the model using pixel-level accuracy and binary cross-entropy loss. Metrics such as IoU and Dice coefficient were not calculated in the notebook.

---

## Prediction and Visualization

After training, the model is used to generate segmentation masks for images from the test set.

The predicted output is converted into a binary mask using a threshold of `0.5`.

The results are visualized as:

~~~text
Original Image | Ground-Truth Mask | Predicted Mask
~~~

This provides a visual comparison between the actual flooded region and the region predicted by the model.

---

## Model Saving

The trained model is saved as a Keras HDF5 model:

~~~text
flood_segmentation_model2.h5
~~~

The saved model can be loaded later without retraining.

---

## Technologies Used

- Python
- TensorFlow
- Keras
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

---

## My Role

This was an individual deep learning project, so I was responsible for the complete implementation.

My work included:

- Preparing and preprocessing the dataset.
- Implementing the U-Net architecture.
- Training the segmentation model.
- Evaluating model performance.
- Generating and visualizing predictions.
- Saving and loading the trained model.
- Troubleshooting issues during development.

---

## Challenges

Some of the main challenges encountered during the project were:

### Image-Mask Handling

The input images and their corresponding masks had to be correctly matched before training.

### Segmentation Accuracy

Unlike image classification, segmentation requires the model to make predictions at the pixel level, making accurate boundary detection more challenging.

### Model Training

Training a U-Net with limited data can make it difficult for the model to generalize well to unseen images.

### Evaluation

Pixel-level accuracy alone does not fully describe the quality of a segmentation model, particularly when the flooded region represents only part of an image.

---

## Key Learnings

This project helped me understand:

- How image segmentation differs from image classification.
- How U-Net can be used for semantic segmentation.
- How encoder-decoder architectures work.
- The purpose of skip connections in U-Net.
- How image and mask pairs are prepared for segmentation.
- How to train and evaluate a segmentation model using TensorFlow and Keras.
- How to visualize model predictions.
- The practical challenges involved in training deep learning models on relatively small datasets.

---

## Limitations

The project has several limitations:

- The dataset contains a relatively small number of image-mask pairs.
- No data augmentation was implemented.
- Evaluation was primarily based on pixel-level accuracy and binary cross-entropy.
- IoU and Dice coefficient were not calculated.
- The test set was also used as validation data during training.
- The model was developed as an academic project rather than a production-ready flood detection system.

---

## Future Improvements

Possible improvements include:

- Increasing the size and diversity of the dataset.
- Adding data augmentation.
- Using IoU and Dice coefficient for evaluation.
- Introducing a separate validation dataset.
- Experimenting with different loss functions such as Dice Loss.
- Using pretrained encoder architectures.
- Comparing U-Net with other segmentation architectures.
- Developing a simple application for uploading an image and viewing the predicted flood mask.

---

## Project Structure

~~~text
flood-area-segmentation/
|
├── README.md
├── notebooks/
│   └── flood_segmentation.ipynb
├── dataset/
│   ├── Image/
│   └── Mask/
├── models/
│   └── flood_segmentation_model2.h5
└── requirements.txt
~~~

---

## Academic Context

This project was developed as an academic deep learning project focused on applying convolutional neural networks to the problem of flood area segmentation.

The project provided practical experience with image preprocessing, semantic segmentation, U-Net architecture, model training and evaluation using TensorFlow and Keras.

---

## Disclaimer

This project is an academic implementation and is not intended to be used as a production-ready flood detection or disaster-response system.

Model performance may vary depending on the characteristics, quality and type of input images.
