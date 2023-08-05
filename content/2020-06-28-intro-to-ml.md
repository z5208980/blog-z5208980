---
title: "Intro to Machine Learning"
date: "2020-06-28"
tags: ["Machine Learning", "Python"]
gradients: ["#ff6e7f", "#bfe9ff"]
---

## Abstraction
Before I start learning about machine learning. The content and notes that I will be collecting comes from the AWS developer path for AI. I will be following this study path and give my understanding on ML (Machine Learning) here, as well as future blogs.

Link: [AWS Developer Path for ML](https://aws.amazon.com/training/learn-about/machine-learning/)

## Machine Learning
### ML terminology
**Training**
- Split into training and testing
- Training is input data to machine and trains the model.
- Then Testing is test for accuracy and compared to stored dataset.

**Model**

**Prediction**

**Features**
- The attributes of data

**Label**
- (the variable output) outcome, response

### Stages
When trying to deploy a model it is usually these steps we found. When studying the **CRISP-DM**, I noticed that it followed the similar pattern. So I combined my notes into here as well.

**Business understanding**
- Requirements (user stories) => problem statements => ML objective. Then project plan.
- Identifying the machine learning problem.
- Includes which algorithm to use

### Type of training model
- **Supervised**: provided dataset with results
- **Unsupervised**: let machine learning output result
- **Reinforce**: reward and penalty

**Developing Dataset**
- Collect datasets and integration. Data should be as accurate as possible.

**Data Collection**
- Convert data types
- Shuffle training data
- Improves accuracy and performance
- Splitting data to test and training (Cross Validation)
    - 80% train and 20% test or 70%, 30%
    - Leave one out, (use one row for testing)
    - K-fold

**Data understanding**
Data Quality (completeness of data and predict missing data)

- Clean ( Reduce data noises )
    -   dealing with null values (missing values) or outliers, invalid values.
    - removes rows, or add new variable (likes adding mean or median)
    - Bias and variances
- Transform ( data type ) (One hot encoding and normalise)
- Merge ( Join attributes )
- Formatting ( text encoding, shuffle )

**Data visualisation**
Plotting on graphs
AWS Services on data analysis (Used in CRISP-DM)
AWS Glue (crate meta data for csv and db in AWS S3)
AWS Athena (used to query in AWS Glue)
AWS Quicksight (used for visualisation analysis in Athena query)

**Feature Engineering** This is Uses trail and errors Implementation convert raw data into useful information
- Transformation
- Binning
- sorting, cateriogical to reduce the total frequency of features.
- combining two features into one feature.
- Using log and mythical algorithms
- For text, stemming, lowercase and text normalisation.

**Model Training** Parameter Tuning. Attributes to tune model, like parameters to prunes to decision tree.

**Evaluation**
- Overfitting
    - Due to noisy data. Need to generalise. Bad, since good at training but very bad in testing. It’s learning from the noise.
- Underfitting
    - Not flexible. Due to high bias. Too few parameters foe features.
- Quality assurance (review project)

**Deployment** These are pretty obvious in regular projects developments.
- Final Report
- Project Review