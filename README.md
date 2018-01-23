# H1-B Visa Project
## Inspiration
Due to the recent turbulence surrounding the changing political climate on immigration we thought that an app that helped determine the probability of one being eligible for H-1B visa would be useful. This app would help employers as well as people who want to know their chances for being eligible for an H-1B visa.

## Background 
An H-1B visa is a visa issued by the U.S. government to foreign workers looking to work in specialty occupations (ex. law, science, engineering). In order for an H-1B visa to be issued, a company must sponsor the individual seeking employment. Even if a foreign worker is sponsored, H1-B visas are capped at 65,000 a year, and are given by lottery. Furthermore, for a company to even sponor an H1-B visa in the first place, it must submit a Labor Condition Application (LCA) to the U.S. Department of Labor. The ACL contains information to convince the U.S. Department of Labor that it will not pay a particular H1-B worker less than an American. The LCA application contains the following information:
  1. Employer Name
  2. Classification within the Standard Occupational Classification System (What kind of job is required by the employer?)
  3. Full Time Position (Y/N)
  4. Prevailing Wage
  5. Year
  6. Worksite (Where the employer is located)
 
## Motivation
H-1B visas cost employers about $5,000 (including government fees) per employee. Immigration lawyer fees cost on average $2,000 to $3,000, while filing fees are usually about $3,000. Employers must also have enough money in the bank necessary to pay the H-1B employee’s salary for a reasonable period of time. Therefore, it is within the best interest of an employer to determine if a workers LCA application will be certified before racking these costs.

## How it Works
Our app asks for the data specific to a prospective employee that a company wants to hire. Using the training data of past employers and their LCA applications given by the Department of Labor on their website (https://www.foreignlaborcert.doleta.gov/performancedata.cfm), we optimize a machine learning algorithm that will determine whether or not a particular employee's LCA application will be approved. 

## Dependencies
Our project uses a machine learning script written in Python. For our machine learning we used the Scikit-learn library, and for data proccessing, we used the Pandas library. Our app is written using Android's development studio and Amazon's Web Service.

## Comparisons of Classification Schemes Used
80/20 Train/Test Split
1. Support Vector Machine
  91.3% Accuracy when accounting for inbalances in data (50/50 split)
2. KNNeighbors
  97.2% Accuracy when accounting for inbalances in data (50/50 split)
