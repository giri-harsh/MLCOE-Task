class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text  = question_text
        self.options  = options
        self.correct_answer    = correct_answer
    
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
        # self.percent = 0; 
   
   
   
   
    def add_question(self, question):
        self.questions.append(question)
        
        self.total_questions = self.total_questions + 1
    
    def start_quiz(self):
        print("==================================================")
        print("Quizz start")
        print("==================================================")
        
        for i in range(len(self.questions)):
            print("\n Q" + str(i + 1) + ": ")
            self.questions[i].display_question()
            
            user_answer = " "
            
            
            while user_answer not in ['a', 'b', 'c', 'd']:
                user_answer = input("input answer a b c d : ")
                user_answer = user_answer.lower()
                if user_answer not in ['a', 'b', 'c', 'd']:
                    print("invalid option")
            
            if user_answer == self.questions[i].correct_answer:
                self.score = self.score + 1
                print("Correct, your Score: " + str(self.score))
            else:
                print("Wrong,  Correct answer was: " + self.questions[i].correct_answer)
                print(" Your Score: " + str(self.score))
        
        
        
        
def show_results(self):
    print("\n" + "=" * 30)
    print("Quiz Over")
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
    q2 = Question("Who made Python?", ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"], "b")
    q3 = Question("What does AI mean?", ["Auto Intelligence", "Artificial Intelligence", "Advanced Internet", "Algo Integration"], "b")
    q4 = Question("Who made iPhone?", ["Google", "Microsoft", "Apple", "Samsung"], "c")
    q5 = Question("What is 2 + 2 * 3?", ["10", "8", "12", "6"], "b")
    
    print(type(q5))
    
    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)
    quiz.add_question(q4)
    quiz.add_question(q5)
    
    quiz.start_quiz()
    
    # print("Percentage : ")
main()

     