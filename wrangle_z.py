
import pandas as pd
from env import host, user, password

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

url = f'mysql+pymysql://{user}:{password}@{host}/zillow'


# Walk through the steps above using your new dataframe. You may handle the missing values however you feel is appropriate.
# df.head()
# df.tail(10)
# df.describe()
# df.shape
# df.info() #total_charges are an object, but need to be float
# df.isnull().sum() # can't eval whether there are nulls because of total_charges is the wrong type
# df.total_charges.value_counts()
# df.replace(r'^\s*$', np.nan, regex=True, inplace=True) #replace missing values with nan
# df.total_charges.value_counts()
# df = df.dropna() #drop non-numbers
# df.info()
# df.total_charges = df.total_charges.astype('float') #save series as 
# df.info()



# End with a python file wrangle.py that contains the function, wrangle_telco(), that will acquire the data and return a dataframe cleaned with no missing values.

def wrangle_zillow():
    zillow_data = pd.read_sql('''SELECT 
	propertylandusedesc AS 'Property Description',
    bathroomcnt AS 'Number of Bathrooms',
    bedroomcnt AS 'Number of Bedrooms',
    calculatedfinishedsquarefeet AS 'Square Feet',
    taxvaluedollarcnt AS 'Tax Appraised Value',
    taxamount AS 'Assessed Tax',
    fips AS 'County Number'
FROM propertylandusetype AS plut
	JOIN properties_2017 AS prop17
		ON plut.propertylandusetypeid = prop17.propertylandusetypeid
	JOIN predictions_2017 AS pred17
		ON pred17.id = prop17.id
	WHERE plut.propertylandusetypeid IN (261,262,273,275,279) 
		AND (pred17.transactiondate >= '2017-05-01' AND pred17.transactiondate <= '2017-06-30')
        AND bathroomcnt > 0
        AND bedroomcnt > 0
		AND calculatedfinishedsquarefeet >0
		AND	taxvaluedollarcnt > 0
		AND	taxamount > 0
		AND fips > 0;''', url)
    zillow_data.replace(r'^\s*$', np.nan, regex=True, inplace=True)  
    zillow_data = zillow_data.dropna()
    return zillow_data


