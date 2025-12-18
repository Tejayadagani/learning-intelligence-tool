import argparse
from inference import run_inference
from chapter_difficulty import detect_chapter_difficulty
from insights import generate_insights

def main():
    parser = argparse.ArgumentParser(description="AI Learning Intelligence Tool")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    args = parser.parse_args()

    df, features = run_inference(args.input)
    chapter_difficulty = detect_chapter_difficulty(df)
    insights = generate_insights(features, chapter_difficulty)

    print("\n=== AI Learning Intelligence Report ===\n")
    print(insights)

if __name__ == "__main__":
    main()
