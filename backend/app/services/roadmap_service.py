from app.database.roadmaps import roadmaps


def generate_roadmap(target_role: str):

    roadmap = roadmaps.get(target_role)

    if not roadmap:
        return {
            "error": f"No roadmap found for role: {target_role}"
        }

    return {
        "target_role": target_role,
        "roadmap": roadmap
    }