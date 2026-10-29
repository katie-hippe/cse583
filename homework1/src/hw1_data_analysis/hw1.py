# katie 
# homework 1
# oct 27

# 0. get set up 
import pandas as pd
import matplotlib.pyplot as plt

# 1. read the csv file into a pandas dataframe
df = pd.read_csv("src/hw1_data_analysis/bicycle_data.csv")

# 2. describe the columns in the df and update data types
print(df.dtypes)
# date: string (this should probably be updated to datetype)
# Fremont bridge Sidewalks (south of 34th) total: float64, should be integer?
                                            # for storage space?
# "" cyclist west sidewalk: float64, change to int
# "" cyclist east sidewalk: float64, change to int

# first we'll change all float columns to int
cols = [
    "Fremont Bridge Sidewalks, south of N 34th St Total",
    "Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk",
    "Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk",
]

# update all at once
df[cols] = df[cols].astype("Int64")

# now we can manage the date
df['datetime'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %I:%M:%S %p')

# 3. Add columns to the dataframe containing:
#       the total (east + west bicycle count)
#       the hour of the day
#       the year

# the total 
# isn't this already a column? redefine it anyway
df['count'] = df["Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"] + df["Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"]

# the hour
df['hour'] = df['datetime'].dt.hour

# and the year 
df['year'] = df['datetime'].dt.year

# 4. create a new dataframe with the subset of data from the year 2016

# subset to just year is 2016
df_2016 = df[df['year'] == 2016]
print(df_2016.shape)

# 5. deal with any missing data 

# subset to just the na values?
print(df_2016[df_2016.isna().any(axis=1)])
# there is just one row with missing data...
# setting it to zero or removing the row would accomplish the same thing,
# because we're doing counts, so let's remove the row

df_2016 = df_2016[~(df_2016.isna().any(axis=1))]
print(df_2016.shape)

# 6. plot the counts by hour (i.e. hour of the day on the x-axis, total daily counts on the y-axis)

# first let's figure out the total counts per hour
# this is just indexed by hour, so across all days 
df_2016_hourly = df_2016[['hour','count']].groupby('hour', as_index=False).sum()

# now we can plot

# set up fig size so y axis label doesn't get cut off
plt.figure(figsize=(8.0, 4.8))
plt.plot(df_2016_hourly['hour'], df_2016_hourly['count'])

# add main title and axes labels
plt.title("Busiest Hours for Bicycles")
plt.xlabel("Hour (Military)")
plt.ylabel("Bicycle count on Fremont bridge (S of N 34th St)")

# now save it :D
plt.savefig('src/hw1_data_analysis/counts_by_hour.png')

# 7. figure out the busiest hour

print(df_2016_hourly[df_2016_hourly['count'] == max(df_2016_hourly['count'])])
# according to this, the busiest hour is 17 (5pm), which makes sense
# as many people would be taking bikes home from work