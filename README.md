# midterm_shopping_intention

## **Problem statement:**

By analyzing data from online sessions of candidate shoppers, the objective is to predict if the session ended with a transaction (gained a revenue) or without a transaction (loss of a revenue). The target column is 'revenue', a boolean, while the other 17 features can be grouped in statistics on web pages visited during the session: (informational, administrative and product-related), (google) analytics data: page_values, bounce_rates and exit_rates and time and place of the transaction: (weekend, month, (proximity of) a special_day, region), type of operating_system, of browser and of traffic

## **Dataset Information:**

The dataset consists of feature vectors belonging to 12,330 online sessions.

The dataset was formed so that each session would belong to a different user in a 1-year period to avoid any tendency to a specific campaign, special day, user profile, or period.

## **Dataset Origin:**

ICS UCI ML Repository: [UCI Machine Learning Repository: Online Shoppers Purchasing Intention Dataset Data Set](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset))

the project was executed in a conda environment and the list of dependencies is in requirements.txt  (sorry, there are more than the essential dependencies because the conda enviroment is the one I make use of for the entire ml-zoomcamp course 2022 till now (week 7))

notebook.ipynb contains EDA and the final Model selection. 
sandbox.ipynb contains a messy :) ,constituted by various experiments that eventually converged in the notebook.ipynb, 
train.py contains the logic for training from CLI the final model detrmined in notebook.ipynb

for the deployment of the model as a service BentoML framework has been used. In particular, service.py and bentofile.yaml are part of the depolyment with bentoml.

service.py contains the logic for the prediction service. bentofile.yaml contains the dependencies.
to try in localhost the service: bentoml serve service.py:svc --reload
then the service can be checked through a swaggerUI interface in the browser

by executing :
bentoml build

a bento archive is built. bento definition from the official docs: 'Bento 🍱 is a file archive with all the source code, models, data files and dependency configurations required for running a user-defined bentoml.Service, packaged into a standardized format.'

in particular in the bento archive is included a Dockerfile

in order to containeraize the service from the bento archive: 
bentoml containerize midterm_classifier:xxxxxxxxxxxxxxx

where midterm_classifier:xxxxxxxxxxxxxxx is the tag of the bento archive (as an example: bentoml containerize midterm_classifier:oah24sc6xgqjouon)

now to serve the prediction as a containerized service, execute:
docker run -it --rm -p 3000:3000 midterm_classifier:7mx2pds7i2pxbr2e
(docker has to be installed to execute the last command. 

I made my project in a linux environment (Ubuntu 22.04) over a windows OS (win11) by using WSL2 virtualization. Docker Desktop was installed in Windows and VSCode was used as IDE.

