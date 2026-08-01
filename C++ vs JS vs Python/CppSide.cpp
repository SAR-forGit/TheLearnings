// setting a username code: (with format):
#include <iostream>
#include <format>
#include <algorithm>
#include <cctype>
using namespace std;

int main() {
    
    string givenName;
    cout << "Enter your name: ";
    getline(cin, givenName);
    
    string lowerName = givenName;
    transform(lowerName.begin(), lowerName.end(), lowerName.begin(), ::tolower);
    
    string recomendedUsername = "@" + lowerName +  to_string(givenName.length());
    
    while(1){
        string userName;
        cout << format("we recommend you username: {}. Do you want to use it? ",recomendedUsername);
        cin >> userName;
        
        string userAnswer = userName;
        
        if(userAnswer == "yes" || userAnswer == "YES" || userAnswer == "Y" || userAnswer == "y"){
            userName = recomendedUsername;
            break;
        }
        else if(userAnswer == "No" || userAnswer == "no" || userAnswer == "NO" || userAnswer == "n" || userAnswer == "N"){
            cout << "Enter your desired username: ";
            cin >> userName;
            cout << format("are you sure for the username @{} ", username);
            while(true || || userAnswer == "No" || userAnswer == "no" || userAnswer == "NO" || userAnswer == "n" || userAnswer == "N"){
                cout << "Enter your desired username: ";
                cin >> userAnswer;
                if(userAnswer == "yes" || userAnswer == "YES" || userAnswer == "Y" || userAnswer == "y") break;
                else continue;    
            }
            break;
        }
        else{
            cout << "Wrong Answer! Try Again.";
            cin >> userName;
            continue;
        }
    }
    cout << format("Hey {}, your username is set to {}", givenName, userName);
    return 0;
}

// setting a username code: (without format):
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string givenName;

    cout << "Enter your name: ";
    getline(cin, givenName);

    // Convert name to lowercase
    string lowerName = givenName;
    transform(lowerName.begin(), lowerName.end(), lowerName.begin(), ::tolower);

    string recommendedUsername = "@" + lowerName + to_string(givenName.length());

    string userName;
    string userAnswer;

    while (true) {
        cout << "We recommend you username: " << recommendedUsername
             << ". Do you want to use it? (yes/no): ";
        getline(cin, userAnswer);

        // Convert answer to lowercase
        transform(userAnswer.begin(), userAnswer.end(),
                  userAnswer.begin(), ::tolower);

        if (userAnswer == "yes" || userAnswer == "y") {
            userName = recommendedUsername;
            break;
        }
        else if (userAnswer == "no" || userAnswer == "n") {

            while (true) {
                cout << "Enter your desired username: ";
                getline(cin, userName);

                cout << "Are you sure for the username @"
                     << userName << "? (yes/no): ";
                getline(cin, userAnswer);

                transform(userAnswer.begin(), userAnswer.end(),
                          userAnswer.begin(), ::tolower);

                if (userAnswer == "yes" || userAnswer == "y") {
                    userName = "@" + userName;
                    break;
                }
            }

            break;
        }
        else {
            cout << "Wrong Answer! Try Again.\n";
        }
    }

    cout << "\nHey " << givenName
         << ", your username is set to "
         << userName << endl;

    return 0;
}

// Replace One Word:
#include <iostream>
#include <string>
using namespace std;

int main() {
   
   string nigg = "Hello Nigg, How are you?" ;
   
   size_t pos = nigg.find("Nigg");
   
   if (pos != string::npos) nigg.replace(pos, 4, "Slave");
   
   cout << nigg;
   
   return 0;
}

// Replace All Word (2 Nigg in one sentence):
#include <iostream>
#include <string>
using namespace std;

int main() {
    string nigg = "Hello Nigg, How are you Nigg?";

    size_t pos = 0;

    while ((pos = nigg.find("Nigg", pos)) != string::npos) {
        nigg.replace(pos, 4, "Slave");
        pos += 4; // Length of "Slave"
    }

    cout << nigg;
}
