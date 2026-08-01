# Customer Funnel Analysis

## Overview

This project analyzes customer behavior throughout an e-commerce purchasing funnel using **Python** and **pandas**. By combining data from multiple stages of the customer journey, the analysis identifies where visitors leave the purchasing process and measures the overall conversion funnel.

The project demonstrates common data analysis techniques, including data merging, missing value analysis, percentage calculations, and datetime operations.

---

## Objectives

* Merge multiple datasets into a complete customer journey.
* Analyze customer drop-off at each stage of the purchasing funnel.
* Identify the weakest step in the conversion process.
* Calculate the average time between a customer's first visit and completed purchase.

---

## Technologies Used

* Python 3
* pandas

---

## Dataset

The project uses four CSV files representing different stages of an online shopping experience:

* **visits.csv** – Customer website visits
* **cart.csv** – Products added to shopping carts
* **checkout.csv** – Customers who reached checkout
* **purchase.csv** – Completed purchases

Each dataset is merged using left joins to preserve customer activity throughout the funnel.

---

## Analysis Performed

The project includes the following analyses:

* Reading and importing CSV datasets
* Parsing datetime columns
* Merging DataFrames with left joins
* Detecting missing values using `isnull()`
* Calculating conversion percentages between funnel stages
* Identifying customer drop-off points
* Measuring the average time from initial visit to purchase

---

## Key Findings

The analysis shows:

* The **Visit → Cart** stage has the largest customer drop-off.
* Customers who reach the checkout stage are significantly more likely to complete a purchase.
* The average time between a customer's first visit and purchase can be calculated using pandas datetime operations.

---

## Skills Demonstrated

* Data manipulation with pandas
* DataFrame merging
* Missing data analysis
* Boolean indexing
* Conversion funnel analysis
* Datetime calculations
* Business metric reporting

---

## Future Improvements

Possible enhancements include:

* Visualizing funnel conversion rates with charts.
* Creating a reusable function for funnel analysis.
* Exporting analysis results to a report.
* Building an interactive dashboard using Plotly or Streamlit.

---

## Author

Lydia L.
