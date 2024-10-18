<h1 style="color:blue;">English Learning App - Most Common Phrasal Verbs</h1>

Welcome to the English Learning App! 

Our goal is to help you master the most common phrasal verbs in English by providing a fun and interactive quiz. Whether you're a beginner or looking to refresh your memory, this app is designed to boost your vocabulary skills effectively.

## User Experience (UX)

User Requirements and Expectations

User Requirements: 

The primary user requirement is the desire to improve english vocabulary while playing in a fun and educational activity. The game is suitable for both beginners and advanced students seeking to enhance their vocabulary.

User Expectations- Users can expect:
- Interactive Quiz: Engage with a random selection of phrasal verbs each time you take the quiz.
- Immediate Feedback: Know right away if your answer is correct and see the correct answer if you make a mistake.
- Unlimited Retakes: Practice as many times as you like to improve your knowledge and confidence.
- Score Tracking: Keep track of your progress with a score at the end of each quiz.
- Users interested in programming can explore the codebase to understand the integration of codes.

User Stories

1) First Time Visitor Goals

As a first-time visitor, I want to understand how to play the game and learn about its purpose in relation to english vocabulary.

I aim to experience an engaging and interactive interface that guides me through the gameplay process.

2) Returning Visitor Goals

As a returning visitor, I want to challenge myself with new rounds of the game and improve my score in different medical term categories.

I wish to continue enjoying the entertaining aspect of the game while reinforcing my english vocabulary.

I look forward to comparing my current highscore with my previous ones and with scores from other players.

3. Frequent Visitor Goals

As a frequent visitor, I want to explore all the available categories and consistently achieve higher scores.

I aim to share my progress and achievements with friends and colleagues, promoting healthy competition among fellow players.

## Flow Chart

![Flowchart](documentation/Flowchart.png)

## Features
## How to Use
1. Start the Quiz: Press enter to begin.
2. Answer Questions: Translate the given phrasal verb from English to Portuguese.
3. Receive Feedback: Get immediate feedback on your answers.
4. The program will repeat the questions 10 times
5. View Your Score: At the end of the quiz, see how well you did.
6. Retake the Quiz: Choose to retake the quiz if you want more practice.

Wecome message

![Wecome message](documentation/wecome_message.png)

First Question

![First Question](documentation/first_question.png)

Wrong Answer Message

![Wrong Answer](documentation/first_answer.png)

Correct Answer Message

![Correct Answer](documentation/correct_answer.png)

Final Score and question to play the game again

![Continue question](documentation/continue_question.png)

No, I don´t want to continue playing the game

![Continue no](documentation/continue-no.png)

Yes, I want to continue playing the game

![Continue yes](documentation/continue_yes.png)

Answer different to Yes/No

![Wrong answer](documentation/wrong_answer.png)

## Responsiviness

![Responsiviness](documentation/responsive.png)

## Testing

- Tested invalid inputs
- Tested the HEROKU link on Chrome 


## Validator Testing

PEP8
- Errors returned from PEP8 validation. The erros were corrected.


![Errors](documentation/pep8_testing.png)

## Bugs

No Bugs were detected

## Deployment
This project was deployed using Code Institute mock terminal for HEROKU.

Deployment process
1) GitHub Setup

Log in to Github

Access the repository for deployment. 

Add a new line character at the  end of the text inside the input method.

To create a list of requirements, the following command was used in the terminal 'Pip3 freeze > requirements.txt'.

2) Heroku Setup

Log in to Heroku.

Click the "New" button in the top right corner.

Select "Create New App."

Provide a name for the app (english-learning-app) and choose a region (Europe).

Click the "Create app" button.

Navigate to the "Deploy" section in the navigation bar. Under "Deployment Method," choose GitHub/Connect to GitHub.

In the "Connect to GitHub" section, enter the repository name and click the search button.

Once the repository link appears in the search results, click the "Connect" button. 

Go to Settings in the nav bar and select "Add Buildpacks."

Add Python and save. Then add Node.js, ensuring that Python is listed first. Buildpacks

Once the Config Vars are set, click Deploy.

Choose Automatic deployment. Automatic deployment updates the site automatically with your GitHub commits. Ensure that "Branch to deploy" is set to the main branch.

Finally, click the "Deploy" button to make the website go live.

[English Learning App](https://english-learning-app-d0710ebd4b97.herokuapp.com)

## Credits
## Content

•	The phrasal verbs and their translations were given by Chatgbt website 
[ChatGbt](https://chatgbt.com/)

## Technologies Used

The primary language employed in this project is Python. 

Frameworks, Libraries & Programs Used:

•	Random - Used to randomly select the word for the game.

•	GitPod - IDE used to create the game.

•	Github - Used for file storage, version control, and hosting page assets.

•	Code Institute Python Essentials Template - Served as the foundational structure for this project.

•	Heroku - Used to deploy the project.

•	Favicon.io - To create favicon.

•	Chat-GPT - To find the most comom english phrasal verbs and their translation to portuguese.

## Acknowledgments

[Code Institute](https://codeinstitute.net/ie/)

•	My project facilitator: Lewis Dillon [Git Hub](https://github.com/LewisDillon)

•	My family for all the support and love



Happy learning!