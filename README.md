# midterm_shopping_intention

## **Problem statement:**

By analyzing data from online sessions of candidate shoppers, the objective is to predict if the session ended with a transaction (gained a revenue) or without a transaction (loss of a revenue). The target column is 'revenue', a boolean, while the other 17 features can be grouped in statistics on web pages visited during the session: (informational, administrative and product-related), (google) analytics data: page_values, bounce_rates and exit_rates and time and place of the transaction: (weekend, month, (proximity of) a special_day, region), type of operating_system, of browser and of traffic

## **Dataset Information:**

The dataset consists of feature vectors belonging to 12,330 sessions.

The dataset was formed so that each session would belong to a different user in a 1-year period to avoid any tendency to a specific campaign, special day, user profile, or period.

## **Dataset Origin:**

ICS UCI ML Repository: [UCI Machine Learning Repository: Online Shoppers Purchasing Intention Dataset Data Set](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset))

notebook.ipynb contains EDA and final Model selection. sandbox.ipynb contains a messy constituted by various experiments tha eventually converged in the notebook.ipynb

for the deployment of the model as a service BentoML package has been used. 