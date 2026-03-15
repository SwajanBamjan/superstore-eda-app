import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# App title and description
st.title("Superstore Sales and Profit Explorer")
st.write(


    """
    This dashboard allows business analysts to interactively explore the
    Superstore retail dataset. Use the sidebar controls to filter product 
    categories and choose how regional sales are broken down. The visualizations
    and summary tables below help uncover what drives profitability across
    products, regions, and customer segments.

    """ 


)


# Load Dataset
@st.cache_data

def load_data():
    df = pd.read_csv("superstore.csv", encoding = "latin-1")
    return df

df = load_data()


# Sidebar Controls
st.sidebar.header("Controls")


# Input 1: Filter scatter plot by Product Category
category_options = ["All"] + sorted(df["Category"].unique().tolist())
selected_category = st.sidebar.selectbox(
    "Filter Scatter Plot by Category",
    category_options
)


# Input 2: Choose how to break down the regional bar chart
group_var = st.sidebar.selectbox(
    "Group Regional Sales by",
    ["Segment", "Category"]
)


# Input 3: Control the sixe of scatter plot points
point_size = st.sidebar.slider(
    "Scatter Point Size",
    min_value = 10,
    max_value = 100,
    value = 30
)

# Filter Data for Scatter Plot

# If "All" is selected, use the full dataset, otherwise filter by category
if selected_category == "All":
    scatter_df = df.copy()
else:
    scatter_df = df[df["Category"] == selected_category]


# Primary Plot: Scatter Plot - Sales vs. Profit
st.subheader("Sales vs. Profit by Product Category")
st.write(
    "Each point represents a single order. Points below the red dashed line "
    "are loss-making transactions. Use the sidebar to filter by category or "
    "adjust point size."
)


# Assign a distinct color for each product category
category_colors = {
    "Furniture":         "#E07B54",
    "Office Supplies":   "#5B8DB8",
    "Technology":        "#4CAF82",


}

fig1, ax1 = plt.subplots(figsize = (8,5))


# Plot each category as a separate series so the legend is informative
for cat in scatter_df["Category"].unique():
    cat_data = scatter_df[scatter_df["Category"] == cat]
    ax1.scatter(
        cat_data["Sales"],
        cat_data["Profit"],
        label = cat,
        color = category_colors.get(cat, "gray"),
        alpha = 0.5,
        s = point_size
    )


    # Red dashed horizontal line marks the break-even point 
ax1.axhline(0, color='red', linestyle="--", linewidth=1, label="Break-even Line")

ax1.set_title(f"Sales vs. Profit - Category: {selected_category}", fontsize=13)
ax1.set_xlabel("Sales ($)")
ax1.set_ylabel("Profit ($)")
ax1.legend(title="Category")

st.pyplot(fig1)


# Seconday Plot: Grouped Bar Chart - Avg Sales by Region

st.subheader(f"Average Sales by Region - Grouped by {group_var}")
st.write(
    f"Compare average order sales across the four U.S. regions, broken down by "
    f"{group_var}. This helps identify which regional segments drive the most revenue."
)


# Calculate average sales for each region x group_var combination
grouped = (
    df.groupby(["Region", group_var])["Sales"]
    .mean()
    .reset_index()
)
grouped.columns = ["Region", group_var, "Average Sales"]


# Pivot so each group_var becomes it's own bar series
pivot = grouped.pivot(index="Region", columns=group_var, values="Average Sales")

fig2, ax2 = plt.subplots(figsize=(8, 5))
pivot.plot(kind="bar", ax=ax2, colormap="Set2", edgecolor="white", width=0.7)

ax2.set_title(f"Average Sales by Region and {group_var}", fontsize=13)
ax2.set_xlabel("Region")
ax2.set_ylabel("Average Sales ($)")
ax2.legend(title=group_var)
ax2.tick_params(axis='x', rotation=0)


st.pyplot(fig2)


# Ouput 1: Summary Statistics

st.subheader("Summart Statistics")
st.write(
    "Descriptive statistics for Sales and Profit based on the current category filter."
)
st.write(scatter_df[["Sales", "Profit"]].describe())



# Output 2: Aggregated Performance Table

st.subheader(f"Average Sales and Profit by Region and {group_var}")
st.write(
    f"This table summarizes average Sales and Profit for every Region x {group_var} "
    "combination. Managers can quickly spot high and low performing segments."
)


# Group the fill dataset and round for readability
agg_table = (
    df.groupby(["Region", group_var])[["Sales", "Profit"]]
    .mean()
    .round(2)
    .reset_index()
)
agg_table.columns = ["Region", group_var, "Avg Sales ($)", "Avg Profit ($)"]

st.dataframe(agg_table)


