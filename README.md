# Final Project Purwadhika Data Science Bandung

In this project I designed a platform for Prediction of Employee Attrition for a Medical Supply/Pharmaceutical Company.
This project goals is to predict employee attrition or in a simple explanation, predict the probability of an employee to resign/retire from their jobs. The main purpose is not to predict whether certain individual tends to leave the company or not. Instead I want to create a platform for better decision making in HR policy and management based on data regarding employee attrition.

## 1. Data Cleaning.

In this project I am using Employee Database of an Indian Medical Supply/Pharmaceutical Company downloaded from Kaggle. 
The Data downloaded from Kaggle contains 4410 entries and distributed in 4 different files, so I must join the data first, fill the NaN values using mean and mode methods, and delete unnecessary columns.
It orgininally contains 24 columns, after adding some features and delete unnecessary columns it become 28 columns. 

The data distribution on numerical features mostly not normally distributed. Means the distribution curve did not shape like a bell, or most of the data are not centered near mean value.
On the categorical values there is no unique condition like some features tends to more affecting the attrition rate than the others, mostly it is because the composition of the population, higher population in a category also mean higher attrition. Like, most of the employee are in Sales department, so the Sales department has the highest att
Attrition rate.

### 2. Modelling

The models used in this platform in Random Forest Regressor with accuracy score around 98%. Score with original data gained score :

Model | Accuracy Score | Second Header | F! Score | Log Loss
------------ | ------------ | ------------- | ------------- | -------------
Random Forest Classifier | 0.992063 | 0.953020 | 0.975945 | 0.274117	
