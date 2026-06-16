from app.database.career_mapping import career_mapping

def get_career_recommendations(interests):
    recommendations = []

    for interest in interests:
        if interest in career_mapping:
            recommendations.append(career_mapping[interest])

    return recommendations
    