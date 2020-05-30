# Final Project Purwadhika Data Science Bandung

In this project I designed a platform for Prediction of Employee Attrition for a Medical Supply/Pharmaceutical Company.
This project goals is to predict employee attrition or in a simple explanation, predict the probability of an employee to resign/retire from their jobs. The main purpose is not to predict whether certain individual tends to leave the company or not. Instead I want to create a platform for better decision making in HR policy and management based on data regarding employee attrition.

### 1. Data Cleaning.

In this project I am using Employee Database of an Indian Medical Supply/Pharmaceutical Company downloaded from Kaggle. 
The Data downloaded from Kaggle contains 4410 entries and distributed in 4 different files, so I must join the data first, fill the NaN values using mean and mode methods, and delete unnecessary columns.
It orgininally contains 24 columns, after adding some features and delete unnecessary columns it become 28 columns. 
The data distribution on numerical features mostly not normally distributed. Means the distribution curve did not shape like a bell, or most of the data are not centered near mean value.
On the categorical values there is no unique condition like some features tends to more affecting the attrition rate than the others, mostly it is because the composition of the population, higher population in a category also mean higher attrition. Like, most of the employee are in Sales department, so the Sales department has the highest attrition rate.

### 2. Modelling

Because the data is imbalance(83 vs 14), I tried using SMOTE on train data on testing stage and it made an improvement on accuracy score and decreasing log loss on the models. On the implementation stage, I prefer to do modelling without SMOTE because RFC is performing well on raw data.
I did not do the feature scaling because the data without scaler is perform really well and also feature scaling to tree based model is not necessarily important because tree model split the features based on similarity between them. I think the tree based model had the better score because the data contains broad range of feature that not on same scale like age, working years, income, categorical data, and scores of survey.
RFC model used with best parameter the accuracy score is still at around 99% in case it maybe increased in small number, as the classification report only takes 2 digit decimal.

The final model used in this platform in Random Forest Regressor with accuracy score around 98%. Score with original data gained score :

Model | Accuracy Score | Recall Score | F1 Score | Log Loss
------------ | ------------ | ------------- | ------------- | -------------
Random Forest Classifier | 0.992063 | 0.953020 | 0.975945 | 0.274117	

#### Hyperparameter Optimization
I search teh best parameter for this model using GridSearchCV. The parameter i used for search are : 
* 'class_weight':[{0 : 1, 1 : 2},{0 : 1, 1 : 4},{0 : 1, 1 : 6}]
* 'min_samples_leaf':[1,2,3,4,5]
* 'min_samples_split':[2,3,4,5]
* 'n_estimators':[50,100,200]}

the best parameters are :
{'class_weight': {0: 1, 1: 2},
 'min_samples_leaf': 1,
 'min_samples_split': 2,
 'n_estimators': 200}

Classification Report with best parameters : 
               precision    recall  f1-score   support

           0       0.99      1.00      1.00       733
           1       1.00      0.95      0.98       149

    accuracy                           0.99       882
   macro avg       1.00      0.98      0.99       882
weighted avg       0.99      0.99      0.99       882

### 3. Dashboard Deployment

The dashboard are needed for user to comfortably use the platform. Dashboard are built using python Flask. The function included in dashboard are table show up, predictor, and several data visualization about the distribution of employee attrition.
![GitHub Logo](/images/dashboard.png)

