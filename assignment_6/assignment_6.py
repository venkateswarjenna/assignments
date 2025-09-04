import os
import re

# Path where all book reviews are stored
REVIEWS_DIR = "book_reviews"

# Predefined sentiment words
positive_words = [
    "interesting", "inspiring", "amazing", "beautiful", "masterpiece",
    "engaging", "thoughtful", "captivating", "brilliant", "insightful",
    "enjoyable", "fascinating", "heartwarming", "uplifting", "well-written",
    "entertaining", "unique", "powerful", "compelling", "impressive"
]

negative_words = [
    "boring", "confusing", "waste", "slow", "terrible",
    "disappointing", "predictable", "weak", "messy", "poor",
    "dull", "unrealistic", "dragging", "forgettable", "annoying",
    "overrated", "clumsy", "shallow", "unconvincing", "frustrating"
]


# Ensure reviews directory exists
if not os.path.exists(REVIEWS_DIR):
    os.makedirs(REVIEWS_DIR)

def analyze_sentiment(text):
    """Detects positive or negative sentiment in the review using regex."""
    pos_count = sum(len(re.findall(rf"\b{word}\b", text, re.IGNORECASE)) for word in positive_words)
    neg_count = sum(len(re.findall(rf"\b{word}\b", text, re.IGNORECASE)) for word in negative_words)

    if pos_count > neg_count:
        return "Positive Review 📖✨"
    elif neg_count > pos_count:
        return "Negative Review 📉"
    else:
        return "Neutral Review 😐"

def read_reviews():
    """Read and analyze all reviews in the folder."""
    files = os.listdir(REVIEWS_DIR)
    if not files:
        print("No reviews found.")
        return

    print("\nAvailable Reviews:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")

    choice = input("Enter review number to analyze (or 'all' for all reviews): ")

    if choice.lower() == "all":
        for file in files:
            filepath = os.path.join(REVIEWS_DIR, file)
            with open(filepath, "r") as f:
                content = f.read()
                print(f"\n📄 {file}: {analyze_sentiment(content)}")
    else:
        try:
            idx = int(choice) - 1
            filepath = os.path.join(REVIEWS_DIR, files[idx])
            with open(filepath, "r") as f:
                content = f.read()
                print(f"\n📄 {files[idx]}: {analyze_sentiment(content)}")
        except (ValueError, IndexError):
            print("Invalid choice.")

def create_review():
    """Create a new book review file with content."""
    filename = input("Enter new review filename (with .txt): ")
    filepath = os.path.join(REVIEWS_DIR, filename)

    if os.path.exists(filepath):
        print("Review already exists.")
        return

    content = input("Enter review content: ")
    with open(filepath, "w") as f:
        f.write(content)
    print("Review created successfully.")

def modify_review():
    """Edit an existing book review."""
    files = os.listdir(REVIEWS_DIR)
    if not files:
        print("No reviews to modify.")
        return

    print("\nAvailable Reviews:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")

    try:
        idx = int(input("Choose review number to edit: ")) - 1
        filepath = os.path.join(REVIEWS_DIR, files[idx])

        with open(filepath, "r") as f:
            old_content = f.read()
        print("\nOld Content:")
        print(old_content)

        new_content = input("\nEnter new content: ")
        with open(filepath, "w") as f:
            f.write(new_content)
        print("Review updated successfully.")

    except (ValueError, IndexError):
        print("Invalid choice.")

def main():
    while True:
        print("\n--- Book Review Sentiment Checker ---")
        print("1. Read & Analyze Reviews")
        print("2. Create New Review")
        print("3. Modify Existing Review")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            read_reviews()
        elif choice == "2":
            create_review()
        elif choice == "3":
            modify_review()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
