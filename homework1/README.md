# Homework 1

This folder contains all the necessary files to accomplish
homework 1, which analyzes the bicycle data from the seattle
government on the fremont bridge to identify the busiest hour
for cycles across 2016.

## structure: 

homework1/                      -- parent folder
├── pyproject.toml            
├── README.md                   -- explanation of project
└── src/                      
  └── hw1_data_analysis/
        ├── __init__.py
        ├── hw1.py              -- script to analyze data
        ├── counts_by_hour.png  -- results   
        └── bicycle_data.csv    -- to download on own device


note that bicycle_data.csv comes from 
https://data.seattle.gov/Transportation/Fremont-Bridge-Hourly-Bicycle-Counts-by-Month-Octo/65db-xm6k. 

## process for doing homework:

- I set up the file structure using command prompts
    - this included various mkdir, cd, and curl commands
- For the python portion, I opened vscode using code .
    - then completed the task requirements
    - used AI in minor ways
        - googled an example of datetime and plots
        - I'd used each before but

## datetime:

I used pandas' built-in datetime format. This stores timestampls as an np array of 64-bit integers, and is vectorized to avoid memory overhead for the standard Python datetime object. It is faster than both the datatime.datetime and np.datetime (but pretty comparable to np.datetime) and has built-in timezoning support as well. 