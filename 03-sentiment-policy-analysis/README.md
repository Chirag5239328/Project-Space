# Sentiment Analysis and Policy Opinion Analysis System

## Overview

This project is a Python-based system for analysing public opinions about a policy using sentiment analysis and several additional analytical components.

The project started from a hackathon/Datathon where I wanted to explore how textual opinions could be analysed to understand whether the overall response towards a policy was positive, neutral, or negative.

At the time of developing the project, I had not yet been formally taught Natural Language Processing (NLP). I therefore had to independently explore the concepts and libraries required to build the system.

The project uses TextBlob to analyse the polarity and subjectivity of opinions and combines this with custom sentiment classification, basic sarcasm detection, entity-based analysis, temporal analysis, parameter tuning, sensitivity analysis, and sentiment visualization.

---

## Project Details

- **Type:** Individual project
- **Field:** Natural Language Processing / Sentiment Analysis / Data Analysis
- **Primary language:** Python
- **Dataset:** 205 policy opinions
- **Main NLP library:** TextBlob
- **Data handling:** Pandas and CSV
- **Visualization:** Matplotlib

---

## Objective

The main objective was to develop a system that could analyse a collection of textual opinions and provide an overall interpretation of public sentiment towards a policy.

The system was designed to:

1. Accept and store textual opinions.
2. Preprocess the opinions.
3. Calculate sentiment polarity and subjectivity.
4. Classify opinions as positive, neutral, or negative.
5. Count the distribution of different sentiment categories.
6. Detect opinions containing an explicit reference to sarcasm.
7. Perform basic entity-based sentiment analysis.
8. Experiment with different analytical parameters and weights.
9. Perform sensitivity analysis.
10. Generate a sentiment distribution visualization.
11. Produce an overall interpretation of the policy sentiment.

---

## Dataset

The project uses a CSV file named `opinions.csv`.

The file contains a single column:

```text
Opinions
