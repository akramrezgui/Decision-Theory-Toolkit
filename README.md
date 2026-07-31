# Decision Theory & Quantitative Finance Toolkit

An interactive Python-based toolkit for exploring mathematical models of decision-making under uncertainty and their applications in finance.

This project aims to transform theoretical concepts from decision theory and financial economics into interactive simulations and visualizations, allowing users to understand not only the results of different models but also the reasoning behind them.

---

## 🎯 Project Objective

Decision-making often requires choosing between alternatives while facing uncertainty about future outcomes.

This repository explores how mathematical frameworks help answer questions such as:

* How should we choose between different alternatives when the future is unknown?
* How do different assumptions about risk affect decisions?
* Why do rational individuals make different choices?
* How can these concepts be applied to investment decisions?

---

# 📚 Topics Covered

## 1. Decision Matrix Analysis

Implementation of classical decision-making methods under uncertainty:

* Decision matrices
* States of nature
* Alternatives and outcomes
* Maximax criterion
* Maximin criterion
* Minimax Regret criterion
* Hurwicz criterion
* Laplace criterion

### Example

A decision-maker must choose between several projects while considering different economic scenarios:

| Project | Growth | Stable | Recession |
| ------- | ------ | ------ | --------- |
| A       | 100    | 50     | -20       |
| B       | 70     | 60     | 10        |
| C       | 40     | 40     | 40        |

The toolkit evaluates the decision using different criteria and shows how the recommended choice changes depending on the decision-maker's assumptions.

---

## 2. Decisions Under Risk

Planned additions:

* Expected value
* Probability-weighted outcomes
* Expected utility theory
* Risk preferences

---

## 3. Utility Theory

Planned additions:

* Utility functions
* Risk-neutral preferences
* Risk-averse preferences
* Risk-seeking preferences
* Utility visualization

---

## 4. Quantitative Finance Applications

Future modules:

* Portfolio theory
* Risk-return analysis
* Diversification
* Efficient frontier
* Portfolio optimization
* Monte Carlo simulations

---

# 🛠️ Technologies Used

* Python
* Streamlit
* NumPy
* Pandas
* Plotly
* Matplotlib

---

# 📂 Repository Structure

```
Decision-Theory-Toolkit/

│
├── decision_matrix/
│   ├── app.py
│   ├── criteria.py
│   └── README.md
│
├── expected_utility/
│
├── utility_functions/
│
├── portfolio_theory/
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/decision-theory-toolkit.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 📊 Current Features

## Decision Matrix Analyzer

Currently implemented:

✅ Interactive payoff matrix input
✅ Multiple decision criteria
✅ Automatic calculation of scores
✅ Comparison between decision methods
✅ Visualization of results

---

# 🧠 Learning Approach

This project is developed alongside the study of:

* Decision theory
* Financial economics
* Portfolio management
* Risk analysis

Each module represents the implementation of a theoretical concept into a practical interactive tool.

---

# 🔮 Future Improvements

* Add Bayesian decision models
* Add expected utility simulations
* Add utility function explorer
* Add risk aversion analysis
* Add portfolio optimization models
* Add machine learning approaches for decision support

---

# 📖 References

* Martin Peterson — *An Introduction to Decision Theory*
* David G. Luenberger — *Investment Science*
* MIT OpenCourseWare — Finance Theory
* Modern Portfolio Theory — Harry Markowitz

---

# 👤 Author

**Akram Rezgui**

Finance & Data Analytics Student

Interested in quantitative finance, decision science, and AI-based financial applications.
