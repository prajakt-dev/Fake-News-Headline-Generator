import random

subjects = ["Sharukh  Khan", "Donald Trump", "Elon Musk", "Kim Kardashian", "Beyoncé", "Kirmada", "Chota Bheem", "Narendra Modi", "Nirmala Sitaram", "A Mumbai City"]

actions = ["launches", "cancels", "dance with","eat", "declare war on", "ordered"]

place_or_things = ["at red fort", "at dholapur", "in mumbai local train", "inside parlament", "on Rajkumari Indumati"]

while True:

    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)
    
    headline = f"BREAKING NEWS:{subject} {action} {place_or_thing}"

    print("\n" + headline)
    user_input = input("\n Do you want another headline ? (Yes/No): ").strip() .lower()

    if user_input == "no":
      break

print("\nThanks for using Fake News Generator!")
