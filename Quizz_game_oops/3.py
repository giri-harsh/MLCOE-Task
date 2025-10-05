class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text  = question_text
        self.options  = options
        self.correct_answer     = correct_answer
    
    def display_question(self):
        
        
        print(self.question_text)
        
        for i in range(len(self.options)):
            letter = chr(97 + i)
            print(letter + " " + self.options[i])


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.total_questions = 0
    
    def add_question(self, question):
        self.questions.append(question)
        self.total_questions = self.total_questions + 1
    
    def start_quiz(self):
        print("Welcome to Quiz Game")
        print("=" * 30)
        
        for i in range(len(self.questions)):
            print("\nQ" + str(i + 1) + ": ")
            self.questions[i].display_question()
            
            user_answer = ""
            while user_answer not in ['a', 'b', 'c', 'd']:
                user_answer = input("Your Answer (a/b/c/d): ")
                user_answer = user_answer.lower()
                if user_answer not in ['a', 'b', 'c', 'd']:
                    print("Please enter a, b, c or d")
            
            if user_answer == self.questions[i].correct_answer:
                self.score = self.score + 1
                print("Correct! Score: " + str(self.score))
            else:
                print("Wrong! Correct answer was: " + self.questions[i].correct_answer)
                print("Score: " + str(self.score))
        
        self.show_results()
        
        
        
        
def show_results(self):
        print("\n" + "=" * 30)
        print("Quiz Over!")
        print("Final Score: " + str(self.score) + "/" + str(self.total_questions))
        
        percentage = (self.score / self.total_questions) * 100
        print("Percentage: " + str(percentage) + "%")
        
        if percentage >= 80:
            print("Excellent!")
        elif percentage >= 60:
            print("Good job!")
        elif percentage >= 40:
            print("Not bad!")
        else:
            print("Keep trying!")
            
            
            

def main():
    quiz = Quiz()
    
    q1 = Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "c")
    q2 = Question("Who made Python?", ["James", "Guido", "Dennis", "Bjarne"], "b")
    q3 = Question("What does AI mean?", ["Auto Intelligence", "Artificial Intelligence", "Advanced Internet", "Algo Integration"], "b")
    q4 = Question("Who made iPhone?", ["Google", "Microsoft", "Apple", "Samsung"], "c")
    q5 = Question("What is 2 + 2 * 3?", ["10", "8", "12", "6"], "b")
    
    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)
    quiz.add_question(q4)
    quiz.add_question(q5)
    
    quiz.start_quiz()

if __name__ == "__main__":
    main()
            
       