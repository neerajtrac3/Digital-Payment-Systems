# ------------------------------------------------------------
# ERMI Score Calculator
# Author: Neeraj Aggarwal
# Description:
#   Computes the Enterprise Risk Modernization Index (ERMI)
#   score based on 5 dimensions of resilience:
#   Architectural, Operational, Data, Security, Organizational.
#   Each dimension is scored 0–5 and weighted to produce a
#   final ERMI score (0–100).
# ------------------------------------------------------------

# ERMI dimension weights (in percentage)
WEIGHTS = {
    "architectural": 0.25,
    "operational": 0.25,
    "data": 0.20,
    "security": 0.20,
    "organizational": 0.10
}

def calculate_ermi_score(scores):
    """
    Calculate the ERMI score.

    Parameters:
        scores (dict): Dictionary containing scores (0–5) for:
            - architectural
            - operational
            - data
            - security
            - organizational

    Returns:
        float: Final ERMI score (0–100)
    """

    # Validate input
    for key in WEIGHTS.keys():
        if key not in scores:
            raise ValueError(f"Missing score for dimension: {key}")
        if not (0 <= scores[key] <= 5):
            raise ValueError(f"Score for {key} must be between 0 and 5.")

    # Weighted score calculation
    final_score = 0
    for dimension, weight in WEIGHTS.items():
        final_score += scores[dimension] * weight * 20  # convert 0–5 scale to 0–100

    return round(final_score, 2)


# ------------------------------------------------------------
# Example Usage
# ------------------------------------------------------------
if __name__ == "__main__":
    example_scores = {
        "architectural": 3.5,
        "operational": 2.0,
        "data": 3.0,
        "security": 2.5,
        "organizational": 4.0
    }

    ermi_score = calculate_ermi_score(example_scores)
    print("ERMI Score:", ermi_score)
