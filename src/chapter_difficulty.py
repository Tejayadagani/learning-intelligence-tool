def detect_chapter_difficulty(df):
    """
    Identifies difficult chapters using dropout,
    average score, and time spent.
    """

    chapter_stats = df.groupby("chapter_order").agg(
        avg_score=("score", "mean"),
        avg_time_spent=("time_spent", "mean"),
        dropout_rate=("completion_status", lambda x: 1 - x.mean())
    ).reset_index()

    chapter_stats["difficulty_score"] = (
        chapter_stats["dropout_rate"] * 0.5 +
        (1 - chapter_stats["avg_score"] / 100) * 0.3 +
        (chapter_stats["avg_time_spent"] / chapter_stats["avg_time_spent"].max()) * 0.2
    )

    return chapter_stats.sort_values("difficulty_score", ascending=False)
