# Sentiment Analysis and Policy Opinion Analysis System

## Overview

This project is an individual Python-based sentiment analysis and policy opinion analysis system developed to explore how textual public opinions can be analysed and converted into meaningful insights.

The project originated from a hackathon where participants were provided with different domains and were required to develop a solution within a selected domain. I chose to explore public opinion analysis and developed a system that could analyse textual opinions about a policy and determine whether the overall response was positive, neutral, or negative.

At the time of developing this project, I had not yet formally studied Natural Language Processing (NLP) in depth. As a result, a significant part of the project involved independently researching NLP concepts, understanding available libraries, experimenting with different approaches, and integrating them into a single analytical workflow.

The project goes beyond basic sentiment classification by incorporating additional experimental components such as subjectivity analysis, sarcasm detection, entity-based sentiment analysis, aspect-based sentiment analysis, temporal analysis, parameter tuning, sensitivity analysis, weighted scoring, and visualization.

## Project Details

- **Project Type:** Individual Project
- **Project Area:** Natural Language Processing, Sentiment Analysis, Data Analysis
- **Primary Language:** Python
- **Dataset:** Policy-related textual opinions
- **Dataset Size:** 205 opinions
- **Main NLP Library:** TextBlob
- **Data Handling:** Pandas and CSV
- **Visualization:** Matplotlib

## Objective

The primary objective of the project was to build a system capable of analysing a collection of textual opinions about a policy and generating an overall interpretation of public sentiment.

The system was designed to:

1. Accept textual opinions as input.
2. Store and manage the opinions using a CSV file.
3. Preprocess the textual data.
4. Calculate sentiment polarity.
5. Calculate subjectivity.
6. Classify opinions as positive, neutral, or negative.
7. Analyse the overall distribution of sentiments.
8. Detect opinions containing explicit references to sarcasm.
9. Perform basic entity-level sentiment analysis.
10. Provide a framework for aspect-based sentiment analysis.
11. Record temporal information associated with the analysis.
12. Experiment with different analytical parameters.
13. Perform sensitivity analysis on the parameters.
14. Calculate a weighted overall sentiment score.
15. Experiment with updating parameter weights.
16. Visualize the distribution of opinions.
17. Generate an overall interpretation of the policy response.

## Project Background

The initial idea was to explore whether public opinion expressed through text could be transformed into a structured analytical output.

Instead of simply identifying whether individual statements were positive or negative, I wanted to experiment with combining multiple characteristics of the opinions into a broader policy-level assessment.

This resulted in a pipeline where individual opinions were analysed first and the resulting information was then aggregated to produce an overall sentiment score and policy interpretation.

An important aspect of this project was that I was learning NLP while building the project. Concepts such as polarity, subjectivity, sarcasm detection, entity-level analysis, and aspect-based sentiment analysis were areas that I had to explore independently.

## Dataset

The project uses a CSV dataset containing policy-related opinions.

The primary column in the dataset is:

```text
Opinions
```

The dataset contains 205 individual opinions.

The opinions represent different perspectives towards a policy, including positive, negative, neutral, supportive, and critical statements.

The dataset was used to test the complete sentiment-analysis pipeline and demonstrate how individual textual responses could be aggregated into an overall policy-level interpretation.

## Data Preprocessing

Basic preprocessing was applied to the textual opinions before analysis.

The system converts opinions to lowercase so that the text can be processed consistently.

The project also allows additional opinions to be entered by the user during execution.

When a new opinion is entered, it can be appended to the existing dataset and stored back in the CSV file.

This allowed the system to function not only as a static analysis of an existing dataset but also as a simple interactive opinion collection and analysis system.

## Sentiment Analysis

The project uses TextBlob to perform the primary sentiment analysis.

For each opinion, TextBlob produces two important measures:

- **Polarity**
- **Subjectivity**

### Polarity

Polarity represents the general direction of sentiment expressed in an opinion.

The project uses the polarity score to classify each opinion into one of three categories.

The custom thresholds used were:

```text
Polarity > 0.1     → Positive
Polarity < -0.1    → Negative
Otherwise          → Neutral
```

The sentiment categories are internally represented as:

```text
Positive = 1
Neutral  = 0
Negative = -1
```

The system then counts the number of positive, neutral, and negative opinions.

### Subjectivity

Subjectivity represents how subjective or opinion-based the textual statement is.

The project calculates the average subjectivity across the analysed opinions and uses this information as another parameter in the overall policy analysis.

## Overall Polarity and Subjectivity

After analysing the individual opinions, the system calculates overall polarity and subjectivity values.

These values are then interpreted using predefined ranges.

Polarity is broadly interpreted as:

```text
Negative
Neutral
Positive
```

Subjectivity is interpreted across levels such as:

```text
Low
Medium
High
```

The purpose of this step was to convert numerical NLP outputs into information that could be understood more easily from a policy-analysis perspective.

## Sentiment Distribution

The system calculates the total number of opinions belonging to each sentiment category.

The three categories are:

- Positive
- Neutral
- Negative

This allows the project to determine whether the dataset is dominated by supportive, neutral, or opposing opinions.

The resulting distribution is also visualized using Matplotlib.

## Sarcasm Detection

The project includes a basic experimental sarcasm-detection component.

The implementation checks whether the word:

```text
sarcasm
```

appears explicitly in an opinion.

Opinions containing this term are counted as sarcastic opinions.

This is not intended to be a sophisticated machine-learning sarcasm detector. It was implemented as an initial exploration of how additional linguistic characteristics could be incorporated into the sentiment-analysis pipeline.

## Entity-Based Sentiment Analysis

The project contains an entity-based sentiment analysis component.

The purpose of this component was to explore whether sentiment could be associated with particular entities mentioned within opinions rather than treating the entire opinion as one sentiment value.

The current implementation uses predefined entities and associated sentiment information as part of the experimental framework.

This provided exposure to the idea that sentiment analysis can be performed at different levels of granularity.

## Aspect-Based Sentiment Analysis

The project also includes a framework for aspect-based sentiment analysis.

The intention was to analyse sentiment towards particular aspects of a policy rather than assigning only one sentiment to the entire opinion.

For example, a single opinion could potentially contain:

```text
Positive sentiment towards one aspect
Negative sentiment towards another aspect
```

The project includes the structure for incorporating this type of analysis, although it is not a complete production-level aspect extraction and classification system.

## Negation Handling

The project also explored the importance of negation in sentiment analysis.

A separate function was included to account for negation-related processing.

The implementation remained basic and did not develop into a complete natural-language negation-handling system.

This was part of the broader experimentation involved in understanding the limitations of basic sentiment-analysis approaches.

## Temporal Analysis

The project includes temporal analysis by recording the current date during the analysis process.

The intention was to create a foundation for analysing sentiment over time.

For example, in a larger implementation, opinions could be collected at different points in time and the resulting sentiment could be compared across different dates.

## Parameter-Based Scoring

One of the more experimental aspects of the project was the creation of a weighted scoring mechanism.

Several analytical parameters were combined to generate an overall score.

The parameters included information such as:

- Overall polarity
- Overall subjectivity
- Positive opinion count
- Negative opinion count
- Sarcasm-related information
- Entity-related information
- Other analytical parameters

Each parameter was assigned a weight.

The weighted parameters were then combined to calculate an overall sentiment/policy score.

The purpose was to experiment with how multiple analytical signals could be combined rather than relying solely on the raw polarity score generated by TextBlob.

## Parameter Tuning

The project includes functionality for modifying the analytical parameters and examining how the overall score changes.

This allowed experimentation with different parameter values and their contribution to the final result.

The objective was to understand which parameters had a larger influence on the final policy score.

## Sensitivity Analysis

Sensitivity analysis was implemented to examine how changes in individual parameters affected the overall score.

For each parameter, values around the original value were tested.

The project experimented with:

```text
90% of the original value
100% of the original value
110% of the original value
```

The resulting scores were compared to determine how sensitive the overall result was to each parameter.

The difference between the maximum and minimum scores was used as an indication of the parameter's sensitivity.

This provided an introduction to analysing how changes in assumptions or inputs can influence an analytical model.

## Weight Updating

The sensitivity results were then used to experiment with updating the weights assigned to the different parameters.

The project also contains a basic gradient-descent-style weight update mechanism using a learning rate.

This was an exploratory implementation intended to understand how model parameters could be iteratively adjusted rather than remaining completely fixed.

The updated weights could then be used to recalculate the overall sentiment score.

## Policy-Level Interpretation

After calculating the overall score, the project generates an interpretation of the policy response.

Instead of returning only numerical values, the system attempts to translate the resulting score into a more understandable policy-level conclusion.

The intention was to answer a question such as:

```text
Is the overall public response towards the policy positive,
neutral, or negative?
```

This creates an additional interpretation layer between the raw NLP output and the final result.

## Visualization

Matplotlib was used to create a visualization of the sentiment distribution.

The visualization represents the number of:

- Positive opinions
- Neutral opinions
- Negative opinions

This makes it easier to understand the composition of the analysed opinion dataset.

The visualization was intended to complement the numerical sentiment analysis and provide a quick overview of the overall response.

## End-to-End Workflow

The overall workflow of the project can be summarized as:

```text
Policy Opinions
       ↓
Data Loading
       ↓
Text Preprocessing
       ↓
Polarity & Subjectivity Analysis
       ↓
Sentiment Classification
       ↓
Sarcasm / Entity / Aspect Analysis
       ↓
Parameter Calculation
       ↓
Sensitivity Analysis
       ↓
Weight Adjustment
       ↓
Overall Sentiment Score
       ↓
Visualization
       ↓
Policy Interpretation
```

## Key Challenges

The biggest challenge was that Natural Language Processing was not yet an area that I had formally studied in depth when I developed this project.

I therefore had to independently research NLP concepts and understand how available Python libraries could be used to implement them.

Another challenge was moving beyond a basic sentiment classifier.

A simple implementation could have stopped after calculating TextBlob polarity and assigning positive, neutral, or negative labels. Instead, I experimented with combining multiple analytical components into a larger pipeline.

The project therefore required understanding how different pieces of information could influence an overall result.

Some of the more challenging areas included:

- Understanding polarity and subjectivity.
- Selecting appropriate sentiment thresholds.
- Combining multiple analytical parameters.
- Designing a weighted scoring mechanism.
- Understanding parameter sensitivity.
- Experimenting with weight updates.
- Integrating additional NLP concepts such as sarcasm, entity-based analysis, and aspect-based analysis.
- Understanding the limitations of simple NLP libraries.

## Key Learnings

### Natural Language Processing

This project gave me my first significant exposure to practical Natural Language Processing.

I learned:

- How basic sentiment analysis works.
- How TextBlob can be used for sentiment analysis.
- The difference between polarity and subjectivity.
- How numerical sentiment scores can be converted into categories.
- How NLP outputs can be incorporated into a larger analytical system.

### Data Analysis

The project strengthened my understanding of working with textual datasets.

I learned:

- How to load and manipulate data using Pandas.
- How to work with CSV-based datasets.
- How to continuously add new observations to a dataset.
- How to aggregate individual observations into overall metrics.
- How to visualize categorical distributions.

### Analytical Thinking

The project also introduced me to the idea that an analytical result does not necessarily have to depend on a single variable.

I experimented with:

- Multiple analytical parameters.
- Weighted scoring.
- Parameter tuning.
- Sensitivity analysis.
- Iterative weight adjustment.

This helped me understand how assumptions and parameter choices can influence an analytical outcome.

### Independent Learning

One of the most important learnings from this project was the ability to work with a subject that was not yet fully covered in my formal coursework.

Since I had not been taught NLP in depth at the time, I had to independently research the concepts, understand the available tools, experiment with them, and integrate what I learned into a working project.

## Technologies and Software Used

### Programming Language

- Python

### Data Processing

- Pandas
- CSV

### Natural Language Processing

- TextBlob

### Visualization

- Matplotlib

### Other Python Libraries

- Datetime

## Project Structure

```text
03-sentiment-policy-analysis/
│
├── README.md
│
├── notebook/
│   └── sentiment_analysis.ipynb
│
├── src/
│   └── sentiment_analysis.py
│
├── data/
│   └── opinions.csv
│
├── screenshots/
│   ├── sentiment-analysis-output.png
│   ├── sentiment-distribution.png
│   └── policy-analysis-output.png
│
└── requirements.txt
```

## Running the Project

### 1. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 2. Ensure the dataset is available

The project expects the opinion dataset to be available as:

```text
opinions.csv
```

### 3. Run the Python program

```bash
python sentiment_analysis.py
```

The program can then accept and analyse textual opinions and generate the corresponding sentiment and policy analysis.

## Limitations

The project was developed as an exploratory NLP and data-analysis project rather than as a production-ready policy-analysis platform.

Some of the components are therefore intentionally basic.

### Sentiment Model

TextBlob provides general-purpose sentiment analysis and may not correctly understand every type of context, sarcasm, cultural expression, or domain-specific language.

### Sarcasm Detection

The sarcasm detection mechanism is basic and checks for an explicit reference to sarcasm rather than actually understanding whether a statement is sarcastic.

### Aspect-Based Sentiment Analysis

The project contains a framework for aspect-based analysis, but it does not implement a complete modern aspect extraction and sentiment-classification pipeline.

### Entity-Based Analysis

The entity analysis component is experimental and does not represent a complete named-entity recognition and entity-level sentiment system.

### Negation Handling

Negation processing remains basic and does not fully resolve the linguistic complexity of negated statements.

### Scoring Methodology

The weighted policy score and parameter-weighting system were created as an experimental analytical framework and should not be treated as a statistically validated measure of public opinion.

## Future Improvements

The project could be extended in several ways:

1. Replace TextBlob with modern transformer-based NLP models.
2. Implement a proper sarcasm-detection model.
3. Implement named-entity recognition and entity-level sentiment analysis.
4. Develop a complete aspect-based sentiment analysis pipeline.
5. Improve negation handling.
6. Support multilingual opinions.
7. Use a larger and more representative dataset.
8. Develop a statistically validated scoring methodology.
9. Compare different sentiment-analysis models.
10. Add sentiment analysis over time using the temporal component.
11. Build an interactive dashboard for exploring the results.
12. Store opinions and analysis results in a database instead of a CSV file.
13. Improve the policy interpretation layer using more advanced NLP techniques.

## Project Outcome

The project successfully produced an end-to-end prototype for analysing textual policy opinions.

It demonstrated how raw textual data could be transformed into:

```text
Individual Opinions
        ↓
Sentiment Scores
        ↓
Sentiment Categories
        ↓
Aggregated Metrics
        ↓
Parameter-Based Analysis
        ↓
Overall Score
        ↓
Policy Interpretation
```

Although several components remained experimental, the project provided practical exposure to Natural Language Processing, textual data analysis, parameter-based modelling, sensitivity analysis, and data visualization.

Most importantly, it represented an early example of independently exploring a new technical area and integrating several concepts into a single working analytical system.
