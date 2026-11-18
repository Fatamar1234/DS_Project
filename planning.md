# Virginia Data Centers, Income, and Demographics — Project Plan

## Research Question
**Do Virginia counties with data centers have lower median household income or a higher share of minority residents than the national average?**

## Project Overview
We will compare Virginia counties/county-equivalents that have data centers with U.S. national benchmarks for:
1. Median household income
2. Share of residents who are minorities (defined for this project as everyone except non-Hispanic White alone)

We will use a consistent data year or ACS 5-year period wherever possible, document the year and definitions, and avoid claiming that data centers *cause* differences. This is a descriptive comparison.

## Team Assignments

### 1. Roberstan — Income Dataset
**Dataset:** County median household income (Virginia counties and the U.S. national benchmark).

**Tasks:**
- Find and download median household income for Virginia counties/county-equivalents and the United States.
- Record the source, table/variable, year or 5-year period, and units (USD).
- Keep the original downloaded file unchanged in `raw_data/`.
- Create a cleaned file containing county name or county FIPS, median household income, and the national median household income benchmark (or a separate national benchmark file).
- Create a plot showing county median household income for counties with data centers, with the national benchmark clearly marked. If helpful, also show counties without data centers as a comparison group.
- Write 2–4 sentences explaining the chart and any caveats.

**Suggested source:** U.S. Census Bureau American Community Survey (ACS), county median household income (use the same ACS vintage for county and national values).

### 2. Aquilla — Minority Population Dataset
**Dataset:** County population and race/ethnicity data used to calculate minority share, for Virginia counties/county-equivalents and the U.S.

**Tasks:**
- Download county total population and non-Hispanic White-alone population, plus national equivalents, for the same year/period as the income data if possible.
- Save the original download(s) unchanged in `raw_data/`.
- Calculate minority population as `total population - non-Hispanic White alone population`.
- Calculate minority share as `minority population / total population * 100`.
- Create a cleaned file with county name or FIPS, total population, non-Hispanic White-alone population, minority population, minority share (%), and national minority-share benchmark.
- Create a plot comparing the minority share of counties with data centers against the national benchmark. If helpful, include counties without data centers as a comparison group.
- Write 2–4 sentences explaining the chart, the minority definition, and caveats.

**Minority definition for this project:** Minority share = 100% − (non-Hispanic White-alone population ÷ total population × 100). State the definition in the chart and report.

### 3. Fatama — Data Center Dataset
**Dataset:** Identify Virginia counties/county-equivalents that have data centers.

**Tasks:**
- Find a credible source/list/map of data center locations in Virginia.
- Count the number of data centers in each county.
Save the cleaned dataset for the group.
- Save the original source/download in `raw_data/` (or save a source copy and document its URL and retrieval date if no downloadable file is available).
- Determine which county or county-equivalent each location is in; deduplicate locations as needed.
- Produce a cleaned county-level file with county name/FIPS and a binary indicator: `has_data_center` (1 = yes, 0 = no). Include a count of data center facilities by county if the source supports it.
- Document the definition of a data center and any limitations in coverage (for example, source may not list every facility).
- Create a plot or map showing Virginia counties with and without identified data centers. This is the geographic/context plot for the project.
- Write 2–4 sentences describing the distribution and data limitations.

### 4. Group Leader — Abigail (Project Coordination, Merge, Analysis, and Final Plot)
**Dataset/workstream:** Combined analysis dataset and national comparison/synthesis.

**Tasks:**
- Create and maintain this plan, project checklist, and README notes; coordinate deadlines and make sure each person commits their work.
- Confirm the three datasets use compatible geography (county/county-equivalent), years/periods, and definitions. Track any differences in a source-notes file.
- Review the three members’ cleaned files and source notes for completeness and consistency.
- Merge the cleaned income, minority, and data-center files using county FIPS when available (prefer FIPS to county names to avoid spelling/name mismatches).
- Create the final analysis file with one row per Virginia county/county-equivalent and columns for income, minority share, and data-center status.
- Calculate descriptive comparisons: average/median income and average/median minority share for counties with identified data centers; compare with the national benchmark. Optionally, calculate the same county summaries for counties without identified data centers.
- Create the final comparison plot(s): a summary chart of data-center counties vs. national income and minority-share benchmarks, and/or side-by-side plots for the two outcomes.
- Draft the findings/conclusion and limitations; assemble the report/slides and ensure the team’s plots have readable titles, units, legends, source notes, and captions.
- Check that the repository is organized, reproducible, and that the README explains how to run the analysis.

**Leader's deliverables:** merged analysis file (saved in `processed_data/`), final comparison plot(s) (saved in `plots/`), summary of findings, final README/report/slides.


## Repository Folder Rules

**All raw/original downloads must go in `raw_data/`. Do not edit raw files.** Make a copy or create a cleaned version for processing.

Suggested structure:

```text
project-repository/
├── planning.md
├── README.md
├── raw_data/              # Original downloads; leave unchanged
├── processed_data/         # Cleaned datasets and merged analysis data
├── notebooks/              # Analysis notebooks (optional)
├── scripts/                # Python scripts (optional)
├── plots/                  # Saved charts and map(s)
└── sources/                # Source links, retrieval dates, and data notes
```

If the folders do not exist yet, create them. Each member should commit their cleaned file, plot, and source notes when their task is complete.

## Workflow / How to Complete the Project

### Step 1 — Download and document the data
- Use credible, clearly documented sources (prefer Census/ACS for demographic and income estimates).
- Use the same ACS vintage or 5-year period for the county and national figures.
- For each source, record: source name, URL, table/variable names, year/period, date downloaded, geographic level, and any caveats.
- Save the original download in `raw_data/` with a descriptive filename. Example: `raw_data/acs_income_original.csv`.

### Step 2 — Clean each dataset separately
- Never overwrite the original file in `raw_data/`.
- Keep only the fields needed for this project, rename columns clearly, standardize county names, and keep county FIPS codes if available.
- Save the cleaned file to `processed_data/` using a clear filename, for example:
  - `processed_data/county_income_clean.csv`
  - `processed_data/county_minority_clean.csv`
  - `processed_data/virginia_data_centers_clean.csv`
- Add a short source/method note in `sources/` for each dataset.

### Step 3 — Make individual plots
- Each dataset owner makes the plot described in their assignment.
- Every plot needs a descriptive title, labeled axes, units/percent signs where applicable, a legend or benchmark line if needed, and a source note.
- Save plots as PNG files in `plots/`. Use clear filenames such as `income_counties_vs_us.png`, `minority_share_counties_vs_us.png`, and `virginia_data_centers_map.png`.
- Make the plot readable: avoid overcrowded county labels; sort bars if using bar charts; choose an appropriate chart type.

### Step 4 — Merge and compare (Group Leader)
- Merge the three cleaned datasets on county FIPS code, if available.
- Verify that every Virginia county/county-equivalent appears once and that the merge did not duplicate rows.
- Identify the counties with `has_data_center = 1`.
- Compare their income and minority-share summaries with the national benchmarks.
- Clearly state how the group summarized counties (mean or median) and do not mix these two statistics.

### Step 5 — Final interpretation
Address each part of the research question separately:
- **Income:** Is the typical median household income among Virginia counties with data centers lower or higher than the national household-income benchmark?
- **Minority share:** Is the typical minority share in Virginia counties with data centers higher or lower than the national benchmark?
- Report the number of Virginia counties included and how many had identified data centers.
- Note that county-level findings cannot tell us about individuals and do not establish that data centers caused any income or demographic pattern.

## Recommended Visualizations

1. **Income chart (Roberstan):** County median household income for identified data-center counties; add a horizontal line for U.S. median household income. Optionally add a comparison group for Virginia counties without identified data centers.
2. **Minority-share chart (Aquilla):** Minority share (%) for identified data-center counties; add a horizontal line for the U.S. minority share. Optionally compare counties without identified data centers.
3. **Data-center map (Fatama):** Virginia county map or another clear geographic visualization showing counties with identified data centers versus counties without.
4. **Final summary chart (Abigail):** Side-by-side summary of data-center county median income and minority share compared with the U.S. benchmarks, with values labeled.

## Shared Quality Checklist

- [ ] All original datasets are saved in `raw_data/` and left unchanged.
- [ ] Every dataset has a source URL and retrieval date.
- [ ] County FIPS codes are included wherever possible.
- [ ] Geography and data years/periods are consistent or differences are documented.
- [ ] Income is in USD and clearly labeled with its ACS period/inflation-adjusted year.
- [ ] Minority-share definition is stated and calculated consistently for counties and national data.
- [ ] Data-center county classification has a source and limitations note.
- [ ] Cleaned datasets are saved in `processed_data/`.
- [ ] Plots are saved in `plots/` with clear labels and captions.
- [ ] Merged data has one row per county/county-equivalent and no accidental duplicate rows.
- [ ] Final report answers both parts of the research question and includes limitations.
- [ ] All members have reviewed the final results and their contribution is committed to GitHub.

## Suggested GitHub Collaboration

- Each member should work on their own branch or separate files to avoid conflicts.
- Use descriptive commit messages, such as `add county income dataset and plot`.
- Open a pull request or ask the group leader to review before merging to the main branch.
- Avoid committing temporary files, duplicate downloads, or files containing credentials.

## Source Guidance

- Prefer the U.S. Census Bureau's ACS data tables for income and population characteristics. The ACS provides detailed tables and data tools for counties and national geographies.
- Choose a consistent ACS vintage/period for all comparisons, and document any limitations or margins of error where available.
- For minority share, use a clearly stated definition and apply it identically to Virginia counties and the U.S. national figure.
- The data-center list/map may come from a different source and year; document what the source includes and what it may omit.
