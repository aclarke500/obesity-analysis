# obesity-analysis
<body>
    <h1>Obesity Analysis of United States</h1>
    <p>Using data from data.gov</p>
    <a href="https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system">Available here: </a>
    <h3>Abstract</h3>
    <p>The goal with this is to analyze obesity rates by state. Namely, the percentage of people (18 and over) obese and the rate at which it is increasing. Obesity rates are increasing in every US state included in this dataset.</p>
    <h3>Methodology</h3>
    <p>For the sake of eloquance, I changed the name of the dataset to 'data.csv' to make it easier to reference. 
        First, I cleaned the data. I did this by removing every empty entry (indicated by a '~' footnote in the entry)' and concatenated this into a new csv.
        Next, I wrote a python method that takes in a state name. It makes a subset of the cleaned data, generates a plot and line of best fit for that state over all years with data.
        It saves the plot as a png and returns the slope of the line of best fit, average obesity rate, and the name of the state.
        I wrote a script that iterates over all states (computed as all unique entries in the 'LocationDesc' column) and calls the method on each state.
        I saved the results in a csv file. I iterated over the results and pulled out some interesting statistics.
    </p>
    <h3>Results</h3>
    <h2>Most Obese State</h2>
    <ul>
        <li>West Virginia</li>
        <li>Average Obesity Rate (2012-2021): 37.3%</li>
        <li>Rate of Increase: 0.7%</li>
    </ul>
    <h2>Least Obese State</h2>
    <ul>
        <li>Colorado</li>
        <li>Average Obesity Rate (2012-2021): 22.9%</li>
        <li>Rate of Increase: 0.4%</li>
    </ul>
    <h2>Highest Increase in Obesity</h2>
    <ul>
        <li>New Mexico</li>
        <li>Average Obesity Rate (2012-2020): 29.6%</li>
        <li>Rate of Increase: 0.9%</li>
    </ul>
    <h2>Slowest Increase in Obesity</h2>
    <ul>
        <li>Washington</li>
        <li>Average Obesity Rate (2012-2021): 28.4%</li>
        <li>Rate of Increase: 0.3%</li>
    </ul>
    <h2>Overall Increase of Obesity in the US</h2>
    <!-- New Mexico,29.556093758093763,0.8805384615384401,9 -->
    <a href="https://ibb.co/b1vVKmY"><img src="https://i.ibb.co/VVCGq9b/national-obesity-in-us.png" alt="national-obesity-in-us" border="0"></a>
    <p>As seen above, the number of obese people in the US is increasing year over year. Each year, 0.6% of the population (Just under 2 million people per year!!!) become obese.</p>
    </body>