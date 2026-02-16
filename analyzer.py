import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/marketing_data.csv")

# Calculate metrics
df["CTR"] = (df["clicks"] / df["impressions"]) * 100
df["Conversion_Rate"] = (df["conversions"] / df["clicks"]) * 100
df["ROAS"] = df["revenue"] / df["spend"]

# Rule-Based AI Logic
def generate_insights(row):
    insights = []

    if row["ROAS"] > 3:
        insights.append("High profitability campaign")
    else:
        insights.append("Low profitability, optimize budget")

    if row["CTR"] < 3:
        insights.append("Ad creative needs improvement")

    if row["Conversion_Rate"] < 5:
        insights.append("Landing page optimization required")

    return " | ".join(insights)

df["AI_Insights"] = df.apply(generate_insights, axis=1)

# Save report
with open("report.txt", "w") as f:
    for _, row in df.iterrows():
        f.write(f"Campaign: {row['campaign']}\n")
        f.write(f"Insights: {row['AI_Insights']}\n\n")

# Visualization
df.plot(x="campaign", y="ROAS", kind="bar", title="Campaign ROAS")
plt.tight_layout()
plt.show()

print("AI Marketing Analysis Completed!")
