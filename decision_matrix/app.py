import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Interactive Decision Criteria Calculator")

# --- Step 1: Upload or Manual Input ---
upload = st.file_uploader("Upload payoff matrix (CSV or Excel)", type=["csv", "xlsx"])

if upload:
    # Load uploaded file
    if upload.name.endswith(".csv"):
        df = pd.read_csv(upload, index_col=0)
    else:
        df = pd.read_excel(upload, index_col=0)

    st.write("### Uploaded Data")
    st.dataframe(df)

    # Expect last row to be probabilities
    if "Probabilities" in df.index:
        probs = df.loc["Probabilities"].values
        df = df.drop("Probabilities")  # remove probability row from payoff matrix
        st.success("Probabilities loaded from file.")
    else:
        st.warning("No 'Probabilities' row found. Please enter manually.")
        probs = np.array([st.number_input(f"Probability of {col}", value=1.0/len(df.columns), min_value=0.0, max_value=1.0, key=f"prob-{col}") for col in df.columns])

    alternatives = df.index.tolist()
    states = df.columns.tolist()

else:
    # Manual entry fallback
    n_alts = st.number_input("Number of alternatives", min_value=2, value=3)
    n_states = st.number_input("Number of states", min_value=2, value=3)

    alternatives = [st.text_input(f"Name of alternative {i+1}", f"Alt{i+1}") for i in range(n_alts)]
    states = [f"State{j+1}" for j in range(n_states)]

    st.subheader("Enter Payoff Matrix")
    matrix = []
    for i in range(n_alts):
        row = []
        for j in range(n_states):
            val = st.number_input(f"Payoff for {alternatives[i]} in {states[j]}", value=0.0, key=f"{i}-{j}")
            row.append(val)
        matrix.append(row)

    df = pd.DataFrame(matrix, index=alternatives, columns=states)
    st.write("### Payoff Matrix")
    st.dataframe(df)

    # Probabilities
    st.subheader("Probabilities of States")
    probs = np.array([st.number_input(f"Probability of {states[j]}", value=1.0/len(states), min_value=0.0, max_value=1.0, key=f"prob-{j}") for j in range(len(states))])

if abs(probs.sum() - 1.0) > 1e-6:
    st.warning("Probabilities should sum to 1.")

# --- Step 2: Hurwicz alpha ---
alpha = st.slider("Hurwicz alpha (optimism index)", 0.0, 1.0, 0.6)

# --- Step 3: Decision Criteria Functions ---
def maximax(df): return df.max(axis=1)
def maximin(df): return df.min(axis=1)
def minimax_regret(df):
    regret = df.apply(lambda col: col.max() - col)
    return -regret.max(axis=1)
def laplace(df): return df.mean(axis=1)
def hurwicz(df, alpha): return alpha*df.max(axis=1) + (1-alpha)*df.min(axis=1)
def expected_value(df, probs): return df.dot(probs)

# --- Step 4: Compute Results ---
results = pd.DataFrame({
    "Maximax": maximax(df),
    "Maximin": maximin(df),
    "Minimax Regret": minimax_regret(df),
    "Laplace": laplace(df),
    "Hurwicz": hurwicz(df, alpha),
    "Expected Value": expected_value(df, probs)
})

st.write("### Decision Criteria Results")
st.dataframe(results)

# Winners
st.write("### Winners per Criterion")
for criterion in results.columns:
    best_alt = results[criterion].idxmax()
    best_score = results[criterion].max()
    st.success(f"{criterion}: {best_alt} (Score = {best_score})")

# --- Step 5: Visualization ---
highlight_df = results.reset_index().melt(id_vars="index", var_name="Criterion", value_name="Score")
highlight_df["Color"] = ["green" if row["Score"] == results[row["Criterion"]].max() else "gray" for _, row in highlight_df.iterrows()]

fig = px.bar(highlight_df, x="index", y="Score", color="Color", facet_col="Criterion",
             labels={"index":"Alternative"}, title="Decision Criteria Comparison by Alternative")
st.plotly_chart(fig)

# --- Step 6: Explanations ---
st.write("### Explanations")
for criterion in results.columns:
    best_alt = results[criterion].idxmax()
    best_score = results[criterion].max()
    st.write(f"According to **{criterion}**, {best_alt} is chosen with a score of {best_score}.")

# --- Step 7: Download Results ---
csv = results.to_csv().encode("utf-8")
st.download_button("Download Results as CSV", csv, "decision_results.csv", "text/csv")
from io import BytesIO

# --- Step 7: Multi-sheet Excel Export ---
output = BytesIO()
with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
    # Sheet 1: Payoff Matrix
    df.to_excel(writer, sheet_name="Payoff Matrix")
    
    # Sheet 2: Results
    results.to_excel(writer, sheet_name="Decision Results")
    
    # Sheet 3: Explanations
    explanations = []
    for criterion in results.columns:
        best_alt = results[criterion].idxmax()
        best_score = results[criterion].max()
        explanations.append([criterion, best_alt, best_score, f"According to {criterion}, {best_alt} is chosen with a score of {best_score}."])
    exp_df = pd.DataFrame(explanations, columns=["Criterion","Winner","Score","Explanation"])
    exp_df.to_excel(writer, sheet_name="Explanations", index=False)
    
    # Optional formatting
    workbook  = writer.book
    for sheet in ["Payoff Matrix","Decision Results","Explanations"]:
        worksheet = writer.sheets[sheet]
        worksheet.set_column(0, 10, 20)

excel_data = output.getvalue()
st.download_button("Download Full Analysis (Excel)", excel_data, "decision_analysis.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
