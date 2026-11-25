# Layer 02: Plotting sales tax revenue from data centers lost among states

# -- Import Libraries --
import pandas as pd
import matplotlib.pyplot as plt


# -- Load CSV --
df=pd.read_csv(r"C:\Users\abiga\Downloads\verified_data_center_tax_exemptions_by_state.csv")

# -- Data Cleaning --
# Keep only real states (drop the average/median rows and states with no annual number)
states = df[df["cost_type"] != "benchmark"]
states = states.dropna(subset=["annual_cost_millions"])

# --Bar Graph Creation --

fig, ax = plt.subplots(figsize=(8,5)) #size

ax.bar(states["state"], states["annual_cost_millions"], color= 'darkblue', label="Annual excemption cost") # x=state names y=costs in millions

fig.set_facecolor('lightgrey') #background color
ax.set_facecolor('lightblue') #background color

plt.title("Data Centers Sales Tax Exemption Cost by State", fontsize=16, fontweight='heavy', color='darkgreen') #title
plt.suptitle("Sources: State Agencies and Good Job First", fontsize=10, fontweight='light', color='lightgreen') #subtitle

#plot average
plt.axhline(436.9, linestyle='--',color='red', linewidth=2, label='Average of 13 states with data ($437M)') 

plt.xlabel("State", color='blue', fontsize=12) #x-axis label
plt.ylabel("Annual Exemption Cost (Millions)", color='purple', fontsize=12) #y-axis label

plt.legend(facecolor='lightgrey', fontsize=10, edgecolor='black') #legend
plt.grid(axis='y', color='black', linestyle=':') #gridlines

plt.tight_layout() #layout
plt.savefig(r"C:\Users\abiga\Downloads\sales_tax_exemption_cost_by_state.png") #save figure
plt.show() #show figure