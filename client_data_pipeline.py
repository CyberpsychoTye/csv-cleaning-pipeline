import pandas as pd

female_df = pd.read_csv("client_all_data.csv")

# Drops uncessary rows and columns
columns = female_df.columns
columns_to_drop = columns[0:17]
female_df.drop([1], axis = 0, inplace =True)
female_df.drop(columns_to_drop, axis = 1, inplace = True)

# Converts the data to "Float64" so that mathmatical operations can be performed on it.
female_df.drop([0], axis = 0, inplace = True)
female_df = female_df.astype("Float64")

# Groups the question responses into categories defined by the client
attitude_series = pd.concat([female_df["Q9"],female_df["Q10"]], ignore_index = True)
subjective_norms_series = pd.concat([female_df["Q11"],female_df["Q12"]], ignore_index = True)
perceived_behavioural_series = pd.concat([female_df["Q13"],female_df["Q14"]], ignore_index = True)
identity_series = pd.concat([female_df["Q4"],female_df["Q5"]], ignore_index = True)
intention_series = pd.concat([female_df["Q7"], female_df["Q8"]], ignore_index = True)

print(identity_series)
print(identity_series.describe())

# Creates the table specified by the client (broski baji)
index = ["Attitude", "Subjective Norms", "Perceived Behavioural Control", "Identity", "Intention"]
list_of_series = [attitude_series, subjective_norms_series, perceived_behavioural_series, identity_series, intention_series]
data = {"N": [ item.count() for item in list_of_series], "Min": [item.min() for item in list_of_series], "Max": [item.max() for item in list_of_series], "Mean": [round(item.mean(),2) for item in list_of_series], 
        "SD": [round(item.std(),2) for item in list_of_series]}

processed_female_df = pd.DataFrame(data = data, index = index)

# Exports the dataframe as an xlsx file, for compatibility with Excel
processed_female_df.to_excel("processed_all_data.xlsx")
