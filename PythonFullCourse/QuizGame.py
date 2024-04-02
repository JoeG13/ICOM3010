# Quiz game: A simple quiz game where the user answers questions
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question("What is the capital of France? ", "Paris"),
    Question("Who wrote 'Romeo and Juliet'? ", "Shakespeare"),
    Question("What is the largest planet in the solar system? ", "Jupiter")
]

score = 0
for question in questions:
    user_answer = input(question.prompt)
    if user_answer.lower() == question.answer.lower():
        score += 1

print("You got", score, "out of", len(questions), "questions correct.")
