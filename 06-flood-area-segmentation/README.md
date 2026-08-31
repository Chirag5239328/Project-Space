````markdown
# Flood Area Segmentation Using Deep Learning

## Project Overview

This project focuses on identifying and segmenting flood-affected areas in images using a convolutional neural network (CNN) based image segmentation model.

The project was developed as one component of a larger team-based Streamlit application created during the 7th semester of my B.Tech in Data Science. The overall application combined multiple machine learning and deep learning tasks, including image segmentation, image classification, prediction, text generation and text classification. Each member of the five-person team was responsible for one component.

I was responsible for developing the flood area segmentation component.

The objective was to train a model that could take a flood-related image and generate a pixel-level segmentation mask indicating the areas identified as flood-affected.

---

## Project Details

| Attribute | Details |
|-----------|---------|
| Project Name | Flood Area Segmentation Using Deep Learning |
| Project Type | Academic Team Project |
| Semester | 7th Semester |
| Team Size | 5 members |
| My Role | Developed the Flood Area Segmentation Component |
| Primary Area | Computer Vision and Deep Learning |
| Programming Language | Python |
| Deep Learning Framework | TensorFlow / Keras |
| Interface | Streamlit |
| Dataset | Flood Images with Corresponding Segmentation Masks |
| Image Size | 256 × 256 pixels |
| Usable Image-Mask Pairs | 289 |
| Train/Test Split | 80:20 |

---

## Problem Statement

Flood-related images can contain large and complex affected regions, making it useful to identify not only whether flooding is present but also where the affected areas are located.

A conventional image classification model could classify an image as containing flooding, but it would not indicate the exact region affected by the flood.

This project therefore approached the problem as an **image segmentation** task, where the model learns to produce a mask corresponding to the flood-affected region of an input image.

---

## Objective

The main objectives of the project were to:

- Load a dataset containing flood images and their corresponding segmentation masks.
- Match each image with its corresponding mask.
- Preprocess the images and masks into a consistent format.
- Resize the data to a fixed 256 × 256 resolution.
- Normalize pixel values for model training.
- Split the prepared data into training and testing sets.
- Develop a U-Net-style convolutional neural network for image segmentation.
- Train the model to generate segmentation masks.
- Compare predicted masks with the corresponding true masks.
- Save and reload the trained model for later use.

---

## Dataset

The project used a dataset containing two corresponding sets of files:

```text
Image/
Mask/
````

The image directory contained the input flood images, while the mask directory contained the corresponding grayscale segmentation masks.

The image and mask filenames were used to determine which files belonged together.

The project specifically searched for common filenames between the two directories and used only image-mask pairs for which both files were available.

After loading and validating the data, **289 usable image-mask pairs** were prepared for the project.

---

## Data Preprocessing

### Image and Mask Matching

The project first extracted filenames from both the image and mask directories.

The filenames were compared after removing their extensions, and only files present in both directories were considered.

For each common filename:

* The input image was loaded as a colour image.
* The corresponding mask was loaded as a grayscale image.
* Failed image or mask loads were detected and excluded.
* Both were resized to 256 × 256 pixels.

This ensured that each training example consisted of a correctly matched input image and target mask.

### Image Resizing

All images and masks were resized to:

```text
256 × 256 pixels
```

The model therefore received inputs with a consistent spatial resolution.

### Normalization

Pixel values were normalized by dividing them by 255.

This converted the values to approximately:

```text
0 to 1
```

The same normalization approach was applied to the images and masks.

### Data Validation

The notebook included checks to identify whether images or masks failed to load correctly.

It also printed the number of successfully loaded images and masks to verify that the dataset had been prepared correctly.

---

## Train/Test Split

The prepared image-mask pairs were divided into training and testing datasets using an 80:20 split.

```text
80% → Training Data
20% → Testing Data
```

A fixed random state was used so that the split could be reproduced.

The training data was used to train the segmentation model, while the test data was used for generating predictions and comparing the predicted masks against the actual masks.

---

## Model Architecture

The project implemented a **U-Net-style convolutional neural network** using TensorFlow and Keras.

The architecture follows an encoder-decoder structure.

### Encoder / Downsampling Path

The downsampling section progressively extracts higher-level features from the input image.

It consists of convolutional blocks followed by max-pooling operations.

The convolutional blocks use:

* `Conv2D`
* ReLU activation
* Same padding

The number of filters increases through the encoder:

```text
64
128
256
512
```

This allows the network to progressively learn more complex representations from the image.

### Bottleneck

At the deepest part of the network, the model uses convolutional layers with:

```text
1024 filters
```

The bottleneck represents the compressed feature representation of the input image.

### Decoder / Upsampling Path

The decoder progressively increases the spatial resolution of the feature representation.

The project uses:

* `UpSampling2D`
* `Concatenate`
* `Conv2D`

The upsampled feature maps are concatenated with corresponding feature maps from the encoder.

This allows the decoder to recover spatial information that is important for pixel-level segmentation.

The decoder progressively reduces the number of filters:

```text
512
256
128
64
```

### Output Layer

The final layer uses a 1 × 1 convolution with a single output channel and sigmoid activation.

The resulting output represents the predicted segmentation mask.

---

## Model Structure

The overall architecture can be represented as:

```text
Input Image
    |
    v
Convolution Block - 64 filters
    |
    v
Max Pooling
    |
    v
Convolution Block - 128 filters
    |
    v
Max Pooling
    |
    v
Convolution Block - 256 filters
    |
    v
Max Pooling
    |
    v
Convolution Block - 512 filters
    |
    v
Max Pooling
    |
    v
Bottleneck - 1024 filters
    |
    v
Upsampling + Skip Connection
    |
    v
Convolution Block - 512 filters
    |
    v
Upsampling + Skip Connection
    |
    v
Convolution Block - 256 filters
    |
    v
Upsampling + Skip Connection
    |
    v
Convolution Block - 128 filters
    |
    v
Upsampling + Skip Connection
    |
    v
Convolution Block - 64 filters
    |
    v
1 × 1 Convolution + Sigmoid
    |
    v
Predicted Flood Segmentation Mask
```

---

## Model Compilation

The segmentation model was compiled using the Adam optimizer.

The loss function used was:

```text
Binary Cross-Entropy
```

The model also tracked accuracy during training.

The training configuration used:

```text
Epochs: 25
Initial Batch Size: 1
```

The notebook also included a fallback to batch size 8 if a batch-size-related `ValueError` occurred during training.

---

## Model Training

The model was trained using the training image-mask pairs, with the test set supplied as validation data.

The training process was configured for up to 25 epochs.

Conceptually, the model learned the relationship:

```text
Flood Image → Flood Segmentation Mask
```

The objective was for the predicted mask to become increasingly similar to the corresponding target mask during training.

---

## Prediction and Visualization

After training, the notebook included a prediction function for visualizing model results.

For a selected test image, the model generates a predicted segmentation mask.

The predicted output is converted into a binary mask using a threshold of:

```text
0.5
```

The notebook then displays three images side by side:

```text
Original Image | True Mask | Predicted Mask
```

Predictions were generated for the first five test images.

This provided a visual way to inspect how closely the model's predicted segmentation corresponded to the actual segmentation mask.

---

## Model Saving and Loading

The trained model was saved as an H5 file:

```text
flood_segmentation_model2.h5
```

The notebook also included functionality for loading a saved TensorFlow/Keras segmentation model from an H5 file.

This allows the trained model to be reused without having to retrain the network from the beginning.

---

## Technologies and Software

### Programming Language

* Python

### Deep Learning

* TensorFlow
* Keras
* Convolutional Neural Networks
* U-Net-style architecture

### Image Processing

* OpenCV

### Data Processing

* NumPy
* Pandas
* Scikit-learn

### Visualization

* Matplotlib

### Development Environment

* Jupyter Notebook
* Kaggle

### Application Framework

* Streamlit

---

## Python Libraries Used

The notebook imports and uses the following libraries:

```text
os
cv2
numpy
matplotlib
sklearn
tensorflow
pandas
```

The TensorFlow/Keras implementation specifically uses:

```text
Conv2D
MaxPooling2D
UpSampling2D
Concatenate
Input
Model
Adam
```

---

## My Contribution

This was a five-member team project in which different members developed different machine-learning components that were intended to be integrated into a single Streamlit application.

My responsibility was the **flood area segmentation component**.

I worked on:

* Understanding the image segmentation problem.
* Preparing the flood-image dataset.
* Matching images with their corresponding segmentation masks.
* Loading images and masks using OpenCV.
* Handling files that failed to load.
* Resizing images and masks to 256 × 256 pixels.
* Normalizing image and mask values.
* Preparing the training and testing datasets.
* Designing and implementing the U-Net-style architecture.
* Implementing convolutional layers and max-pooling layers.
* Implementing the bottleneck of the network.
* Implementing upsampling and skip connections.
* Compiling the model using Adam and binary cross-entropy.
* Training the segmentation model.
* Generating predictions on test images.
* Visualizing original images, true masks and predicted masks.
* Saving and loading the trained model.

---

## Key Concepts Learned

### Image Classification vs Image Segmentation

One of the main concepts I learned through this project was the difference between classification and segmentation.

Classification attempts to assign a label to an entire image.

For example:

```text
Image → Flood
```

Segmentation instead attempts to identify the relevant pixels within an image:

```text
Image → Pixel-Level Flood Mask
```

This makes segmentation more appropriate when the location and extent of the affected region are important.

### Working With Paired Image Data

The project provided practical experience with datasets where each input image has a corresponding target mask.

I learned that maintaining the correct relationship between the image and its mask is critical because the mask represents the expected output for that particular image.

### Image Preprocessing

I learned how image dimensions and pixel values need to be standardized before being supplied to a deep-learning model.

This included:

* Resizing images.
* Resizing masks.
* Normalizing pixel values.
* Converting masks into grayscale.
* Checking for invalid image files.

### CNN-Based Feature Extraction

The project provided practical exposure to how convolutional layers can extract increasingly complex visual features from images.

I also learned how pooling operations reduce spatial dimensions while allowing the network to learn higher-level representations.

### Encoder-Decoder Architecture

The project helped me understand the basic idea behind encoder-decoder segmentation architectures.

The encoder extracts features while progressively reducing spatial resolution, while the decoder reconstructs the segmentation output.

### Skip Connections

The use of concatenation between encoder and decoder feature maps helped me understand why segmentation architectures need to preserve spatial information.

Features extracted at earlier stages can provide useful location information when reconstructing the final mask.

---

## Challenges

### 1. Correctly Matching Images and Masks

The most important preprocessing challenge was ensuring that every image was paired with its correct segmentation mask.

Since the model learns from image-mask pairs, incorrect matching would result in incorrect training targets.

### 2. Handling Image Loading Errors

The dataset contained at least one file that could not be loaded successfully.

The preprocessing code therefore included checks for failed image and mask loading and excluded invalid pairs.

### 3. Working With Segmentation Data

Working with segmentation masks required different preprocessing considerations compared with ordinary tabular or classification datasets.

Both the input image and target mask had to be resized consistently and prepared in a format suitable for the network.

### 4. Understanding a More Complex Neural Network Architecture

The U-Net-style architecture was more complex than a basic CNN classifier because it contained both downsampling and upsampling paths together with skip connections.

Understanding how the feature maps move through these different stages was an important part of the project.

### 5. Computational Requirements

The architecture uses progressively larger numbers of convolutional filters, reaching 1024 filters in the bottleneck.

Training such a network on image data requires considerably more computational resources than simpler machine-learning models.

---

## Result

The project produced a complete deep-learning pipeline for flood-image segmentation.

The pipeline was able to:

1. Load flood images and their corresponding masks.
2. Prepare 289 usable image-mask pairs.
3. Resize and normalize the data.
4. Split the dataset into training and testing sets.
5. Construct a U-Net-style CNN segmentation model.
6. Train the model for up to 25 epochs.
7. Generate segmentation predictions for test images.
8. Visualize the original image, true mask and predicted mask.
9. Save the trained model as an H5 file.
10. Reload the trained model for subsequent use.

The project gave me practical exposure to computer vision and showed me how deep-learning models can be used for pixel-level analysis rather than only assigning a single class to an image.

---

## Project Files

The project folder can contain the following structure:

```text
06-flood-segmentation/
│
├── README.md
│
├── notebook/
│   └── flood_segmentation.ipynb
│
├── model/
│   └── flood_segmentation_model2.h5
│
├── screenshots/
│   ├── original_vs_true_mask_vs_predicted_mask.png
│   └── ...
│
└── requirements.txt
```

The original dataset is not included in this repository if its size or licensing makes redistribution impractical.

---

## Limitations

The project was developed primarily as an academic learning project and has several limitations.

* The dataset contained only 289 usable image-mask pairs.
* The model was developed and tested on the available dataset rather than a large production-scale dataset.
* The project focused primarily on developing the segmentation pipeline rather than extensive model optimization.
* The notebook did not document extensive segmentation-specific evaluation metrics beyond the training accuracy.
* The quality of predictions can vary depending on the type and quality of the input image.
* The model may not generalize well to flood imagery that differs substantially from the training dataset.
* The project was one component of a larger Streamlit application rather than a standalone production deployment.

---

## Future Improvements

Potential improvements to the project could include:

* Increasing the size and diversity of the training dataset.
* Applying data augmentation to improve generalization.
* Experimenting with different U-Net architectures.
* Using pretrained encoder architectures.
* Experimenting with alternative loss functions such as Dice loss or focal loss.
* Evaluating the model using segmentation-specific metrics such as IoU and Dice coefficient.
* Performing more systematic hyperparameter tuning.
* Improving the Streamlit interface for image upload and prediction.
* Deploying the trained model as a standalone application or API.
* Testing the model on flood imagery from different geographic regions and environmental conditions.

---

## Conclusion

This project provided practical experience in applying deep learning to a computer vision problem where the objective was not simply to classify an image but to identify a specific region within it.

Through the project, I worked with paired image and mask data, implemented preprocessing pipelines, developed a U-Net-style segmentation architecture using TensorFlow/Keras, trained the model and visualized its predictions.

The project also helped me understand that successful machine-learning applications depend not only on the model architecture but also on the quality and preparation of the underlying data.

```
```
