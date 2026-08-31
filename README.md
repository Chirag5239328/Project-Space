# Project-Space
All Projects
# Chirag Chaudhary | Project Portfolio

Welcome to my project portfolio.

I am a B.Tech graduate in Data Science with a particular interest in statistics, data analysis, data visualization and the practical application of technology to solve problems.

This repository contains selected academic, self-initiated and post-graduation projects that I worked on during and after my undergraduate studies.

The projects cover areas including:

- Data Analysis
- Business Intelligence
- Machine Learning
- Natural Language Processing
- Computer Vision
- Process Automation
- Software Development
- Business Decision Systems

The projects vary considerably in their purpose and complexity. Some were academic assignments, some were projects I created independently to explore a technology or area that interested me, and some came from problems I wanted to understand or solve myself.

---

## About Me

I completed my Bachelor of Technology in Data Science from NMIMS Mukesh Patel School of Technology Management & Engineering with a CGPA of 3.76/4.00.

During my undergraduate studies, I developed a stronger interest in the areas of Data Science that involved understanding data, finding patterns and using analytical methods to support decisions. I particularly enjoyed statistics, data analysis, visualization and the mathematical side of problem-solving.

At the same time, I explored several technical areas including machine learning, NLP, computer vision, business intelligence, automation and application development.

My internships provided an opportunity to apply some of these skills in different environments, including an NGO, a mutual fund company and FedEx.

After graduation, I began working in my family business while continuing to explore technology and smaller software ideas independently. This gave me a different perspective on problem-solving. I began to understand that identifying an insight or building a technical solution is only one part of solving a business problem. The way a business operates, the people involved, existing processes and practical constraints can determine whether a technically sound solution actually creates value.

This repository is therefore not intended to represent a single specialization. Instead, it reflects my progression from learning technical concepts during my degree to experimenting with how those concepts can be applied to practical problems.

---

# Project Index

| No. | Project | Type | Main Areas |
|-----|---------|------|------------|
| 01 | [Audio Transcription & Translation Application](./01-capstone-audio-transcription-translation/) | Individual Capstone | NLP, Speech Processing, Cloud |
| 02 | [Financial Risk Assessment & Risk Rating Prediction](./02-financial-risk-assessment/) | Individual | Financial Analytics, Machine Learning |
| 03 | [Sentiment Analysis & Policy Opinion Analysis](./03-sentiment-policy-analysis/) | Individual | NLP, Data Analysis |
| 04 | [SQL Analysis](./04-SQL-analysis/) | Self-Initiated | SQL, Covid-19 |
| 05 | [Power BI Dashboard Analysis](./05-powerbi-dashboard-analysis/) | Self-Initiated | Power BI, DAX, HR Analytics, business Analytics |
| 06 | [Flood Area Segmentation Using Deep Learning](./06-flood-segmentation/) | Team Project | Computer Vision, CNN, Deep Learning |
| 07 | [Kwick Kravings](./07-kwick-kravings/) | Academic Team Project | Django, React, Web Development |
| 08 | [Config-Driven Decision Engine](./08-config-driven-decision-engine/) | Independent / Post-Graduation | Rule Engines, SaaS Concepts, Backend Systems |

---

# 01. Audio Transcription & Translation Application

**Type:** Individual Capstone Project  
**Area:** Speech Processing, NLP, Cloud Computing  
**Technologies:** Python, Streamlit, AWS, Whisper, MarianMT, Hugging Face

### Overview

This project began with a personal problem: difficulty communicating seamlessly through audio messages.

The initial idea was relatively simple: upload an audio file and generate a transcription.

As I worked on the idea, I felt that a transcription-only application would be too limited. I therefore expanded the application to include translation and cloud-based file storage so that it could potentially be used by people with different language requirements.

### What the application does

The application allows a user to upload an audio file.

The workflow then:

1. Stores the uploaded file using AWS.
2. Determines whether the audio is in English or another language.
3. Transcribes the audio using Whisper.
4. If the audio is not in English, produces both the original-language transcription and an English translation.
5. Retains the English text for subsequent processing.
6. Allows the user to translate the resulting text into a language of their choice.

### My Role

This was an individual project.

I worked on the application architecture, model integration, cloud integration and Streamlit interface.

### Challenges

One of the main challenges was achieving reliable transcription and translation accuracy using pretrained models.

The application also struggled with:

- Hindi audio
- Hinglish or mixed-language audio
- Different accents and speech patterns
- Integrating cloud storage after initially developing the application without it

The approximate accuracy I observed during testing was around 75-80%.

I tested the application using audio files collected from publicly available sources, including audio extracted from TED Talk-style videos.

### Key Learning

The project taught me that integrating pretrained models into an application is different from simply using the models individually.

I also learned about the importance of testing models against real-world data rather than assuming that good model performance in general would translate directly to every type of input.

### Project Paper

A technical paper was written based on this project as part of the academic work. It was not published.

---

# 02. Financial Risk Assessment & Risk Rating Prediction

**Type:** Individual Self-Initiated Project  
**Area:** Financial Analytics, Machine Learning  
**Technologies:** Python, Pandas, NumPy, Scikit-learn, Random Forest, XGBoost, SMOTE, Matplotlib, Seaborn

### Overview

I chose this project because I was interested in finance and wanted to explore how machine learning could be applied to financial decision-making.

The project used a dataset containing 15,000 records and 20 variables related to borrowers and their financial characteristics.

The objective was to predict a borrower's risk rating as:

- Low
- Medium
- High

### Data

The dataset contained information including:

- Income
- Credit score
- Loan amount
- Employment status
- Payment history
- Debt-to-income ratio
- Assets
- Previous defaults
- Other demographic and financial characteristics

### What I Did

The project involved:

- Exploratory data analysis
- Missing-value analysis and treatment
- Outlier analysis using the IQR method
- One-hot encoding of categorical variables
- Target encoding
- Feature standardization
- Training/testing split using stratified sampling
- Random Forest classification
- SMOTE-based class balancing
- XGBoost experimentation
- Hyperparameter tuning using GridSearchCV
- Model evaluation using accuracy, precision, recall and F1-score

### Results

The initial Random Forest model achieved approximately 60% accuracy.

However, the model was significantly better at identifying the Low-risk class than the Medium- and High-risk classes.

I therefore experimented with SMOTE and alternative modelling approaches.

The SMOTE-based Random Forest achieved approximately 54% accuracy, while the XGBoost experiment achieved approximately 51.6%.

Rather than treating the lower scores simply as a failure, the project helped me understand an important modelling problem: overall accuracy can be misleading when the target classes are imbalanced.

### Key Learning

The biggest learning from this project was understanding the importance of looking beyond a single performance metric.

A model can appear reasonably accurate while still performing poorly on the categories that may be more important from a practical decision-making perspective.

---

# 03. Sentiment Analysis & Policy Opinion Analysis System

**Type:** Individual Project  
**Area:** NLP, Sentiment Analysis, Data Analysis  
**Technologies:** Python, Pandas, TextBlob, Matplotlib

### Overview

This project originated from a hackathon in which participants were given different domains and asked to develop a project within one of them.

I chose to explore public opinion analysis and developed a system for analysing textual opinions.

At the time, I had not yet formally studied NLP, so much of the work involved independently researching the concepts required to build the system.

### What I Did

The system:

- Analysed textual opinions
- Calculated sentiment polarity
- Calculated subjectivity
- Classified opinions as positive, neutral or negative
- Stored opinions using CSV files
- Used Pandas for data handling
- Added basic sarcasm detection
- Added entity-based sentiment analysis
- Created a framework for aspect-based sentiment analysis
- Added temporal analysis
- Implemented parameter tuning
- Performed sensitivity analysis
- Created a weighted overall sentiment score
- Implemented a basic gradient-descent-based weight update mechanism
- Generated sentiment distribution visualizations
- Produced an overall interpretation of the analysed policy opinions

### Key Learning

The project introduced me to practical NLP concepts that I had not previously encountered in my coursework.

I learned how textual information can be converted into measurable features and how multiple analytical factors can be combined to produce a broader interpretation.

I also learned the difference between polarity and subjectivity and gained exposure to the limitations of simple rule-based sentiment analysis.

---

# 04. Business Analysis Dashboard

**Type:** Self-Initiated Project  
**Area:** Business Intelligence, Data Visualization  
**Technologies:** Power BI, DAX

### Overview

I created this project independently to explore Power BI and understand how it could be used to convert raw business data into interactive analysis.

The project used the publicly available Superstore dataset from Kaggle.

The dashboard contains three pages and analyses areas including:

- Sales
- Profit
- Customers
- Products
- Regions
- Categories
- Sub-categories
- Returns
- Payment modes

### What I Did

I explored:

- Data preparation
- Data modelling
- DAX
- Measures
- Calculated columns
- Interactive dashboard design
- Business-oriented data visualization
- Deriving insights from multiple dimensions of the dataset

### Key Learning

This was my first deeper exploration of Power BI.

Rather than learning the software only as part of coursework, I used the project to understand what could actually be done with the tool.

The experience later proved useful during my FedEx internship, where I used Power BI for more advanced dashboards and incorporated features such as bookmarks and navigation.

---

# 05. HR Analysis Dashboard

**Type:** Self-Initiated Project  
**Area:** HR Analytics, Business Intelligence  
**Technologies:** Power BI, DAX

### Overview

This was the first of my two self-initiated Power BI dashboard projects.

I used an HR dataset obtained from Kaggle containing information about employees, including:

- Age
- Department
- Attrition
- Education
- Job role
- Job satisfaction
- Salary
- Performance
- Work-life balance
- Years of experience
- Overtime
- Promotion history
- Other employee characteristics

### What I Did

I created an interactive HR Analysis Dashboard and used DAX calculations to derive additional information from the dataset.

The objective was to explore employee-related patterns and understand how Power BI could be used to present HR data in a business-friendly format.

### Key Learning

This project helped me understand the basic capabilities of Power BI and gave me the foundation to explore DAX and more advanced dashboard functionality in my subsequent Superstore project.

---

# 06. Flood Area Segmentation Using Deep Learning

**Type:** Team Project  
**My Role:** Flood Segmentation Component  
**Area:** Computer Vision, Deep Learning  
**Technologies:** Python, OpenCV, TensorFlow, Keras, NumPy, Pandas, Scikit-learn

### Overview

This project was part of a larger team application containing five different machine-learning components.

The overall application included areas such as:

- Image segmentation
- Image classification
- Prediction
- Text generation
- Text classification

Each member was responsible for one component.

I worked on the flood-area segmentation component.

### Objective

The objective was to use deep learning to identify flooded areas within images.

The dataset contained flood images together with corresponding segmentation masks.

### What I Did

I:

- Loaded the image and mask dataset
- Matched images with their corresponding masks
- Used OpenCV for image processing
- Resized images and masks to 256 × 256 pixels
- Normalized pixel values
- Identified and handled an image that failed to load
- Prepared 289 usable image-mask pairs
- Split the data into training and testing sets
- Built a CNN-based segmentation architecture
- Used convolutional layers
- Used max pooling
- Used upsampling
- Combined feature maps using concatenation

### Key Learning

The project helped me understand the difference between image classification and image segmentation.

Instead of predicting one label for an entire image, segmentation requires identifying the relevant region at the pixel level.

I also gained practical experience working with paired images and masks and understanding the preprocessing required before training a computer vision model.

---

# 07. Kwick Kravings

**Type:** Academic Team Project  
**Team:** 3 members  
**Area:** Web Development  
**My Role:** Django / Backend  
**Technologies:** Python, Django, React, HTML, CSS

### Overview

This was an academic project in which our team was required to develop a website using technologies including React and Django.

We decided to build a food-ordering website called Kwick Kravings.

### My Role

The project responsibilities were divided between the team members.

I was responsible for the Django/backend component.

Other members focused primarily on the React/frontend and CSS components.

### Result

We developed a functioning food-ordering website containing sections such as:

- Home
- About Us
- Addresses
- Cart
- Checkout

A payment gateway was not integrated, which would have been the logical next stage for a more complete application.

### Key Learning

The project gave me practical exposure to Django and helped me understand how a backend component fits into a larger application.

It also took place during a semester in which I was simultaneously learning several new areas, including cloud computing and machine learning, which made managing multiple technical subjects at once challenging.

---

# 08. Config-Driven Decision Engine

**Type:** Independent Post-Graduation Project  
**Area:** Business Systems, Rule Engines, SaaS Concepts  
**Technologies:** Python, Pydantic, YAML, SQLite, Pandas, Pytest

### Overview

This project is a backend decision engine designed to evaluate structured records against externally defined rules and produce deterministic decisions with full auditability.

The project was inspired by my interest in building smaller SaaS and automation tools.

After graduation, I was exploring a larger startup idea but found that working on a large problem at once created challenges across several areas. While working in my family business, I began experimenting with smaller software projects to become more comfortable with the process of building and structuring such tools.

I chose a configuration-driven decision engine because the same concept could be useful across different types of SaaS and enterprise applications.

### Core Idea

The system separates:

- Data
- Policy
- Execution
- Audit
- Reporting

Rules can therefore be modified without changing the core application logic.

### Architecture

```text
Input CSV
    ↓
Schema Validator
    ↓
Rule Loader
    ↓
Rule Engine
    ↓
Audit Logger
    ↓
Output Generator
    ↓
Summary Report
