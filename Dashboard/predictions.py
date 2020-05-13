import pickle
from pandas import DataFrame, get_dummies

model = pickle.load(open('final_model.sav', 'rb'))
real_columns = pickle.load(open('original_column.sav','rb'))
one_hot_columns = pickle.load(open('x_dummies_column.sav', 'rb'))

def predictions(data):
    df = DataFrame(data, index=[0])
    df = get_dummies(df)
    df = df.reindex(columns=one_hot_columns, fill_value=0)
    hasil = model.predict(df)
    return round(hasil[0])