# Fraud Detection Case Study

Topics included in this case study include:
* Classification modeling.
* Programming Practice: Handing off models. 
* Teamwork.
* Web applications.
* Website hosting with AWS
* Deploying a DS application.
* Data visualization.
* Results presentation.

#### Rough timeline 

* Day 1: Project scoping, Team direction, Model building
* Day 2: Web app and deployment

#### Deliverables

* A dashboard for investigators to use which helps them identify new events that are worthy of investigation for fraud.  This will pull in new data regularly, and update a useful display for the investigation team.  
* A ten-minute presentation on your process and results. 

#### Problem Statement

Our goal is to create a live dashboard with the predicted probability of fraud for every event the moment users create them on our client's events hosting website. Our primary motivation is the prevention of false negatives: when an event is actually fraudulent yet we predict that it is not, since the company must refund their customers for the fraudulent tickets. It would be much better to catch these fraudulent events first and investigate them. We had 2 days to complete this project.

#### Process Flow
We tackled this project as a cross-functional team with 2 web developers and 4 data scientists. We started with a brainstorm on the content of the dashboard so web dev could prototype until we could connect them to the database containing the events and our predictions. 

#### Accuracy Metrics
We evaluated our models with a Roc_Auc score and a recall score because it shows how many fraudulent events we catch out of all the fraudulent events. A profit analysis would determine the optimum threshold for predicting fraud. We avoided accuracy since it is less applicable to imbalanced datasets like ours, where around 10% of the labels are fraud, and the rest non-fraud. 

#### Results
We were pleasantly surprised by a roc score (area under the curve) of .97. This turned out to be one of the higher scores achieved by the teams competing on this project.

Please see [report](report.md) for more results.