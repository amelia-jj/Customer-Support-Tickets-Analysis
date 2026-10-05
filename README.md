# Customer-Support-Tickets-Analysis

An analysis of a 20,000-ticket customer support dataset, examining what actually influences customer satisfaction (CSAT) - response time, resolution time, priority, category, and sentiment. Drawing on my background of over two years in customer support, I focused on questions I know matter in practice, rather than just those that are easy to measure.

Tools: Python (pandas) for analysis, Power BI for an interactive dashboard, and a dataset sourced from Kaggle.


Here is the analysis and interpretations:

Firstly, I checked every single cell to count how many missing values exist in the DataFrame. In this case, since it's synthetic dataset, there were no missing values.

Then, I compared CSAT in relation to response and resolution time:
CSAT vs response time: -0.12;
CSAT vs resolution time: -0.39

Summary: customers care more about getting their problem solved quickly than about getting a fast first reply. 

I checked the average satisfaction within each category group separately, but the result revealed that category alone doesn't explain the huge satisfaction swing. Although, there's still a clear pattern: Shipping has the lowest average CSAT (3.18), while Account issues score highest (3.44). It means that shipping-related tickets show the lowest average satisfaction, suggesting this category may need closer attention.

Resolution time by priority behaves sensibly:

Urgent: 11.5 hours,
High: 12.6 hours,
Medium: 15.6 hours,
Low: 21.4 hours

This shows that the support system is doing what it should - urgent tickets get resolved fastest, and low-priority tickets wait longest.

But satisfaction barely moves across priority levels:

Urgent: 3.34, High: 3.30, Medium: 3.31, Low: 3.35 - all nearly identical

Even though Urgent tickets get resolved almost twice as fast as Low priority tickets, their satisfaction scores are pretty much the same. Despite the big difference in how fast tickets are actually handled, priority level and resolution speed don't seem to directly drive satisfaction.

Resolution time overall did correlate with CSAT (like I mentioned earlier: customers care more about getting their problem solved quickly than about getting a fast first reply), but that relationship doesn't seem to be explained by priority. Despite urgent requests getting faster service, this does not lead to a significant increase in customer satisfaction. This suggests that the cause of dissatisfaction may be elsewhere (perhaps the quality of communication or some unresolved issue, rather than the speed of service itself).

So, do negative reports tend to be more common in certain areas?

Billing, Shipping and Technical Issue tickets are entirely tagged Negative.
Account and Product Inquiry tickets have no Positive sentiment at all, split only between Negative and Neutral.
Feedback is the only category with any Positive sentiment.

Since this is a synthetic dataset, it is possible that artificially generated data has categories with no variation sentiment-wise.

To confirm, I filtered the dataset to Billing tickets only and checked which sentiment values appeared among them. The result confirmed that certain ticket categories show no sentiment variation at all in this data.

The spread of CSAT across channel is small (3.31 to 3.33), so channel doesn't appear to meaningfully drive satisfaction on its own.


Summary:

Average resolution time: 15.3 hours;
Zero missing data across all columns;
CSAT correlates more with resolution time (-0.39) than response time (-0.12);
Resolution time drops with priority (Urgent: 11.5h → Low: 21.4h), but CSAT barely changes across priority levels;
Shipping has the lowest average CSAT by category; Account the highest;
Billing, Shipping and Technical Issue tickets are 100% negative sentiment in this dataset 
