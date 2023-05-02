import os
import pandas as pd
import helper_functions

def create_dataframe(data):
    # create dataframe from dict
    df = pd.DataFrame(data)
    df['URL'] = df['URL'].apply(helper_functions.make_hyperlink)
    return df

def create_directory(excel_directory):
     if not os.path.exists(excel_directory):
          os.makedirs(excel_directory)

def save_to_excel(writer, dataframe, sheet_name):
    # Create directory if one does not exist
    dataframe.to_excel(writer, index=False, sheet_name = sheet_name)

def average_price_per_model_code(dataframe):
    avg_price_per_model = dataframe.groupby(["Model Code"]).aggregate({'Model': 'max', "Model Code":'max', "Total Price USD":'mean',  "Color" : 'count'})
    avg_price_per_model = avg_price_per_model.astype({"Total Price USD": int})
    avg_price_per_model.rename(columns = {'Color':'Model Count', 'Total Price USD':'Average Price USD'}, inplace=True)
    return avg_price_per_model