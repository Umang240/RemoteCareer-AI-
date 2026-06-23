from app.database.role_skills import role_skills


def analyze_skill_gap(target_role: str, current_skills: list):

    required_skills = role_skills.get(target_role)

    if not required_skills:
        return {
            "error": f"No skill data found for role: {target_role}"
        }

    missing_skills = list(
        set(required_skills) - set(current_skills)
    )

    return {
        "target_role": target_role,
        "missing_skills": missing_skills
    }