 # Creating a Psychedelic Trip-Report Generator
### Analyzing psychedelic trip reports for predictive modeling and creating a trip report generator

![tree machine.png](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/trip%20generator%201.png)
    
By Jordan Loewen-Colón August 2023

# Objective

In March 2022, researchers from McGill University embarked on a [groundbreaking project](https://www.mcgill.ca/neuro/channels/news/largest-ever-psychedelics-study-maps-changes-conscious-awareness-neurotransmitter-systems-338389) using descriptions from personal experiences with psychedelic substances to map specific mental states to brain activity. This study laid the foundation for developing a sophisticated technology tool that may predict which areas of the brain should be activated to create particular mental sensations or feelings.

This research aims to contribute to **discovering new medicines** by understanding how different drugs can affect the mind. However, a major challenge in this area is the **scarcity** of firsthand accounts or personal descriptions of these experiences.

To address this gap, our objective is to leverage existing personal narratives and use artificial intelligence (AI) to **create realistic 'trip reports'** categorized by different types of drugs. These AI-generated descriptions will then be used to **enhance future research** in the exciting and evolving field of psychedelics, potentially leading to **innovative therapeutic applications**.

# Insights:

From our analysis, the key insights include:

**Significance of "Feeling"**: The word "feeling" was found to have a positive weight in the Random Forest Classifier model, making it likely to classify a report as a psychedelic experience.

**Improvement with Larger Data Sample for Psychedelics**: Word2Vec improved the precision in predicting Psychedelics with RFC by 11%. More data in other categories could lead to similar enhancements.

**Underlying Patterns in Predictions**: Visualization revealed differences in positive and negative predictions related to psychedelics, indicative of how the model made its false positives.

We also employed an LDA model to identify underlying themes. Key topics included words with existential themes; physical sensations; encapsulating social aspects; and illustrative visual experiences. The topics for "Psychedelics" and "Pharmaceuticals" were quite different, as expected. The detailed LDA results can be viewed [here](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Sandbox/LDA%20Final.ipynb).

The first draft of the generator can be found at [Hugging Face Spaces](https://huggingface.co/spaces/Legacy7070/Psychedelic-Trip-Report-Generator). 

# Data Understanding
Our data was collected using a data transfer agreement with McGill University and Queen’s University. The data is from [Erowid’s experience vaults](https://erowid.org/experiences/) and is subject to their copyright, and *may only be used with their permission*. 

The raw data set contains nearly 70k drug reports with 11743 unique drug types. No identifying information was gathered other than the metadata, including dosage, delivery method, the weight of the individual, year consumed, and gender.

Reports themselves averaged between 3k and 5k words.

# Data Preparation
To prepare our data, we performed the following steps:

**Cleaning:**
* Dropping of Null and NaN values
* Dropping non-English reports
* Dropping reports with less than five words
* Dropping drug reports with a single occurrence

**Feature Engineering:**
* Processing the reports into a new column using lemmatization, tokenization, and lowercasing the text
* Creating a new column to indicate whether or not a report contained multiple drug labels
* Creating a new report copy for each individual drug listed in a mixed report
* Cleaning and categorizing drugs into 10 drug categories: Psychedelic, Pharmaceutical, Cannabinoid, Other, Stimulant, Entactogen/Empathogen, Dissociative, Depressant, Opioid, Entheogen. These categories were drawn from the [Alcohol and Drug Foundation Wheel](https://adf.org.au/drug-facts/#wheel)
* Doubling reports that were not mixed to add weight to "pure" drug reports

# Data Modeling

Although we aim to create a psychedelic trip generator, we started by running models like Logistic Regression, RFC (Random Forest Classifier), and XGBoost on the collected trip reports. This is an exploratory step in understanding the language patterns and correlations between drugs and experiences. Analyzing these patterns, we can identify key linguistic features that distinguish various psychedelic experiences. Although these models can't generate new reports, their predictions can inform the design of a more sophisticated trip report generator, such as GPT-2, by providing insights into how specific terms and structures are associated with different drugs. These models act as groundwork to build a more nuanced and informed generative model.

**Precision was our metric**, as we wanted a model that is able to reproduce similar reports itself. 

High precision means that when the model predicts a certain drug type, it is more likely to be correct. If there are severe consequences associated with incorrect positive predictions (false positives), such as legal implications, mislabeling, or misguidance in treatment, then precision would be a critical metric.

After running all three models, we decided to move forward with our best RFC model. We chose the RFC over the logistic regression (which scored slightly better) because the RFC is more robust in providing data on what it considers important to making its predictions and the relationships between different features. After tuning its hyperparameters, the model scored a 75 on precision. In simpler terms, if the model says that a report falls into the 'Psychedelic' category, there is a 75% chance that this prediction is correct.

![rfcclassification.png](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/RFC%20Classification%20Report.PNG)

# Evaluation

Scores like that on their own don't really tell us much about the story. For example, of the 25% of the time the model guessed wrong, what was it most likely to choose?

![heatmatrix.png](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/heatmatrix.png)

Our model was most likely to confuse a trip report about psychedelics with one about Cannabinoids or Empathogen/Entactogens (and even Entheogens, relative to their small sample size!). This aligns with what we would expect, as all three other categories, especially Cannabis, often fall under the broader range of 'psychedelic' substances. 

To help our model find more complex patterns in the reports, we used Word2Vec, which is a method used to represent words in a way that computers can understand. Imagine that every word in a language is represented by a point in space. Words with similar meanings are closer together, and words with different meanings are farther apart. Word2Vec is a technique that helps to find these points for each word. In the following image, we clustered the words together based on their similar meanings (which Word2Vec derives from their context). We then chose the 5 closest (or most similarly meaningful) words from each cluster. Word2Vec learns from the patterns of how words appear with others and represents these patterns as numerical vectors. The similarity between these vectors then gives a measure of the similarity between the words themselves. It's like mapping the social circles of words based on who they "hang out" with!

![word vec clusters.png](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/word%20vec%20clusters.PNG)

We clearly have some different clusters here, but it is not clear what they might have in common. That's because our data set is so complex, and Word2Vec is relatively simply, but it's a positive sign that the clusters do seem to be clear! That means even our simple model is picking up on patterns. To get a different understanding of the underlying patterns between the words in the report, we ran an LDA model and then visualized some word clouds:

![psy word clouds](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/psy%20word%20cloud.PNG)

![pharm word clouds](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/pharm%20word%20cloud.PNG)

Here we see a clear difference between words in the reports labeled "Psychedelic" and those labeled "Pharmaceutical." It looks like both sets of clusters include the names of the drugs from the label category. That could be something we take into account with future data cleaning and engineering. Nevertheless, it's encouraging that our model was able to find relevant distinctions.

Next, we moved on to trying to understand what features and elements our RFC model found important as it was making its predictions. We used LIME (Local Interpretable Model-agnostic Explanations), a tool that helps explain complex models like RFC. LIME is like a translator that breaks the decisions of the RFC model into simpler terms, showing the main reasons behind the decision. It's like asking a translator, "Why did the committee decide this?" and getting a plain-English answer that highlights the most important factors. With the above visualization, we can see that **the word "feeling"** was given positive weight when making a prediction, which means that, when that word appeared, it was likelier to be a "Psychedelic" than not.

![LIME features](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/LIME%20words.PNG)

The "weights" in this plot represent the importance of specific words in determining the category "Psychedelic" for a given text sample. In the context of this plot, a weight is a numerical value assigned to each word that reflects how strongly it influences the classification.

Imagine each word in the text as a vote towards the "Psychedelic" category. The weight tells you how powerful that vote is. A higher weight means the word has a more substantial influence in identifying the text as related to psychedelic experiences, while a lower weight means it has less influence.

Next, we created an explainer using LIME, then chose an instance to explain, and then had the model explain. This visualization takes a single report and then highlights and weights the words within it to show which were most important for predicting whether the report was labeled a "Psychedelic."

![LIME analysis](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/LIME%20analysis.PNG)

Unfortunately, we cannot derive much from the LIME explanation as it seems to indicate that our model gave a lot of weight to stop words in making its predictions. This will require more analysis in the future and perhaps some experiments with removing the stop words even if we lose semantic understanding for our GPT-2 Model later.

Next, we visualized our positive predictions and false predictions.

![prediction patterns](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/true%20and%20false.PNG)

![prediction patterns combined](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Images/true%20vs%20false.PNG)

The three plots visualize model predictions related to psychedelics on a 2D plane. Plot 1 shows correct predictions; Plot 2 highlights incorrect ones with red 'x' markers, and Plot 3 contrasts correct (blue) and incorrect (red 'x') predictions. While the model cannot tell exactly what the patterns are that it is following, we can see that there are differences here that the model is picking up on. Our next step was then to use a more complex model (BigBird) to find features that could take into account the longer form versions of the reports. That model can be found [here](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Sandbox/BigBird.ipynb).

# Conclusion

A company aiming to create a realistic psychedelic trip report generator may consider adopting three strategic approaches: 
- First, capitalizing on the significance of terms like "feeling" and underlying existential or sensory themes, targeted content creation can be employed, with collaboration from experts in the field of psychedelics to ensure the authenticity of trip reports.
- Second, recognizing the improvements seen with larger data samples, investment in extensive research and data collection across varied psychedelic experiences can be undertaken, along with partnerships with psychedelic research organizations for comprehensive insights.
- Finally, more visualization and interpretation tools can be leveraged for both internal assessment and client-facing customization. Offering transparency and alignment with genuine psychedelic experiences, this could also be a unique selling point for engaging a wider audience. Together, these strategies, based on understanding key terms, expanding data insights, and leveraging visualization, can pave a pathway for a more nuanced and business-savvy approach to generating authentic psychedelic trip reports.

# Next Steps

Given the time constraints, our final GPT-2 model is not capable of producing the quality of reports we'd like. Given more time, we'd like to better incorporate the insights from out LDA model which was able to identify underlying themes, the results of which can be viewed [here](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Sandbox/LDA%20Final.ipynb). We also implemented a [BigBird model](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Sandbox/BigBird.ipynb) to process large data sets, taking advantage of its capabilities to handle extensive reports, but did not have time to feed the embedding data into our GPT-2 model. Finally, our [GPT-2 Model here](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Sandbox/GPT_2_Text_Generator.ipynb) was trained to generate text, and an application was created, hosted on [Hugging Face Spaces](https://huggingface.co/spaces/Legacy7070/Psychedelic-Trip-Report-Generator), for public access.

# Questions?
For a full analysis, please check the Jupyter Notebook or slide presentation.
Further questions? Contact Jordan Loewen-Colón @ jbloewen@syr.edu

## Repository Structure


├── [data](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/tree/main/Data) : data used for modeling
├── [images](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/tree/main/Images) : images used in PPT and README
├── [sandbox](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/tree/main/Sandbox) : previous files from first draft of project
├── [GPT-2_generator.ipynb](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/Sandbox/Copy_of_GPT_2_Text_Generator.ipynb) : notebook used to create the generator
├── [Hugging Face Space](https://huggingface.co/spaces/Legacy7070/Psychedelic-Trip-Report-Generator) : Hosted space to access the generator U/I
├── [README.md](https://github.com/jbloewencolon/Psychedelic-Trip-Generator/blob/main/README.md) : project information and repository structure
├── [presentation.pdf]() : the powerpoint presentation used to present data analysis

