# NBASalaryAnalysis
```
merged_dataset2.csv -Dataset with all the stats
cleanedup_data.csv -Cleaned up dataset with all the stats
nba_eda.csv -Data from the analysis
```



This project will analyze NBA players' salaries based on their performance in the 2019-2020 NBA regular season. The project will compare their performace to their salary.

# Data Collection
NBA players' salaries, as well as basic stats, and advanced stats were scrapped off NBA reference and combined into a single dataset.

# Data Cleaning
Duplicates and empty values were removed in order to avoid inconsistent data. If players played for more than one team during the regular season, their total performance on both teams were taken, instead of their performance on invididual teams.

# Data Analysis
The correlation coefficient was used to compare players' stats and their salary to see how much they correlated with each other. This was used in determining features and models that would best fit the data. Graphs and models such as boxplot, pivot tables, and seaborn were also used to visualize the data.

# Model Building
Random Forest Regressior, Linear Regression, and Ada Boost Regressor were regression models that were used to measure the r^2 score and the mean value square root error.
