
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

class Question {
private:
    string questionText;
    vector<string> options;
    char correctAnswer;

public:
    
    Question(string text, vector<string> opts, char correct) {
        questionText = text;
        options = opts;
        correctAnswer = correct;
    }
    
    
    void displayQuestion() { // getter
        cout << questionText << endl;
        for (int i = 0; i < options.size(); i++) {
            char optionLetter = 'a' + i;  
            cout << optionLetter << ") " << options[i] << endl;
        }
    }
    
    
    bool isCorrect(char userAnswer) {
        return (userAnswer == correctAnswer);
    }
    
    
    char getCorrectAnswer() {
        return correctAnswer;
    }
};

class Quiz {
private:
    vector<Question> questions;  
    int score;
    int totalQuestions;

public:
    
    Quiz() {
        score = 0;
        totalQuestions = 0;
    }
    
    
    void addQuestion(Question q) {
        questions.push_back(q);
        totalQuestions++;
    }
    
    
    void startQuiz() {
        cout << "quizz start" << endl;
        cout << string(40, '=') << endl;
        
        
        for (int i = 0; i < questions.size(); i++) {
            cout << "\nQ" << (i + 1) << ": ";
            questions[i].displayQuestion();
            
            char userAnswer;
            
            while (true) {
                cout << "Your Answer (a/b/c/d): ";
                cin >> userAnswer;
                
                
                cout << "Please enter a valid option (a, b, c, or d)" << endl;
            }
            
            
            if (questions[i].isCorrect(userAnswer)) {
                score++;
                cout << " Correct, Your Score: " << score << endl;
            } else {
                cout << "Wrong! Correct answer was: " 
                     << questions[i].getCorrectAnswer() << endl;
                cout << "Score " << score << endl;
            }
        }
        
        
        showResults();
    }
    
    
    void showResults() {
        cout << "\n" << string(40, '=') << endl;
        cout << "QUIZ END! " << endl;
        cout << "Final Score: " << score << "/" << totalQuestions << endl;
        
        
        double percentage = (double(score) / totalQuestions) * 100;
        cout << "Percentage: " << fixed << setprecision(1) << percentage  << endl;
        
        
        if (percentage >= 80) {
            cout << " Excellent work!" << endl;
        } else if (percentage >= 60) {
            cout << "Good job!" << endl;
        } else if (percentage >= 40) {
            cout << " Not bad, keep practicing!" << endl;
        } else {
            cout << " Keep studying and try again!" << endl;
        }
    }
};

int main() {
    
    Quiz quiz;
    
    
    Question q1("What is the capital of France?",
                {"Berlin", "Madrid", "Paris", "Rome"}, 'c');
    
    Question q2("Who developed the Python programming language?",
                {"James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"}, 'b');
    
    Question q3("What does 'AI' stand for?",
                {"Automated Intelligence", "Artificial Intelligence", "Advanced Internet", "Algorithmic Integration"}, 'b');
    
    Question q4("Which company created the iPhone?",
                {"Google", "Microsoft", "Apple", "Samsung"}, 'c');
    
    Question q5("What is 2 + 2 × 3?",
                {"10", "8", "12", "6"}, 'b');
    
    
    quiz.addQuestion(q1);
    quiz.addQuestion(q2);
    quiz.addQuestion(q3);
    quiz.addQuestion(q4);
    quiz.addQuestion(q5);
    
    
    quiz.startQuiz();
    
    return 0;
}