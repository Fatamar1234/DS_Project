Who Lives Near Virginia's Data Centers?
The question

Are neighborhoods within 3 miles of a data center in Virginia lower-income or more minority than Virginia as a whole?

Data centers use a lot of power, land, and water. We wanted to see if they tend to be built near certain kinds of communities.

How we answer it (in plain English)
Find where the data centers are.
Draw a 3-mile circle around each one.
Mark every census tract that touches a circle as "near a data center."
Look up the income and race numbers for each tract.
Compare the "near" tracts to the Virginia average.

What's a census tract? A neighborhood-sized area drawn by the U.S. Census Bureau, usually 1,200 to 8,000 people. Virginia has about 2,200 of them. It's the smallest area where the Census shares reliable income and race numbers.

The data
#	Dataset	What it gives us	Key columns	Source
1	Tract income (ACS 5-year, table S1901)	Median household income per tract and for Virginia	GEO_ID, households, median income, margin of error	data.census.gov
2	Tract race and ethnicity (ACS 5-year, table B03002)	Who lives in each tract	GEO_ID, total population, non-Hispanic White alone	data.census.gov
3	Tract boundaries (TIGER/Line 2024)	The shape of every tract, so we can map them and measure distance	GEOID, ALAND, geometry	Census TIGER/Line
4	Data center locations (Cleanview)	Where data centers are	name, latitude, longitude, status, operating year, county	Cleanview API docs

How they connect: every tract has an ID (GEOID). The income and race tables use the same ID, so we can match them to the tract shapes. The data center points are then placed on the tract map.

Key definitions
Near a data center: a tract that falls within 3 miles (about 4,828 meters) of a data center. [Fill in: touches the circle, or tract center is inside it.]
Percent minority: everyone who is not non-Hispanic White, calculated as 1 - (B03002_003E / B03002_001E).
Which data centers count: [Fill in: Operating only, or also Under Construction.]
Virginia average: the state-level value from the same Census tables, used as our comparison point.
Cleaning steps
Tracts: keep GEOID, NAMELSAD, COUNTYFP, ALAND, geometry. Remove water-only tracts (ALAND = 0). Reproject to EPSG:5070 so distances are in meters.
Income and race: make sure the ID matches the tract file. Turn income into numbers (some values are text). Keep margins of error.
Data centers: keep Virginia, keep the statuses we chose, remove rows with no coordinates, and count each campus once.
Tools

Python, pandas, GeoPandas, Jupyter Notebook.

Results

[Add after the analysis. Example: "Tracts near data centers had a median income X% higher/lower than the Virginia median."]

Limitations
The Census income and race numbers are estimates and have margins of error, especially in small tracts.
Some data centers have missing coordinates and are left out.
Tracts near the Virginia border may be close to data centers in other states that we don't count. [Update if neighboring states are included.]
Being near a data center doesn't prove the data center caused anything. This project only looks at who lives nearby.
Team
Role	Person
Income data (S1901)	Robertsan
Race and ethnicity data (B03002)	Aquilla
Tract boundaries (TIGER)	Abigail
Data center locations (Cleanview)	Fatama
Data credits
U.S. Census Bureau, American Community Survey 5-Year Estimates (2020-2024)
U.S. Census Bureau, TIGER/Line Shapefiles (2024)
Cleanview data center database
