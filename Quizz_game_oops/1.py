
class Question:
    """
    A simple class to store a quiz question with its options and correct answer
    """
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options  
        self.correct_answer = correct_answer  
    
    def display_question(self):
        """Display the question and its options in a formatted way"""
        print(self.question_text)
        for i, option in enumerate(self.options):
            print(f"{chr(97 + i)}) {option}")  

class Quiz:
    """
    Main quiz class that manages questions, scoring, and user interaction
    """
    def __init__(self):
        self.questions = [] 
        self.score = 0      
        self.total_questions = 0
    
    def add_question(self, question):
        """Add a question object to the quiz"""
        self.questions.append(question)
        self.total_questions += 1
    
    def start_quiz(self):
        """Main method to run the entire quiz"""
        print("🎯 Welcome to the Simple Quiz Game! 🎯")
        print("=" * 40)
        
      
        for i, question in enumerate(self.questions):
            print(f"\nQ{i + 1}: ", end="")
            question.display_question()
            
            
            while True:
                user_answer = input("Your Answer (a/b/c/d): ").lower().strip()
                if user_answer in ['a', 'b', 'c', 'd']:
                    break
                print("Please enter a valid option (a, b, c, or d)")
            
            
            if user_answer == question.correct_answer:
                self.score += 1
                print(f"✅ Correct! Score: {self.score}")
            else:
                print(f"❌ Wrong! Correct answer was: {question.correct_answer}")
                print(f"Score remains: {self.score}")
        
       
        self.show_results()
    
    def show_results(self):
        """Display final quiz results"""
        print("\n" + "=" * 40)
        print("🏆 QUIZ COMPLETED! 🏆")
        print(f"Final Score: {self.score}/{self.total_questions}")
        
      
        percentage = (self.score / self.total_questions) * 100
        print(f"Percentage: {percentage:.1f}%")
        
       
        if percentage >= 80:
            print("🌟 Excellent work!")
        elif percentage >= 60:
            print("👍 Good job!")
        elif percentage >= 40:
            print("👌 Not bad, keep practicing!")
        else:
            print("📚 Keep studying and try again!")


def main():
    """Main function to set up and run the quiz"""
    
    
    quiz = Quiz()
    
    
    q1 = Question(
        "What is the capital of France?",
        ["Berlin", "Madrid", "Paris", "Rome"],
        "c"
    )
    
    q2 = Question(
        "Who developed the Python programming language?",
        ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"],
        "b"
    )
    
    q3 = Question(
        "What does 'AI' stand for?",
        ["Automated Intelligence", "Artificial Intelligence", "Advanced Internet", "Algorithmic Integration"],
        "b"
    )
    
    q4 = Question(
        "Which company created the iPhone?",
        ["Google", "Microsoft", "Apple", "Samsung"],
        "c"
    )
    
    q5 = Question(
        "What is 2 + 2 × 3?",
        ["10", "8", "12", "6"],
        "b"
    )
    
    
    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)
    quiz.add_question(q4)
    quiz.add_question(q5)
    
    
    quiz.start_quiz()


if __name__ == "__main__":
    main()