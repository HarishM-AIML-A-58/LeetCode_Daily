import os
import re

def update_problem_readme(readme_path, problem_title, difficulty, date, solution_code, problem_statement):
    new_content = f"""
# 🌟 {problem_title}

> 📏 **Date:** {date}  
> 🌟 **Difficulty:** `{difficulty}`  
> 📚 **Category:** LeetCode Solutions  

---

## 📚 Problem Statement  
{problem_statement}

---

## 💪 Solution Approach  
🔹 **Key Concepts Used:**  
- Explain briefly what approach was used to solve the problem.

🔹 **Complexity Analysis:**  
- 🫠 **Time Complexity:** O(...)  
- 📂 **Space Complexity:** O(...)  

---

## 🖥️ Solution Code  
```python
{solution_code}
```

---

### 🚀 Run & Test  
```bash
python {problem_title.replace(" ", "_")}.py
```

---

### 🔗 More Solutions  
📌 [Back to main README](../../README.md)
"""
    with open(readme_path, "w", encoding="utf-8") as readme:
        readme.write(new_content)

def update_main_readme(repo_path, leetcode_path):
    main_readme_path = os.path.join(repo_path, "README.md")
    entries = ["# 🚀 LeetCode Daily Streak\n\n## 📌 Solved Problems\n\n"]

    for difficulty in ["Easy", "Medium", "Hard"]:
        difficulty_path = os.path.join(leetcode_path, difficulty)
        if not os.path.exists(difficulty_path):
            continue

        for date_folder in sorted(os.listdir(difficulty_path), reverse=True):
            date_path = os.path.join(difficulty_path, date_folder)
            if not os.path.isdir(date_path):
                continue

            readme_path = os.path.join(date_path, "README.md")
            if os.path.exists(readme_path):
                with open(readme_path, "r", encoding="utf-8") as file:
                    title_line = file.readline().strip().replace("# 🌟 ", "")

                entry = f"📌 **[{date_folder}]** - [{title_line}](LeetCode/{difficulty}/{date_folder}/README.md) `{difficulty}`\n"
                entries.append(entry)

    with open(main_readme_path, "w", encoding="utf-8") as main_readme:
        main_readme.writelines(entries)

def main():
    repo_path = os.path.abspath(os.path.dirname(__file__))
    leetcode_path = os.path.join(repo_path, "LeetCode")

    for difficulty in ["Easy", "Medium", "Hard"]:
        difficulty_path = os.path.join(leetcode_path, difficulty)
        if not os.path.exists(difficulty_path):
            continue

        for date_folder in os.listdir(difficulty_path):
            date_path = os.path.join(difficulty_path, date_folder)
            if not os.path.isdir(date_path):
                continue

            readme_path = os.path.join(date_path, "README.md")
            if os.path.exists(readme_path):
                with open(readme_path, "r", encoding="utf-8") as file:
                    content = file.read()

                title_match = re.search(r"# (.+)", content)
                problem_title = title_match.group(1).strip() if title_match else "Unknown Problem"
                
                statement_match = re.search(r"## Problem Statement\n(.+?)##", content, re.DOTALL)
                problem_statement = statement_match.group(1).strip() if statement_match else "No problem statement found."
                
                solution_match = re.search(r"```python\n(.+?)```", content, re.DOTALL)
                solution_code = solution_match.group(1).strip() if solution_match else "No solution found."
                
                update_problem_readme(readme_path, problem_title, difficulty, date_folder, solution_code, problem_statement)

    update_main_readme(repo_path, leetcode_path)
    print("✅ All README files updated successfully!")

if __name__ == "__main__":
    main()