def generate_insights(features, chapter_difficulty):
    """
    Converts predictions into human-readable insights.
    """

    high_risk_students = features[
        features["dropout_risk"] == 1
    ]["student_id"].tolist()

    difficult_chapters = chapter_difficulty.head(3)["chapter_order"].tolist()

    insights = {
        "high_risk_students": high_risk_students,
        "difficult_chapters": difficult_chapters,
        "average_completion_prediction": features["completion_prediction"].mean()
    }

    return insights
