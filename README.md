# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game's purpose is to guess a secret number within a set range and 
  number of attempts, earning points based on how quickly you guess 
  correctly. The difficulty setting changes the range and number of 
  attempts allowed. The game was built with bugs to practice 
  identifying and fixing broken logic with Copilot inline chat.
- The bugs I found:
1. The hint messages were swapped — guessing too high showed "Go HIGHER" 
     and guessing too low showed "Go LOWER"
2. The new game button did not reset the game properly, the attempts 
     counter never decreased correctly, and a browser refresh was required 
     to play again
3. The final score was always 70 because the attempt_number calculation 
     in update_score was off by one
- Fixes applied:
1. swapped greater than and less than conditions
2. fixed new game reset block to properly clear attempts, score, 
     status, and history, and corrected the starting value from 0 to 1
3. corrected the attempt_number calculation in update_score and removed 
   the even/odd type hack that was making wins impossible on 
   even attempts.

## 📸 Demo

-The game built using Streamlit contains intentional bugs that were identified and fixed using GitHub Copilot inline chat. The player guesses a number within a range 
determined by the difficulty setting, receives hints, and earns points 
based on how quickly they guess correctly.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
