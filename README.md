# Fraud Detection Case Study

For the next two days we will work with the entire end to end pipeline of data science through a case study.  We have touched on aspects of this throughout the course but have not yet put all the pieces together.

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

We will want two deliverables from you for this project:

* A dashboard for investigators to use which helps them identify new events that are worthy of investigation for fraud.  This will pull in new data regularly, and update a useful display for the investigation team.  How you wish to lay this out is up to you.
* A ten-minute presentation on your process and results. 

#### Notes

* [Overview](overview.md): gives a detailed overview of the project.  Included are *suggestions* for how you can organize your team, though this is not binding, and you are free to deviate.
* [Building your model](model_notes.md): notes on how to get started with the dataset and how to save your model once you've trained it.

<<<<<<< HEAD



---------------------------------------------------------------

decided to pick all numerical features first and run random forest.
=======
------------------------------------------------------------------------
Reducing scope:
Decided to pick all numerical features first and run random forest.
Looked at the features which we would receive from the API live feed and threw out all features not included there from our features list since we would not be able to use them to predict. We also excluded information that would not be present when we need to predict.

'acct_type', 'approx_payout_date', 'body_length', 'channels', 'country', 'currency', 'delivery_method', 'description', 'email_domain', 'event_created', 'event_end', 'event_published', 'event_start', 'fb_published', 'gts', 'has_analytics', 'has_header', 'has_logo', 'listed', 'name', 'name_length', 'num_order', 'num_payouts', 'object_id', 'org_desc', 'org_facebook', 'org_name', 'org_twitter', 'payee_name', 'payout_type', 'previous_payouts', 'sale_duration', 'sale_duration2', 'show_map', 'ticket_types', 'user_age', 'user_created', 'user_type', 'venue_address', 'venue_country', 'venue_latitude', 'venue_longitude', 'venue_name', 'venue_state'

Reduced to

'channels', 'country', 'currency', 'delivery_method', 'description', 'email_domain', 'event_created', 'event_end', 'event_published', 'event_start', 'fb_published', 'has_analytics', 'has_header', 'has_logo', 'listed', 'name', 'name_length', 'object_id', 'org_desc', 'org_facebook', 'org_name', 'org_twitter', 'payee_name', 'previous_payouts', 'show_map', 'ticket_types', 'user_age', 'user_created', 'user_type', 'venue_address', 'venue_country', 'venue_latitude', 'venue_longitude', 'venue_name', 'venue_state'
>>>>>>> daniellebranch
