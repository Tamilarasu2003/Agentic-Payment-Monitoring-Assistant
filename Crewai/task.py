from crewai import Task
from agents import issue_identifier, failure_quantifier, solution_provider

def create_all_tasks(sample_data: str):
    task1 = Task(
        description=(
            f"You are tasked with thoroughly analyzing the provided sample of payment transaction data. "
            f"Identify any potential issues, anomalies, or suspicious activity within the dataset. "
            f"Focus your analysis on detecting failed payment requests, unusual transaction amounts, "
            f"irregular timing patterns, repeated failures, or any other indicators of payment processing problems. "
            f"Consider scenarios such as duplicate transactions, payment gateway errors, network timeouts, or fraudulent attempts. "
            f"Your findings should be detailed and actionable, specifying the nature and context of each issue, "
            f"and highlighting any patterns that suggest systemic problems or isolated incidents."
            f"\n\nSample data:\n{sample_data}"
        ),
        expected_output=(
            "A comprehensive report detailing all identified payment anomalies, including:\n"
            "- Classification of payment failure types (e.g., declined, timeout, invalid account)\n"
            "- Description of suspicious patterns such as repeated failures from the same account or IP\n"
            "- Detection of outlier amounts that may indicate errors or fraud\n"
            "- Timing-related irregularities (e.g., spikes in failure rates during specific periods)\n"
            "- Specific examples illustrating the issues found"
        ),
        agent=issue_identifier,
    )

    task2 = Task(
        description=(
            "Using the issues and anomalies detected in the previous task, quantify the impact on the overall payment system. "
            "Calculate the total number of failed payment requests, and break down these failures by their cause, frequency, and affected user segments. "
            "Assess how widespread each issue is and identify any trends over time or correlations with other data points. "
            "Your analysis should include clear numerical summaries, percentages, and, where relevant, segment-level insights (e.g., by geography or user type)."
        ),
        expected_output=(
            "A detailed failure quantification report including:\n"
            "- Total count and percentage of failed transactions\n"
            "- Breakdown of failures by error type or cause\n"
            "- Frequency and temporal distribution of failures\n"
            "- Identification of high-risk users or regions\n"
            "- Summary statistics highlighting the severity and scope of the payment issues"
        ),
        agent=failure_quantifier,
        depends_on=[task1],
    )

    task3 = Task(
        description=(
            "Based on the identified payment issues and their quantified impact, provide actionable recommendations to improve payment processing reliability. "
            "Suggest specific steps for remediation such as process changes, system enhancements, user education, or monitoring improvements. "
            "Include strategies for proactive detection and mitigation of future payment failures, and outline best practices for maintaining a healthy payment ecosystem."
        ),
        expected_output=(
            "A comprehensive set of practical solutions and recommendations including:\n"
            "- Remediation steps tailored to the most common and severe payment failure causes\n"
            "- Process and system improvements to reduce failure rates\n"
            "- Recommendations for real-time monitoring, alerts, and anomaly detection\n"
            "- Strategies for user engagement or manual intervention when needed\n"
            "- Best practices for ongoing payment system health checks and audits"
        ),
        agent=solution_provider,
        depends_on=[task2],
    )

    return [task1, task2, task3]
