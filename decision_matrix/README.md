# Decision Matrix Analyzer

An interactive Python application for analyzing decisions under uncertainty using classical decision theory methods.

This project implements decision-making criteria that help compare alternatives when future outcomes are unknown. It allows users to create a payoff matrix, apply different decision rules, and visualize the results.

## 🎯 Project Objective

Many real-world decisions involve uncertainty:

- Choosing between investment projects
- Selecting business strategies
- Evaluating possible outcomes under different scenarios

Decision theory provides mathematical frameworks to help make rational choices depending on the decision-maker's assumptions about uncertainty.

This project transforms these theoretical concepts into an interactive tool.

---

# 📚 Implemented Concepts

## Decision Matrix

A decision matrix represents:

- Alternatives (possible choices)
- States of nature (possible future scenarios)
- Outcomes (payoffs associated with each combination)

Example:

| Alternative | Scenario 1 | Scenario 2 | Scenario 3 |
|------------|------------|------------|------------|
| A | 100 | 50 | -20 |
| B | 70 | 60 | 10 |
| C | 40 | 40 | 40 |

---

# Decision Criteria

The application currently supports:

## Maximax Criterion

Represents an optimistic decision-maker.

The chosen alternative is the one with the highest possible payoff.

---

## Maximin Criterion

Represents a pessimistic decision-maker.

The chosen alternative is the one with the best worst-case outcome.

---

## Minimax Regret Criterion

Chooses the alternative that minimizes the maximum possible regret.

Regret represents the opportunity loss from not choosing the best alternative after the state of nature is known.

---

# 🚀 Features

✅ Interactive payoff matrix input  
✅ Multiple decision criteria  
✅ Automatic calculation of scores  
✅ Comparison between different approaches  
✅ Visualization of decision results  
✅ User-friendly Streamlit interface  

---

# 🛠️ Technologies Used

- Python
- Streamlit
- NumPy
- Pandas
- Plotly

---

# 📂 Project Structure
