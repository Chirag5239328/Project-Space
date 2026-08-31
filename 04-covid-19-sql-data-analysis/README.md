# COVID-19 SQL Data Analysis

## Overview

This project focuses on analyzing a COVID-19 dataset using SQL to extract meaningful information about confirmed cases, deaths, recoveries, active cases, case fatality rates, weekly changes, and regional trends.

The project consists of a collection of 18 SQL-based analytical queries designed to examine the progression and distribution of COVID-19 cases across countries and WHO regions.

The analysis focuses on transforming raw COVID-19 data into structured insights that can be used to compare countries, identify trends, calculate important epidemiological measures, and understand differences across WHO regions.

---

## Objectives

The main objectives of the project were to:

- Analyze confirmed COVID-19 cases and deaths across countries.
- Identify countries experiencing high numbers of new cases.
- Examine countries with large numbers of active cases.
- Compare recoveries across WHO regions.
- Identify countries with high recovery rates.
- Calculate average and country-level death rates.
- Analyze weekly changes in COVID-19 cases.
- Calculate case fatality rates.
- Compare COVID-19 statistics across WHO regions.
- Rank countries according to confirmed cases.
- Analyze the relationship between confirmed cases, deaths, and recoveries.
- Calculate rolling averages to identify trends over time.

---

## Analysis Performed

The project contains 18 SQL analyses.

### 1. Total Confirmed Cases and Deaths by Country

Analyzed the total number of confirmed COVID-19 cases and deaths for each country.

This provides a country-level overview of the scale of the pandemic and allows countries to be compared based on their reported case and death counts.

---

### 2. Top 10 Countries with the Highest New Cases

Identified the 10 countries with the highest number of newly reported COVID-19 cases.

This analysis helps highlight countries experiencing particularly high levels of new infections.

---

### 3. Countries with More than 100,000 Active Cases

Identified countries where the number of active COVID-19 cases exceeded 100,000.

This provides an indication of countries experiencing a substantial number of ongoing cases.

---

### 4. Total Recoveries by WHO Region

Calculated the total number of recovered COVID-19 cases for each WHO region.

This allows recovery levels to be compared across different geographical regions.

---

### 5. Countries with a Recovery Rate Higher Than 80%

Calculated recovery rates and identified countries where the recovery rate exceeded 80%.

This analysis focuses on comparing recovery outcomes between countries.

---

### 6. Average Death Rate Across All Countries

Calculated the average death rate across the countries represented in the dataset.

This provides an overall measure that can be used as a reference when comparing country-level death rates.

---

### 7. Countries with the Highest Weekly Percentage Increase in Cases

Analyzed weekly changes in confirmed cases and identified countries experiencing the highest percentage increase.

This focuses on the rate at which reported cases were increasing rather than simply looking at total cases.

---

### 8. Countries with the Largest Weekly Change in Confirmed Cases

Identified countries with the largest absolute weekly changes in confirmed COVID-19 cases.

This analysis complements the percentage-based weekly increase analysis by focusing on the magnitude of the change.

---

### 9. Case Fatality Rate (CFR) for Each Country

Calculated the Case Fatality Rate for each country using confirmed cases and reported deaths.

The analysis provides a standardized way to compare the proportion of confirmed cases associated with reported deaths.

---

### 10. Total Cases and Deaths per WHO Region

Aggregated confirmed cases and deaths by WHO region and ranked the regions according to total deaths.

This provides a regional-level comparison of the impact of COVID-19.

---

### 11. Countries Where the Death Rate Exceeds the Recovery Rate

Compared death rates and recovery rates at the country level.

Countries where the death rate exceeded the recovery rate were identified for further comparison.

---

### 12. Top 5 Countries by Total Confirmed Cases

Ranked countries according to their total number of confirmed COVID-19 cases and identified the top five.

This provides a straightforward comparison of countries with the largest reported case counts.

---

### 13. WHO Regions with a Recovery Rate Below 75%

Calculated recovery rates at the WHO-region level and identified regions where the recovery rate was below 75%.

This allows regional differences in reported recovery outcomes to be examined.

---

### 14. Countries with the Highest Confirmed-to-Death Ratio

Calculated the ratio between confirmed COVID-19 cases and deaths for each country.

The analysis was used to identify countries with the highest confirmed-to-death ratios.

---

### 15. 7-Day Rolling Average of New Cases for Each Country

Calculated a seven-day rolling average of newly reported cases for each country.

Rolling averages help smooth daily fluctuations and provide a clearer view of short-term trends in reported cases.

---

### 16. Countries with the Largest Decrease in Active Cases Over the Last Week

Analyzed changes in active cases over a one-week period and identified countries experiencing the largest decreases.

This provides an indication of where active case counts were declining most substantially.

---

### 17. Countries with the Highest Death Proportion Compared to New Cases

Compared reported deaths with new cases to identify countries with a relatively high death proportion compared with newly reported cases.

---

### 18. Top 5 WHO Regions by Case Fatality Rate

Calculated the Case Fatality Rate at the WHO-region level and identified the five regions with the highest rates.

This provides a regional comparison based on the relationship between reported deaths and confirmed cases.

---

## Key SQL Concepts Applied

The project provided practical exposure to SQL-based data analysis, particularly through queries involving:

- Aggregation
- Filtering
- Grouping
- Sorting
- Ranking
- Calculated metrics
- Rate calculations
- Ratio calculations
- Country-level analysis
- WHO-region-level analysis
- Weekly comparisons
- Rolling averages
- Case fatality rate calculations
- Comparative analysis

The project demonstrates how SQL can be used to move from raw records to structured analytical insights.

---

## Dataset

The project uses a COVID-19 dataset containing country-level and regional COVID-19 statistics.

The analysis works with measures relating to:

- Confirmed cases
- New cases
- Active cases
- Recoveries
- Deaths
- Weekly changes
- WHO regions

The original project documentation does not contain the original dataset file or its exact source information. Therefore, the repository should only include the dataset if the original file is available and can be legally redistributed.

---

## Project Documentation

The original project was documented as a collection of SQL analysis questions and their corresponding outputs.

The documentation covers all 18 analytical tasks performed in the project.

---

## Key Learnings

### 1. Applying SQL to Real-World Data

The project provided practical experience in using SQL to analyze a real-world dataset rather than working only with simple sample tables.

---

### 2. Translating Business Questions into SQL Queries

Each analysis began with a specific analytical question and required converting that question into a SQL query capable of producing the required result.

This helped develop the ability to approach data analysis as a problem-solving process rather than simply writing SQL syntax.

---

### 3. Aggregating and Comparing Data

The project involved aggregating COVID-19 statistics at both country and WHO-region levels.

This provided experience in comparing large groups of records and extracting meaningful summaries.

---

### 4. Working with Derived Metrics

Several analyses required calculated measures such as recovery rates, death rates, case fatality rates, ratios, and percentage changes.

This provided experience in creating analytical metrics rather than relying only on raw columns.

---

### 5. Time-Based Analysis

The project included weekly comparisons and a seven-day rolling average of new cases.

This provided exposure to analyzing how data changes over time and using time-based calculations to identify trends.

---

### 6. Ranking and Filtering

Several analyses required ranking countries or regions and filtering results according to specific conditions.

Examples include identifying:

- Top 10 countries by new cases
- Top 5 countries by confirmed cases
- Countries with more than 100,000 active cases
- Countries with recovery rates above 80%
- WHO regions with recovery rates below 75%

---

### 7. Understanding Data from Different Levels

The project demonstrated the importance of analyzing data at different levels.

Country-level analysis provides detailed comparisons, while WHO-region analysis provides a broader geographical perspective.

---

## Challenges

One of the main challenges in this project was translating different analytical questions into appropriate SQL logic.

The project required more than simple filtering because several questions involved:

- Calculated rates
- Ratios
- Aggregations
- Rankings
- Weekly comparisons
- Regional grouping
- Rolling averages

Working through these different analytical requirements helped develop a broader understanding of how SQL can be used for data analysis.

---

## Project Outcome

The project resulted in a collection of 18 SQL analyses covering different aspects of COVID-19 data.

The analyses examined country-level and regional statistics, including cases, deaths, recoveries, active cases, rates, ratios, weekly changes, and rolling averages.

The project therefore served as practical SQL data-analysis work, demonstrating the use of SQL to answer a diverse set of analytical questions from a structured dataset.

---

## Analysis Summary

| # | Analysis |
|---|---|
| 1 | Total Confirmed Cases and Deaths by Country |
| 2 | Top 10 Countries with the Highest New Cases |
| 3 | Countries with More than 100,000 Active Cases |
| 4 | Total Recoveries by WHO Region |
| 5 | Countries with a Recovery Rate Higher Than 80% |
| 6 | Average Death Rate Across All Countries |
| 7 | Countries with the Highest Weekly Percentage Increase in Cases |
| 8 | Countries with the Largest Weekly Change in Confirmed Cases |
| 9 | Case Fatality Rate for Each Country |
| 10 | Total Cases and Deaths per WHO Region |
| 11 | Countries Where the Death Rate Exceeds the Recovery Rate |
| 12 | Top 5 Countries by Total Confirmed Cases |
| 13 | WHO Regions with a Recovery Rate Below 75% |
| 14 | Countries with the Highest Confirmed-to-Death Ratio |
| 15 | 7-Day Rolling Average of New Cases |
| 16 | Countries with the Largest Decrease in Active Cases |
| 17 | Countries with the Highest Death Proportion Compared to New Cases |
| 18 | Top 5 WHO Regions by Case Fatality Rate |

---

## Technologies

- SQL
- Relational data analysis
- COVID-19 dataset

---

## Project Context

This project was created as an individual data-analysis project to gain practical exposure to SQL and demonstrate the ability to work with a real-world dataset.

The project complemented other data-analysis and visualization projects by focusing specifically on SQL-based analytical problem solving.
