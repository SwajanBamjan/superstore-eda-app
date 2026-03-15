# Superstore Sales and Profit Explorer

> An interactive EDA dashboard built with Python and Streamlit.

---

## Description

The application that has been developed for this project is an interactive EDA application using the Python and Streamlit library to assist business analysts in carrying out an EDA of the sample Superstore retail data available on Kaggle. The sample data contains informaton about more than 9,900 retail orders received in the U.S. for various categories of retail orders, customers, geographical locations, sales, profit, discount, and Quantity. The business question that this dashboard is meant to anser is: What drives profitability, and where is the loss happening, across products, regions, and customers. There is the option to filter the data shown on the scatter plot based on product category, select the group variable used to create the bar chart shown on the right, and adjust the appearance of the plot via the sidebar. The primary visualization is a actter plot that displays the relationship between Sales and Profit at an individual order level, allowing for easy identification of orders that are making a loss. The secondary visualization is a grouped bar chart that displays a comparision of average sales performance across the four regions in the U.S., grouped by Segment or Category. To aid these plots, a table for summary statistics and a table for aggregated performance provide more numerical data for sales and profits for regions and categories. these tools allow manager and analysts to easily see areas of the business that performing well and areas of the business that could use more strategic planning. 

---

## Tool Used

| Tool | Purpose |
|------|---------|
| **Python** | This is the programming language that is used to develop the entire application. |
| **Streamlit** | This is an open-source framework that is used for developing and deploying the interactive web dashboard. |
| **pandas** | This is used for loading, filtering, grouping, and aggregating the data. |
| **Matplotlib** | This is used for developing the visualization for the scatterplot and grouped bar chart. |


 ## How to Run the Project 

 **1. Download the dataset**
 
 The dataset `superstore.csv` is already included in the repository.


 **2. Install dependencies**

 Open a terminal in the project folder and run:

 `pip install -r requirement.txt`
 
 
 **3. Launch the app**

 `streamlit run app.py`


 **4. Open the dashboard**

 streamlit will automatically open a browser and run the app


 **5. Use the sidebar controls**

 - To filter the scatter plot by product category
 - To choose a grouping variable for the regional bar chart
 - To adjust the scatter point size


 ---


 ### Business Analysis and Insights

 The scatter plot indicates that there is a very percentage of orders below the break-even point, and the category of furniture has maximum losses, as the sales values are very high and profits are negative pointing towards aggressive discounting being the reasson. Technology experiences the best sales-profit relationship, as the orders are very high above the break-even point, making it the most profitable category. From the grouped bar chart, it is clear that all the regions of East and West and performing better than the regions of Central and South. Also, Corporate and Home Offices are doing better in terms of average order value compared to Consumers. The aggregated performance table also indicates that technology in East and West regions contributes to high returns, while Furniture in the South and Central regions reults is losses. These results indicate that managers should review the discount strategy for underperforming categories and regions. and invest more in high-margin categories where profitability has already been established. 