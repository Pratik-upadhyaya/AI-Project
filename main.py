def get_user_input():
    print("Rate your proficiency in the following subjects from 1 (low) to 5 (high):")
    subjects = ["Math", "Science", "English", "Computer", "Account", "Health"]
    ratings = {}
    for subject in subjects:
        while True:
            try:
                rating = int(input(f"{subject}: "))
                if 1 <= rating <= 5:
                    ratings[subject] = rating
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input, please enter a number.")
    return subjects, ratings

career_requirements = {
    "Engineer": {"Math": 4, "Science": 3, "English": 2, "Computer": 4},
    "Accountant": {"Account": 4, "Math": 3, "English": 2},
    "Teacher": {"English": 4, "Health": 3, "Science": 2},
    "Doctor": {"Science": 5, "Health": 4, "Math": 3},
    "Software Developer": {"Computer": 5, "Math": 4, "English": 3},
    "Nurse": {"Health": 5, "Science": 4, "English": 3},
}

def match_careers(user_ratings, career_requirements):
    scores = {}
    for career, reqs in career_requirements.items():
        score = 0
        total = 0
        for subject, req_rating in reqs.items():
            total += req_rating
            user_rating = user_ratings.get(subject, 0)
            score += min(user_rating, req_rating)
        scores[career] = score / total if total > 0 else 0
    return scores

if __name__ == "__main__":
    subjects, ratings = get_user_input()
    career_scores = match_careers(ratings, career_requirements)
    sorted_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)

    print("\nCareer Recommendations:")
    for career, score in sorted_careers:
        print(f"{career}: {score*100:.1f}% match")
