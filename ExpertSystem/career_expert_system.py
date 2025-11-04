import tkinter as tk
from tkinter import messagebox

def suggest_career():
    interests = interest_entry.get().lower()
    skills = skill_entry.get().lower()
    personality = personality_var.get().lower()     
    work_pref = work_type_var.get().lower()         

    # --- Rule-based Career Suggestions ---
    if "coding" in interests or "programming" in interests:
        if "math" in skills or "logic" in skills:
            if personality == "introvert":
                result = "Software Developer / Data Scientist"
            else:
                result = "AI Product Manager / Tech Consultant"
            reason = "You enjoy coding and have analytical thinking."

    elif "ai" in interests or "machine learning" in interests or "data" in skills:
        result = "AI / Machine Learning Engineer"
        reason = "You are interested in artificial intelligence and data."

    elif "biology" in interests or "medical" in interests:
        result = "Doctor / Nurse / Pharmacist"
        reason = "You like biology and helping people."

    elif "law" in interests or "debate" in interests or "public speaking" in skills:
        result = "Lawyer / Judge"
        reason = "You have strong communication and reasoning skills."

    elif "math" in interests or "accounting" in interests or "finance" in interests:
        result = "Chartered Accountant / Financial Analyst"
        reason = "You enjoy working with numbers and finance."

    elif "machines" in interests or "engineering" in interests:
        result = "Mechanical / Electrical Engineer"
        reason = "You like machines, engineering, and design."

    elif "construction" in interests or "architecture" in interests:
        result = "Civil Engineer / Architect"
        reason = "You are interested in buildings, structure, and design."

    elif "drawing" in interests or "art" in interests or "creativity" in skills:
        result = "Graphic Designer / Animator / UI-UX Designer"
        reason = "You are creative and enjoy visual design."

    elif "business" in interests or "entrepreneur" in interests:
        if personality == "extrovert":
            result = "Entrepreneur / Business Manager"
        else:
            result = "Business Analyst / Financial Consultant"
        reason = "You have leadership or analytical skills in business."

    elif "teaching" in interests or "education" in interests:
        result = "Teacher / Professor"
        reason = "You enjoy sharing knowledge and teaching others."

    elif "army" in interests or "police" in interests or "defense" in interests:
        result = "Defense / Army / Police"
        reason = "You are disciplined and interested in protecting the nation."

    elif "marketing" in interests or "social media" in interests:
        result = "Digital Marketer / Content Creator"
        reason = "You enjoy creativity and influencing people."

    elif "psychology" in interests or "mental health" in interests:
        result = "Psychologist / Counselor"
        reason = "You understand human behavior and emotions."

    elif "plants" in interests or "farming" in interests or "environment" in interests:
        result = "Agricultural Scientist / Environmentalist"
        reason = "You care about nature and agriculture."

    elif "travel" in interests or "tourism" in interests:
        result = "Hotel Management / Tourism Specialist"
        reason = "You enjoy meeting people, travel, and hospitality."

    # SMART SUGGESTIONS if no match is found 
    else:
        if "space" in interests:
            result = "Astronomer / Aerospace Engineer"
            reason = "You are interested in space and the universe."
        elif "music" in interests:
            result = "Musician / Sound Engineer"
            reason = "You love music and sound creation."
        elif "sports" in interests or "game" in interests:
            result = "Athlete / Sports Coach / Fitness Trainer"
            reason = "You enjoy physical activities and sports."
        else:
            result = "No clear career match found."
            reason = (
                "Try using more clear interests like:\n"
                "- Coding, Biology, Business, Drawing, Law\n"
                "- Psychology, Teaching, Engineering, Marketing\n"
                "\nTip: Use keywords like 'coding', 'doctor', 'art', 'law', etc."
            )

    
    messagebox.showinfo("Career Suggestion", f"Suggested Career: {result}\n\nReason: {reason}")


root = tk.Tk()
root.title("Career Guidance Expert System")
root.geometry("450x500")

tk.Label(root, text="Enter your interests:").pack()
interest_entry = tk.Entry(root, width=50)
interest_entry.pack()

tk.Label(root, text="Enter your skills:").pack()
skill_entry = tk.Entry(root, width=50)
skill_entry.pack()

tk.Label(root, text="Personality Type:").pack()
personality_var = tk.StringVar(value="introvert")
tk.Radiobutton(root, text="Introvert", variable=personality_var, value="introvert").pack()
tk.Radiobutton(root, text="Extrovert", variable=personality_var, value="extrovert").pack()

tk.Label(root, text="Preferred Work Type:").pack()
work_type_var = tk.StringVar(value="desk")
tk.Radiobutton(root, text="Desk Job", variable=work_type_var, value="desk").pack()
tk.Radiobutton(root, text="Field Work", variable=work_type_var, value="field").pack()

tk.Button(root, text="Get Career Suggestion", command=suggest_career).pack(pady=20)

root.mainloop()
