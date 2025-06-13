"""
burnout_sample.py

Sample burnout-related AI prompts for emotional support.
Optimized for GPT-4 and wellness applications.
Designed by Faith Ogbefho – blending Psychology (B.A.) + AI (M.S.)

Built for Bonsai's AI Prompt Design Fellowship application.
"""

# Prompt categories and structured lists
prompt_categories = {
    "Self-Reflection": [
        "What does burnout feel like in your body right now?",
        "If your burnout had a voice, what would it say?",
        "What small act of care could you offer yourself today?"
    ],
    "Validation": [
        "It's okay to feel overwhelmed — you're not alone.",
        "You've been carrying a lot. Would you like to talk about it?",
        "What you're feeling is valid. Want to reflect together?"
    ],
    "Grounding": [
        "Take a breath. What are 5 things you see, 4 you can touch, 3 you can hear, 2 you can smell, and 1 you can taste?",
        "What's one thing in the room that makes you feel safe right now?",
        "Focus on your feet — how do they feel touching the ground?"
    ],
    "Reframing": [
        "What if burnout is your body’s way of asking for change?",
        "Can you think of a time you overcame something difficult before?",
        "What would rest look like if it were productive, too?"
    ]
}

# Function to list categories
def list_categories():
    return list(prompt_categories.keys())

# Function to get a random prompt from a chosen category
import random
def get_prompt(category):
    try:
        return random.choice(prompt_categories[category])
    except KeyError:
        return "Invalid category. Please choose from: " + ", ".join(list_categories())

# Example usage
if __name__ == "__main__":
    print("Prompt Categories:", list_categories())
    selected_category = "Grounding"  # change this to test other categories
    print("Prompt from '{}':".format(selected_category))
    print(get_prompt(selected_category))
