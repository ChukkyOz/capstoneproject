import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------
# 1. Load & Prepare Data
# ----------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv('C:\\Users\\Chukwuebuka Ozoh\\Downloads\\players.csv')  # adjust path
    if 'now_cost' not in df.columns:
        st.error("Dataset must contain a 'now_cost' column.")
        st.stop()
    df['cost_m'] = df['now_cost'] / 10.0
    df['value']  = df['total_points'] / df['cost_m']
    return df

fpl_data = load_data()

# Define key metrics
key_metrics = [
    'minutes', 'goals_scored', 'assists', 'clean_sheets',
    'expected_goals', 'expected_assists', 'expected_goal_involvements',
    'bonus', 'form', 'total_points'
]

# ----------------------------------------
# 2. Sidebar Filters
# ----------------------------------------
st.sidebar.header("🔧 Filters")
positions = sorted(fpl_data['position'].unique())
sel_pos = st.sidebar.multiselect("Position", options=positions, default=positions)

min_cost = float(fpl_data['cost_m'].min())
max_cost = float(fpl_data['cost_m'].max())
sel_cost = st.sidebar.slider("Cost Range (£m)", min_cost, max_cost, (min_cost, max_cost))

top_n = st.sidebar.number_input("Show Top N Picks", min_value=5, max_value=50, value=10)

# ----------------------------------------
# 3. Filtered Data & Top Picks
# ----------------------------------------
filtered = fpl_data[
    (fpl_data['position'].isin(sel_pos)) &
    (fpl_data['cost_m'] >= sel_cost[0]) &
    (fpl_data['cost_m'] <= sel_cost[1])
]
top_picks = filtered.sort_values('value', ascending=False).head(int(top_n))

# ----------------------------------------
# 4. Main Display
# ----------------------------------------
st.set_page_config(page_title="FPL Value Picks Dashboard", layout="wide")
st.title("💡 FPL Cost-Effective Stars")
st.markdown("Use historical performance metrics to identify the season's best value picks.")

st.subheader(f"🏆 Top {top_n} Value Picks")

# Build display columns without duplicating total_points
base_cols = ['name', 'team', 'position', 'cost_m', 'value']
metrics_without_target = [m for m in key_metrics if m != 'total_points']
display_cols = base_cols + ['total_points'] + metrics_without_target

st.dataframe(
    top_picks[display_cols]
        .rename(columns={
            'cost_m':'cost (£m)',
            'value':'pts per £m'
        }),
    height=400
)

# ----------------------------------------
# 5. EDA Visualization
# ----------------------------------------
st.subheader("📈 Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(
    fpl_data[key_metrics + ['value']].corr(),
    annot=True, fmt=".2f", cmap="coolwarm", ax=ax
)
ax.set_title("Correlation: Key Metrics vs. Value Score")
st.pyplot(fig)

# ----------------------------------------
# 6. Footer
# ----------------------------------------
st.markdown("---")
st.caption("Built by Chukwuebuka Ozoh | Capstone: Predicting FPL Performance | 2023–24 Season")
