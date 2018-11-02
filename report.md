# Report

## Problem Statement

Our goal is to return a predicted probability that a given event posted on our website is fraudulent. Our primary motivation is to the prevention of false negatives: when an event is actually fraudulent yet we predict that it is not. In this case our company must refund our customers for the fraudulent tickets. It would be much better to catch these fraudulent events first and investigate them. 

## Accuracy Metrics
We evaluated our models with recall score because it shows how many fraudulent events we catch out of all the fraudulent events. A profit analysis would determine the optimum threshold for predicting fraud. We avoided accuracy since it is less applicable to imbalanced datasets like ours, where around 10% of the labels are fraud, and the rest non-fraud. 

After inspecting the data and the format of incoming data we determined that we would make basic models with the numeric data and proceed to tune and feature engineer for the basic model which performed best initially. We initially tried a Random Forest model, a Logistic Regression model, and a Gradient Boosting model. The Random Forest model performed best initially with a recall score around 0.65. The others were significantly worse. After some tuning and grid searching we were able to get a cross-validated recall score around 0.72. We decided to proceed with this model.

The next step was to create dummy variables for the many categorical columns to attempt to pick up any signal that may be present in those variables. At this iteration we left out the columns that would require NLP for further analysis, such as the event titles and descriptions. For columns with a significant amount missing data, we encoded missing values as a dummy variable so as to retain the signal that could be provided by a user not submitting data for that column. The result was...

We were pleasantly surprised by the roc score and the graph. At .97, we noticed that when we lower our threshold into the .005 range, we can send our recall score into the .90s while maintaining a false positive rate below .20. At a threshold of around .50, our recall is around .67.

Our next steps will be to use NLP on the descriptive features and run that version of the data through our pipeline.

-------------


An overview of a chosen "optimal" modeling technique, with:
process flow
preprocessing
accuracy metrics selected
validation and testing methodology
parameter tuning involved in generating the model
further steps you might have taken if you were to continue the project.
