from flask import Flask, render_template, request
from data import travel, department, edu, edu_field, gender, job_level, job_role, marital, stock_option, environment, job_satisf, work_life, job_involve, performance
from predictions import predictions
from plots import scatter, hist
from sqlalchemy import create_engine
import pandas as pd



## translate to python object
app = Flask(__name__)

engine = create_engine("mysql+mysqlconnector://root:12345@localhost/clean_data?host=localhost?port=3306")
conn = engine.connect()
result = conn.execute('SELECT * from clean_data.cleaned_data').fetchall()
df = pd.DataFrame(result, columns = result[0].keys())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/', methods =['GET','POST'])
def prediction():
    if request.method == "POST":
        data = request.form
        data = data.to_dict()
        data['Age']                     = int(data['Age'])
        data['DistanceFromHome']        = int(data['DistanceFromHome'])
        data['MonthlyIncome']           = int(data['MonthlyIncome'])
        data['NumCompaniesWorked']      = int(data['NumCompaniesWorked'])
        data['PercentSalaryHike']       = int(data['PercentSalaryHike'])
        data['TotalWorkingYears']       = int(data['TotalWorkingYears'])
        data['TrainingTimesLastYear']   = int(data['TrainingTimesLastYear'])
        data['YearsAtCompany']          = int(data['YearsAtCompany'])
        data['YearsSinceLastPromotion'] = int(data['YearsSinceLastPromotion'])
        data['YearsWithCurrManager']    = int(data['YearsWithCurrManager'])
        data['Absence']                 = int(data['Absence'])
        hasil = predictions(data)
        return render_template ('result.html', hasil_prediction=hasil)
    return render_template('prediction.html',data_travel = travel, data_department=sorted(department),data_edu=sorted(edu), data_eduField = edu_field, 
    data_gender=gender, data_jobLevel = job_level,data_jobRole = job_role, data_marital=marital, data_stockOption=stock_option, data_environment = environment, 
    data_satisf=job_satisf, data_worklife=work_life, data_jobinvolve=job_involve, data_performance=performance)

@app.route('/data')
def data():
    data = df
    return render_template('tabel_data.html' ,data=data)

@app.route('/plots')
def plots():
    plot1 = scatter()
    plot2 = hist()
    return render_template('plots.html', plot_1=plot1, plot_2=plot2)

if __name__ == "__main__":
    app.run(debug=True, port=5000)