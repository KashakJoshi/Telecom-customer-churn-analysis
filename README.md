1.1 Project Overview and Business Context

This project analyzes customer churn in a telecom company using a purely analytical, data-driven approach without applying machine learning models.

The company is facing significant customer churn, which directly impacts revenue stability. While the overall churn rate appears moderate, the deeper concern lies in structural instability within specific customer segments.

The objective of this project was to:
	•	Identify structural churn drivers
	•	Quantify revenue exposure
	•	Build an interpretable risk scoring framework
	•	Simulate financial recovery scenarios
	•	Design a financially prioritized retention strategy

The focus is not just on predicting churn, but on understanding and monetizing churn risk.




1.2 Dataset Overview

The dataset contains 7043 customers and 21 features related to:
	•	Customer demographics
	•	Subscription details
	•	Contract type
	•	Internet services
	•	Billing and payment behavior
	•	Monthly charges and total charges
	•	Churn status

The data allows analysis of churn from multiple business angles including contract structure, payment behavior, lifecycle stage, and revenue contribution.





1.3 Key Insights and Findings

Overall churn rate: 26.5 percent
Revenue at risk: 30.5 percent

Strongest churn drivers:
	•	Tenure 0 to 6 months: 52.9 percent churn
	•	Month-to-month contract: 42.7 percent churn
	•	Electronic check payment: 45 percent churn
	•	Fiber optic users: 41.9 percent churn
	•	Senior citizens: 41.7 percent churn

Extreme risk cluster identified:

Month-to-month + Fiber optic
Churn rate: 54.6 percent
Monthly revenue churn from this cluster: over 100,000

This cluster represents a structurally unstable and financially vulnerable segment.

⸻




1.4 Risk Scoring Framework

A rule-based risk scoring model was developed using five high-risk signals:
	•	Month-to-month contract
	•	Fiber optic internet
	•	Electronic check payment
	•	Tenure less than or equal to 6 months
	•	Senior citizen

Each customer was assigned a risk score between 0 and 5.

Customers were grouped into:

Low Risk
Medium Risk
High Risk

Results:

Low Risk churn rate: 6.6 percent
Medium Risk churn rate: 37.6 percent
High Risk churn rate: 67.8 percent

The scoring framework demonstrated strong monotonic separation, validating its effectiveness without using machine learning.

⸻





⸻

1.5 Financial Impact and Scenario Modeling

Revenue recovery simulations were performed under different churn reduction assumptions.

Combined recovery for Month-to-month and Fiber optic segments:

10 percent churn reduction: 282,176 annual recovery
20 percent churn reduction: 564,353 annual recovery
30 percent churn reduction: 846,529 annual recovery
40 percent churn reduction: 1,128,706 annual recovery

Revenue response was linear and predictable, indicating strong financial elasticity.

Break-even retention cost estimation:

Target segment size: 3730 customers
Allowable retention cost per customer at 20 percent improvement: 151 per year

This provides a clear financial boundary for retention campaign budgeting.

⸻






⸻

1.6 Strategic Recommendations

Tier 1 – Immediate Intervention

Focus on Month-to-month and Fiber optic customers.
Introduce contract upgrade incentives and pricing alignment strategies.

Tier 2 – Behavioral Stabilization

Encourage auto-payment adoption among Electronic check users.
Offer small incentives for switching to automatic payment.

Tier 3 – Lifecycle Improvement

Improve onboarding for customers in their first six months.
Introduce early engagement and support programs.

Tier 4 – Demographic Sensitivity

Provide simplified support and billing assistance for senior customers.

Retention strategy should prioritize financial exposure, not just churn percentage.








⸻

1.7 Final Conclusion

Churn in the telecom business is not random. It is structurally concentrated within flexible contracts, high-value internet plans, early lifecycle customers, and manual payment users.

By combining risk profiling with financial modeling, this project transforms churn analysis into a strategic revenue optimization framework.

Even modest churn reduction efforts can produce substantial and predictable financial recovery.

This project demonstrates how structured data science thinking can guide executive-level business decisions without relying on complex machine learning models.






1.8 Interview-Ready Summary

In this project, I moved beyond simple churn analysis and built a multi-dimensional risk profiling framework that quantified financial exposure across customer segments.

I identified structurally unstable segments, developed an interpretable risk scoring model, and simulated revenue recovery under multiple improvement scenarios.

The final outcome was a financially prioritized retention strategy with measurable ROI and a break-even budget framework.

This demonstrates my ability to connect data analysis directly to business impact and decision-making.

⸻

