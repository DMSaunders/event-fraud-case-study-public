# Report

## Problem Statement

Our goal is to return a predicted probability that a given event posted on our website is fraudulent. Our primary motivation is to the prevention of false negatives: when an event is actually fraudulent yet we predict that it is not. In this case our company must refund our customers for the fraudulent tickets. It would be much better to catch these fraudulent events first and investigate them. A profit analysis would determine the optimum threshold for predicting fraud.

After inspecting the data and the format of incoming data we determined that we would make basic models with the numeric data and proceed to tune and feature engineer for the basic model which performed best initially. We initially tried a Random Forest model, a Logistic Regression model, and a Gradient Boostieng model. The Gradient Boosting model performed best initially with a recall score around 0.65. The others were significantly worse. After some tuning and grid search cross validation we were able to get a cross validated recall score around 0.70. We decided to proceed with this model.

The next step was to create dummy variables for the many categorical columns to attempt to pick up any signal that may be present in those variables. The result was...

If we had more time to develop the model...


