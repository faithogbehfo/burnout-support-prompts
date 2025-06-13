"""
burnout_prompt_chatbot.py

A simple command-line chatbot that delivers AI-generated burnout support prompts.
Blends psychology + AI to demonstrate prompt delivery and user interaction.
Created by Faith Ogbefho for the Bonsai Prompt Design Fellowship.
"""

import random
import time

# Prompt bank
burnout_prompts = [
    "What's weighing on your mind today? Let's unpack it.",
    "List 3 things you’re proud of, even if they seem small.",
    "What’s one boundary you can set today to protect your peace?",
    "Describe a moment this week when you felt joy or calm.",
    "If your burnout had a voice, what would it say? How would you answer?",
    "It’s okay to feel overwhelmed — you’re not alone.",
    "You’ve been carrying a lot. Would you like to talk about it?",
    "Take a breath. What are 5 things you see, 4 you can touch, 3 you can hear, 2 you can smell, and 1 you can taste?"
]

def deliver_prompt():
    print("\n🤖 AI Support Bot: Welcome! I'm here to guide you through a quick reflection.")
    time.sleep(1)
    prompt = random.choice(burnout_prompts)
    print(f"\n🧘 Prompt: {prompt}")
    input("\n(Press Enter when you're ready to continue...)\n")
    print("✅ Thank you for taking a moment for yourself. You’re doing great.\n")

if __name__ == "__main__":
    while True:
        deliver_prompt()
        again = input("Would you like another prompt? (y/n): ").lower()
        if again != 'y':
            print("🌟 Take care of yourself today!")
            break
