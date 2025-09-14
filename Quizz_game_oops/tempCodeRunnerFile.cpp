// Simple Quiz Game - C++ Implementation
// MLCOE Probation Task by [Your Name]

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
    // Constructor to initialize a question
    Question(string text, vector<string> opts, char correct) {
        questionText = text;
        options = opts;
        correctAnswer = correct;
    }
    
    // Method to display question and options
    void displayQuestion() {
        cout << questionText << endl;
        for (int i = 0; i < options.size(); i++) {
            char optionLetter = 'a' + i;  // Convert 0->a, 1->b, 2->c, 3->d
            cout << optionLetter << ") " << options[i] << endl;
        }
    }
    
    // Method to check if the given answer is correct
    bool isCorrect(char userAnswer) {
        return (userAnswer == correctAnswer);
    }
    
    // Getter method to return correct answer
    char getCorrectAnswer() {
        return correctAnswer;
    }
};

class Quiz {
private:
    vector<Question> questions;  // Vector to store all questions
    int score;
    int totalQuestions;

public:
    // Constructor
    Quiz() {
        score = 0;
        totalQuestions = 0;
    }
    
    // Method to add a question to the quiz
    void addQuestion(Question q) {
        questions.push_back(q);
        totalQuestions++;
    }
    
    // Main method to run the quiz
    void startQuiz() {
        cout << "🎯 Welcome to the Simple Quiz Game! 🎯" << endl;
        cout << string(40, '=') << endl;
        
        // Loop through each question
        for (int i = 0; i < questions.size(); i++) {
            cout << "\nQ" << (i + 1) << ": ";
            questions[i].displayQuestion();
            
            char userAnswer;
            // Get valid input from user
            while (true) {
                cout << "Your Answer (a/b/c/d): ";
                cin >> userAnswer;
                
                // Convert to lowercase
                if (userAnswer >= 'A' && userAnswer <= 'D') {
                    userAnswer = userAnswer - 'A' + 'a';
                }
                
                if (userAnswer >= 'a' && userAnswer <= 'd') {
                    break;
                }
                cout << "Please enter a valid option (a, b, c, or d)" << endl;
            }
            
            // Check answer and update score
            if (questions[i].isCorrect(userAnswer)) {
                score++;
                cout << "✅ Correct! Score: " << score << endl;
            } else {
                cout << "❌ Wrong! Correct answer was: " 
                     << questions[i].getCorrectAnswer() << endl;
                cout << "Score remains: " << score << endl;
            }
        }
        
        // Show final results
        showResults();
    }
    
    // Method to display final results
    void showResults() {
        cout << "\n" << string(40, '=') << endl;
        cout << "🏆 QUIZ COMPLETED! 🏆" << endl;
        cout << "Final Score: " << score << "/" << totalQuestions << endl;
        
        // Calculate percentage
        double percentage = (double(score) / totalQuestions) * 100;
        cout << "Percentage: " << fixed << setprecision(1) << percentage << "%" << endl;
        
        // Give feedback based on performance
        if (percentage >= 80) {
            cout << "🌟 Excellent work!" << endl;
        } else if (percentage >= 60) {
            cout << "👍 Good job!" << endl;
        } else if (percentage >= 40) {
            cout << "👌 Not bad, keep practicing!" << endl;
        } else {
            cout << "📚 Keep studying and try again!" << endl;
        }
    }
};

int main() {
    // Create a quiz object
    Quiz quiz;
    
    // Create sample questions using vectors for options
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
    
    // Add all questions to the quiz
    quiz.addQuestion(q1);
    quiz.addQuestion(q2);
    quiz.addQuestion(q3);
    quiz.addQuestion(q4);
    quiz.addQuestion(q5);
    
    // Start the quiz
    quiz.startQuiz();
    
    return 0;
}