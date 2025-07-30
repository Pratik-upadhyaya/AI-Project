import tkinter as tk

def on_submit():
    try:
        # Get skill ratings as integers
        skill_ratings = {subject: int(entries[subject].get()) for subject in subjects}
    except ValueError:
        result_label.config(text="Please enter valid integers between 1 and 5 for all subjects.")
        return
    
    # Validate ratings range
    for rating in skill_ratings.values():
        if rating < 1 or rating > 5:
            result_label.config(text="Ratings must be between 1 and 5.")
            return

    total = sum(skill_ratings.values())
    
    # Avoid division by zero
    if total == 0:
        result_label.config(text="Please enter ratings greater than zero.")
        return

    # Calculate career match percentages
    careers = {
        "Engineer": skill_ratings["Math"] + skill_ratings["Science"] + skill_ratings["Computer"],
        "Doctor": skill_ratings["Science"] + skill_ratings["Health"],
        "Accountant": skill_ratings["Math"] + skill_ratings["Account"],
        "Teacher": skill_ratings["English"] + skill_ratings["Science"],
        "Software Developer": skill_ratings["Computer"] + skill_ratings["Math"],
        "Nurse": skill_ratings["Health"] + skill_ratings["English"]
    }

    # Convert scores to percentages
    career_percentages = {career: (score / (5 * 3)) * 100 for career, score in careers.items()}

    # Sort by highest match
    sorted_careers = sorted(career_percentages.items(), key=lambda x: x[1], reverse=True)

    # Format the result text
    result_text = "Career Recommendations:\n"
    for career, percent in sorted_careers:
        result_text += f"{career}: {percent:.1f}% match\n"

    result_label.config(text=result_text)

root = tk.Tk()
root.title("AI Career Guidance System")

subjects = ["Math", "Science", "English", "Computer", "Account", "Health"]
entries = {}

tk.Label(root, text="Rate your skills from 1 (low) to 5 (high):").grid(row=0, column=0, columnspan=2, pady=10)

for i, subject in enumerate(subjects, start=1):
    tk.Label(root, text=subject).grid(row=i, column=0, sticky="e", padx=5, pady=2)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=2)
    entries[subject] = entry

submit_btn = tk.Button(root, text="Get Recommendations", command=on_submit)
submit_btn.grid(row=len(subjects)+1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.grid(row=len(subjects)+2, column=0, columnspan=2, padx=10)

root.mainloop()
