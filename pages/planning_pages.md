# pages/ folder

This folder holds one Python file for each **layer** of the Data Center Footprint dashboard. Streamlit turns every `.py` file in this folder into its own page in the app's sidebar menu, so each teammate can build and test their layer separately and then add it to the shared site.

## How it works

- Each `.py` file in this folder becomes one page of the dashboard.
- The number at the start of the file name sets the order in the menu (`1_` first, `2_` second, and so on).
- The rest of the file name becomes the page title. Underscores turn into spaces (`1_Tax_Exemptions.py` shows as "Tax Exemptions").
- Files that are not `.py` (like this README) are ignored by Streamlit.

## Current layers

| File | Layer | Owner | Data |
|------|-------|-------|------|
| `1_Tax_Exemptions.py` | Annual data center sales tax exemption cost by state | Abigail | `data/verified_data_center_tax_exemptions_by_state.csv` |
| `2_Heatmap.py` | County-level map of data center presence and demographics | Whole team | (add file) |

Add a new row here when you add a new layer.

## Rules for adding a layer

1. **Build and test your chart as a plain Python script first**, then copy it into this folder.
2. **Edit only your own file.** This avoids conflicts when several people push to GitHub. The heatmap is built by the whole team, so for `2_Heatmap.py` pull the latest version from GitHub before you edit it, and tell the team when you push a change.
3. **Add `import streamlit as st` at the top** and show your chart with Streamlit instead of `plt.show()`:
   - Matplotlib charts: `st.pyplot(fig)`
   - Plotly charts: `st.plotly_chart(fig)`
4. **Use paths inside the repo, not paths on your computer.** Read data from the shared `data/` folder, for example `pd.read_csv("data/your_file.csv")`. Do not use paths like `C:\Users\...`.
5. **Do not save images to your own computer.** Remove any `plt.savefig(r"C:\Users\...")` line, or save to a relative path.
6. **Add any new library to `requirements.txt`** in the main folder so the deployed site can install it.
7. **Add a short note under your chart** with the data source, the year, and any limits of the data (for example, states that do not publish their costs).

## Running the dashboard locally

From the main project folder (the one with `app.py`), run:

```
streamlit run app.py
```

Your page appears in the sidebar menu.

## Deploying

The site is published from this GitHub repo with Streamlit Community Cloud. Once your file is pushed to GitHub, the live site updates with your page.
