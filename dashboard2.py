import streamlit as st
#Reads, cleans, and analyzes your CSV dataset.
import pandas as pd
#Creates interactive graphs, charts, and maps.

import geopandas as gpd
import plotly.express as px
import json

import folium
from streamlit_folium import st_folium



# Set up the dashboard

st.set_page_config(
    #this is for the browser tab 
    page_title="Virginia Data Center Explorer",
    #I chose it to be narrow
    layout="wide"
)


# Load the cleaned CSV
df = pd.read_csv("_data_centers_clean.csv")

#title 
st.title("Virginia Data Center Explorer")
#subheading
st.write("Explore data center development across Virginia.")
st.warning(
    "Disclaimer: The information presented in this dashboard "
    "is based on publicly available data from Cleanview. "
    "As the data center industry continues to evolve, "
    "the data may not reflect the most recent developments "
    "or capture every data center in Virginia. "
    "This dashboard is intended for educational and research purposes."
)


# Sidebar filters
st.sidebar.header("Filter")

county = st.sidebar.selectbox(
    "Select County",
    ["All Counties"] + sorted(df["county"].dropna().unique().tolist())
)
#we are using multiselect to sort the status 
statuses = st.sidebar.multiselect(
    "Select Status",
    options=sorted(df["status"].unique())
)

filtered_df = df
if statuses:
    filtered_df = filtered_df[
        filtered_df["status"].isin(statuses)
    ]

if county != "All Counties":
    filtered_df = filtered_df[
        filtered_df["county"] == county
    ]


st.subheader("Data Center Overview")

# Find the county with the most matching data centers
top_county = filtered_df["county"].mode()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Data Center Records",
    len(filtered_df)
)



col2.metric(
    "Counties Represented",
    filtered_df["county"].nunique()
)

col3.metric(
    "Highest Concentration",
    top_county.iloc[0] if not top_county.empty else "N/A"
)







# Interactive map
st.subheader("Data Center Locations")

fig_= px.scatter_map(
    filtered_df,
    lat="latitude",
    lon="longitude",
    color="status",
    hover_name="project_name",
    hover_data=["county"],
    map_style="carto-positron",
    zoom=6,
    center={"lat": 37.5, "lon": -78.5},
    height=600
)

st.plotly_chart(fig_, key="locations_map")
st.subheader("Data Center Distribution by County")

# Load US county boundaries
url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"

us_counties = gpd.read_file(url)

# Select only Virginia (state FIPS code 51)
virginia = us_counties[us_counties["STATE"] == "51"].copy()
virginia["FIPS"] = virginia["STATE"] + virginia["COUNTY"]

county_counts = (
    filtered_df.groupby("county")
    .size()
    .reset_index(name="data_center_count")
)
county_counts["county"] = (
    county_counts["county"]
    .str.lower()
    .str.strip()
    .str.replace(r"\s+county$", "", regex=True)
)

virginia["county"] = (
    virginia["NAME"].str.lower().str.strip()
)

print(county_counts["county"].unique())

print(virginia["county"].unique())

virginia = virginia.merge(
    county_counts,
    on="county",
    how="left"
)

virginia["data_center_count"] = (
    virginia["data_center_count"].fillna(0).astype(int)
)

geojson = json.loads(virginia.to_json())

fig = px.choropleth(
    virginia,
    geojson=geojson,
    locations=virginia.index.astype(str),
    color="data_center_count",
    hover_name="NAME",
    color_continuous_scale="Blues",
    labels={"data_center_count": "Data Centers"}
)

fig.update_geos(
    fitbounds="locations",
    visible=False
)

fig.update_layout(
    height=600,
    margin={"r": 0, "t": 20, "l": 0, "b": 0}
)


st.plotly_chart(fig)



st.subheader("Operating Data Centers by County")

# Keep only operating data centers
operating_df = df[df["status"] == "Operating"]

# Count operating data centers in each county
operating_counts = (
    operating_df.groupby("county")
    .size()
    .reset_index(name="operating_count")
)

# Sort from highest to lowest
operating_counts = operating_counts.sort_values(
    by="operating_count",
    ascending=False
)
operating_counts["county"] = (
    operating_counts["county"].str.lower().str.strip()
)

virginia["county"] = (
    virginia["county"].str.lower().str.strip()
)

virginia.loc[
    virginia["FIPS"] == "51660",
    "county"
] = "harrisonburg city"

virginia.loc[
    virginia["FIPS"] == "51600", "county"
] = "fairfax city"

# Add FIPS codes from the Virginia dataset
operating_counts = operating_counts.merge(
    virginia[["county", "FIPS"]],
    on="county",
    how="left"
)

# Arrange the columns
operating_counts = operating_counts[
    ["county", "FIPS", "operating_count"]
]


# Display the table
st.dataframe(operating_counts, hide_index=True)
