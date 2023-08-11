# Psychedelic Trip-Report Generator
### Analyzing psychedelic trip reports for predictive modeling and creating a trip report generator

![tree machine.png](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/trip%20generator%201.png)
    
By Jordan Loewen-Colón August 2023

# Objective
In March 2022, researchers from McGill University embarked on a [groundbreaking project](https://www.mcgill.ca/neuro/channels/news/largest-ever-psychedelics-study-maps-changes-conscious-awareness-neurotransmitter-systems-338389) using descriptions from personal experiences with psychedelic substances to map specific mental states to brain activity. This study laid the foundation for developing a sophisticated technology tool that might one day predict which areas of the brain should be activated to create particular mental sensations or feelings.

This research aims to contribute to **discovering new medicines** by understanding how different drugs can affect the mind. However, a major challenge in this area is the **scarcity** of firsthand accounts or personal descriptions of these experiences.

To address this gap, our objective is to leverage existing personal narratives and use artificial intelligence (AI) to **create realistic 'trip reports'** categorized by different types of drugs. These AI-generated descriptions will then be used to **enhance future research** in the exciting and evolving field of psychedelics, potentially leading to **innovative therapeutic applications**.

# Insights:


# Data Understanding
Our data was collected using a data transfer agreement with McGill University and Queen’s University. The data itself is from Erowid’s experience vaults and is subject to their copyright and may only be used with their permission. 

The raw data set contains close to 40k drug reports with 11743 unique drug types. No identifying information was gathered other the metadata including dosage, delivery method, weight of individual, year consumed, and gender.

Reports themselves averaged between 3k and 5k words.

# Data Preparation
To prepare our data we performed the following steps:

**Cleaning:**
* Dropping of Null and NaN values
* Dropping non-English reports
* Dropping reports with less than five words
* Dropping drugs with a single occurrence

**Feature Engineering:**
* Processing the reports into a new column using lemmatization, tokenization, and lowercasing the text
* Creating a new column to indicate whether or not a report contained multiple drug labels
* Creating a new report copy for each individual drug listed in a report
* Cleaning and categorizing drugs into 10 drug categories  [Psychedelic, Pharmaceutical, Cannabinoid, Other, Stimulant, Entactogen/Empathogen, Dissociative, Depressant, Opioid, Entheogen]
* Doubling reports that were not mixed to add weight to "pure" drug reports

# Data Modeling

![confusionmatrix.png]()


![log reg featureimport.png]()

**Model: Logistic Regression**

- accuracy: 0.8763326226012793
- precision: 0.9723926380368099
- recall: 0.8661202185792349
- F1-score: 0.9161849710982659

**Model: RFC**

- accuracy: 0.8571428571428571
- precision: 0.9746031746031746
- recall: 0.8387978142076503
- F1-score: 0.9016152716593245

**Model: GBC**

- accuracy: 0.8528784648187633
- precision: 0.9684542586750788
- recall: 0.8387978142076503
- F1-score: 0.8989751098096632

# Data Understanding

Interpretations:

![top coefficients.png]()

![oscore use.png]()


# Conclusion


# Next Steps


# Questions?
For a full analysis, please check the Jupyter Notebook or slide presentation.
Further questions? Contact Jordan Loewen-Colón @ jbloewen@syr.edu

## Repository Structure


├── [data](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/tree/main/Data) : data used for modeling
├── [images](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/tree/main/Images) : images used in PPT and README
├── [sandbox](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/tree/main/Sandbox) : previous files from first draft of project
├── [generator.ipynb]() : notebook used to create the generator
├── [README.md](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/README.md) : project information and repository structure
├── [presentation.pdf]() : the powerpoint presentation used to present data analysis

