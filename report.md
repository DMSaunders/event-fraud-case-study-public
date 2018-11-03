# Report

## Problem Statement

Our goal is to create a live dashboard with the predicted probability of fraud for every event the moment users create them on our client's events hosting website. Our primary motivation is the prevention of false negatives: when an event is actually fraudulent yet we predict that it is not, since the company must refund their customers for the fraudulent tickets. It would be much better to catch these fraudulent events first and investigate them. We had 2 days to complete this project.

## Process Flow
We tackled this project as a cross-functional team with 2 web developers and 4 data scientists. We started with a brainstorm on the content of the dashboard so web dev could prototype until we could connect them to the database containing the events and our predictions. Soon after we received web dev's requirement that we should pull the data out of our database and provide them a route to it as json. Then the data scientists brainstormed accuracy metrics and preprocessing for the creation of the model that output the predictions and divided the labor. We reconvened a few more times to brainstorm and divvy. We operated on separate feature branches on github which we merged at the end to run and debug on a single machine running an AWS EC2. 

## Accuracy Metrics
We evaluated our models with a Roc_Auc score and a recall score because it shows how many fraudulent events we catch out of all the fraudulent events. A profit analysis would determine the optimum threshold for predicting fraud. We avoided accuracy since it is less applicable to imbalanced datasets like ours, where around 10% of the labels are fraud, and the rest non-fraud. 

## Preprocessing
After inspecting the data and the incoming data from the API we determined that we would make basic models with features filling these requirements: 
* numeric data (for simplicity)
* features present in the API 
* features that would be available at the time of prediction

We tuned and feature engineered for the basic model which performed best on this feature set. We started with a Random Forest model, a Logistic Regression model, and a Gradient Boosting model. The Random Forest model performed best with a recall score around 0.65. The others were significantly worse. 

The next step was to create dummy variables for the many categorical columns to attempt to pick up any signal that may be present in those variables. At this iteration we left out the columns that would require NLP for further analysis, such as the event titles and descriptions. For columns with a significant amount missing data, we encoded missing values as a dummy variable so as to retain the signal that could be provided by a user not submitting data for that column. 

## Parameter Tuning
The categorical feature set, with gridsearch, was a lower score of around .50. After some tuning and grid searching we were able to get a cross-validated recall score around 0.72 with Gradient Boosting on the most basic feature set. We used 3-fold cross-validation and a couple parameters for number of estimators, percent subsample, minimum sample split, and max depth, with a single learning rate of .10. We decided to proceed with this model. 

We were pleasantly surprised by the roc score (area under the curve) of .97. This turned out to be one of the higher scores achieved by the teams competing on this project. We noticed that when we lower our threshold into the .005 range, we can send our recall score into the .90s while maintaining a false positive rate below .20. At a threshold of around .50, our recall is around .67.

## Dashboard
We had the pleasure of collaborating with the web development students for the production of the web app. We created a flask server which queries all the rows from our DynamoDB and returns them when @app.route is hit. Web dev created a dashboard displaying these rows with a subset of relevant columns: Event name, probability of fraud, risk label (low, med, high), and event id. This enables a user to see the events by risk and take action to take down fraudulent events, saving the company reimbursement costs.

## AWS
We hosted all of this on a deep learning Amazon Web Services EC2 instance so that the web dev team could access our server.

## Next Steps
Our next steps will be to use NLP on the descriptive features and run that version of the data through our pipeline. Given that our gradient boosting model reveals feature importances for each feature, we would like to display the top three most important features in the model on our dashboard so users can see which event attributes most likely caused the event to be flagged. The user who is contacting the event creator can be aware that we flagged events most likely due to user type, user age (in days since account creation), and/or presence of logo. That way, if the user encounters a non-fraudulent user, they can remedy the event or assure the user that likelihood of being flagged declines with account age. 






