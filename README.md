 # Psychedelic Trip-Report Generator
### Analyzing psychedelic trip reports for predictive modeling and creating a trip report generator

![tree machine.png](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/trip%20generator%201.png)
    
By Jordan Loewen-Colón August 2023

# Objective

In March 2022, researchers from McGill University embarked on a [groundbreaking project](https://www.mcgill.ca/neuro/channels/news/largest-ever-psychedelics-study-maps-changes-conscious-awareness-neurotransmitter-systems-338389) using descriptions from personal experiences with psychedelic substances to map specific mental states to brain activity. This study laid the foundation for developing a sophisticated technology tool that may predict which areas of the brain should be activated to create particular mental sensations or feelings.

This research aims to contribute to **discovering new medicines** by understanding how different drugs can affect the mind. However, a major challenge in this area is the **scarcity** of firsthand accounts or personal descriptions of these experiences.

To address this gap, our objective is to leverage existing personal narratives and use artificial intelligence (AI) to **create realistic 'trip reports'** categorized by different types of drugs. These AI-generated descriptions will then be used to **enhance future research** in the exciting and evolving field of psychedelics, potentially leading to **innovative therapeutic applications**.

# Insights:

From our analysis, the key insights include:

Significance of "Feeling": The word "feeling" was found to have a positive weight in the Random Forest Classifier model, making it likely to classify a report as a psychedelic experience.

Improvement with Larger Data Sample for Psychedelics: Word2Vec improved the precision in predicting Psychedelics with RFC by 11%. More data in other categories could lead to similar enhancements.

Underlying Patterns in Predictions: Visualization revealed differences in positive and negative predictions related to psychedelics, indicative of how the model made its false positives.

We also employed an LDA model to identify underlying themes. Key topics included words with existential themes; physical sensations; encapsulating social aspects; and illustrative visual experiences. The topics for "Psychedelics" and "Pharmaceuticals" were quite different, as expected. The detailed LDA results can be viewed here.

# Data Understanding
Our data was collected using a data transfer agreement with McGill University and Queen’s University. The data itself is from Erowid’s experience vaults and is subject to their copyright and may only be used with their permission. 

The raw data set contains nearly 40k drug reports with 11743 unique drug types. No identifying information was gathered other than the metadata, including dosage, delivery method, the weight of the individual, year consumed, and gender.

Reports themselves averaged between 3k and 5k words.

# Data Preparation
To prepare our data, we performed the following steps:

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

Although we aim to create a psychedelic trip generator, we start by running models like Logistic Regression, RFC (Random Forest Classifier), and XGBoost on the collected trip reports. This is an exploratory step in understanding the language patterns and correlations between drugs and experiences. We can identify key linguistic features that distinguish various psychedelic experiences by analyzing these patterns. Although these models can't generate new reports, their predictions can inform the design of a more sophisticated trip report generator, such as GPT-2, by providing insights into how specific terms and structures are associated with different drugs. These models act as a groundwork to build a more nuanced and informed generative model.

After running all three models, we decided to move forward with our best RFC model. We chose the RFC over the logistic regression (which scored better) because the RFC is more robust in providing data on what it considers important and the relationships between different features. After tuning its hyperparameters, the model scored a 75 on precision. In simpler terms, if the model says that a report falls into the 'Psychedelic' category, there is a 75% chance that this prediction is correct.

![rfcclassification.png](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/RFC%20Classification%20Report.PNG)

# Data Understanding

Scores like that on their own don't really tell us much about the story. For example, of the 25% of the time the model guessed wrong, what was it most likely to choose?

![heatmatrix.png](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/heatmatrix.png)

Our model was most likely to confuse a trip report about psychedelics with one about Cannabinoids or Empathogen/Entactogens (and even Entheogens, relative to their small sample size!). This all falls in line with what we would expect, as all three of those other categories, especially Cannabis, often fall under the broader range of 'psychedelic' substances.

![word vec clusters.png](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/word%20vec%20clusters.PNG)

![psy word clouds](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/psy%20word%20cloud.PNG)

![pharm word clouds](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/pharm%20word%20cloud.PNG)

![LIME features](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/LIME%20words.PNG)

![LIME analysis](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/LIME%20analysis.PNG)

![prediction patterns](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/true%20and%20false.PNG)

![prediction patterns combined](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/true%20vs%20false.PNG)

# Conclusion

A company aiming to create a realistic psychedelic trip report generator may consider adopting three strategic approaches: First, capitalizing on the significance of terms like "feeling" and underlying existential or sensory themes, targeted content creation can be employed, with collaboration from experts in the field of psychedelics to ensure the authenticity of trip reports. Second, recognizing the improvements seen with larger data samples, investment in extensive research and data collection across varied psychedelic experiences can be undertaken, along with partnerships with psychedelic research organizations for comprehensive insights. Finally, more visualization and interpretation tools can be leveraged for both internal assessment and client-facing customization. Offering transparency and alignment with genuine psychedelic experiences, this could also be a unique selling point for engaging a wider audience. Together, these strategies, based on understanding key terms, expanding data insights, and leveraging visualization, can pave a pathway for a more nuanced and business-savvy approach to generating authentic psychedelic trip reports.

# Next Steps

We also employed an LDA model for topic modeling to identify underlying themes, the results of which can be viewed [here](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Sandbox/LDA%20Final.ipynb). We also implemented a [BigBird model](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Sandbox/BigBird.ipynb) to process large data sets, taking advantage of its capabilities to handle extensive reports. Finally, our [GPT-2 Model here](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Sandbox/GPT_2_Text_Generator.ipynb) was trained to generate text, and an application was created, hosted on Hugging Face Spaces, for public access.

# Questions?
For a full analysis, please check the Jupyter Notebook or slide presentation.
Further questions? Contact Jordan Loewen-Colón @ jbloewen@syr.edu

## Repository Structure


├── [data](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/tree/main/Data) : data used for modeling
├── [images](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/tree/main/Images) : images used in PPT and README
├── [sandbox](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/tree/main/Sandbox) : previous files from first draft of project
├── [generator.ipynb](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Psychedelic_Trip_Generator.ipynb) : notebook used to create the generator
├── [Hugging Face Space](https://huggingface.co/spaces/Legacy7070/Psychedelic-Trip-Report-Generator) : Hosted space to access the generator U/I
├── [README.md](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/README.md) : project information and repository structure
├── [presentation.pdf]() : the powerpoint presentation used to present data analysis

