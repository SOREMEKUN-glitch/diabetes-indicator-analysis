Diabetes Indicator Comparison (Diabetic vs Non-Diabetic)
Overview

This project is a small, interpretable health data analysis that compares basic clinical measurements between diabetic and non-diabetic groups. The goal is not to “diagnose diabetes”, but to practice data exploration, group comparison, and biological interpretation in a clean, reproducible way.

Instead of jumping into complex machine learning, I focused on a simple question:
Which measurements show the largest differences between groups?

Research Question

What measurements differ most between diabetic and non-diabetic patients, and how should those differences be interpreted?

Dataset

For this learning project, I used a synthetic sample dataset (n = 8) created directly inside the script.

Features included:

Age

BMI

Blood Pressure

Glucose

Insulin

Diabetes status (Yes / No)

Why synthetic?

It allows me to practice the full analysis flow (loading → exploring → comparing → visualising) without privacy issues.

It makes the code easy to run for anyone reviewing the project.

Note: Because this is synthetic and very small, results are only for demonstration.

Method
1) Data exploration

Previewed the first rows of the dataset

Checked dataset shape (rows, columns)

Generated summary statistics (describe())

2) Group comparison

Separated the dataset into two groups:

Diabetics (Diabetes == "Yes")

Non-diabetics (Diabetes == "No")

For each metric (BMI, blood pressure, glucose, insulin), I computed:

Average value for diabetics

Average value for non-diabetics

Difference = (Diabetic average − Non-diabetic average)

This makes the comparison transparent and easy to interpret.

3) Ranking most differentiating measurements

Sorted the metrics by difference to see which measurement separated the groups the most.

4) Visualization

Created a bar chart of metric differences:

X-axis: health metric

Y-axis: difference between group averages

Saved output as:

diabetes_analysis.png

Results

After separating diabetic and non-diabetic groups and comparing average values, the measurements ranked by difference were:

Metric	Non-Diabetic Avg	Diabetic Avg	Difference
Glucose	89.50	190.00	+100.50
Blood Pressure	117.50	144.25	+26.75
Insulin	12.75	27.25	+14.50
BMI	25.60	34.90	+9.30

The strongest separation between the groups was glucose level, which showed a difference of +100.5 units — far larger than any other measurement. The visualization (diabetes_analysis.png) displays this ranking directly.

Interpretation

The results follow expected physiological patterns:

Glucose: Largest difference and primary indicator of diabetes status

Blood pressure: Elevated in diabetics, consistent with metabolic syndrome association

Insulin: Higher values suggest compensatory insulin resistance in earlier disease stages

BMI: Increased body mass correlates with risk but is less specific than glucose

An important observation is that although multiple measurements differ, their predictive usefulness is not equal. Some variables (like BMI) relate to long-term risk, while others (glucose) reflect current metabolic state.

This highlights a key concept in health analytics:

The most statistically different measurement is not always the most biologically informative — interpretation depends on physiology and context.
Limitations

This project is intentionally simple, and it has important limitations:

Very small sample size (n=8) → results are not statistically reliable

Synthetic dataset → not representative of real clinical variability

No confounder adjustment → differences could reflect other factors (e.g., age distribution)

Not clinical advice → this is not a diagnostic tool

Future work should use a larger real dataset and include:

-statistical tests (t-test / effect size)

-confidence intervals

-missing data handling

-model-based comparisons (logistic regression as next step)