# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
- the hints worked, but my score did not update
- number of attempts left didn't decrease appropriately and I could never start a new game without refreshing the page
-Final score is always 70 and I can't move on to the next round
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
I used Copilot for inline suggesions and and Claude code to help identify bugs
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 
Copilot correctly identified that the even/odd secret type hack was causing 
  wins to be impossible on even attempts. It suggested removing the block that 
  converted the secret to a string and passing the secret directly to 
  check_guess. I verified this by playing multiple rounds and confirming I 
  could win on any attempt number, not just odd ones.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I asked Copilot to fix the new game reset, it only reset the 
  attempts counter but left score and status unchanged. This was misleading 
  because the game still showed "You already won" after clicking New Game. 
  I verified it was still broken by winning a round, clicking New Game, but the message was still there. I then used the Inline Chat feature to highlight the 
  block and asked Copilot to also reset score and status, which fully fixed it.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I ran the game with streamlit run app.py after each fix and tested 
  the scenario for which it was broken. I only considered the bug fixed when I played multiple rounds and the same mistake didn't show up.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I manually tested the score fix by winning on the first guess and checking 
  that the final score was no longer always 70. The score correctly showed 90 
  points, which confirmed the attempt_number calculation in update_score was 
  fixed.
- Did AI help you design or understand any tests? How?
Yes, Copilot suggested the pytest case structure for update_score and 
  explained what the expected output should be based on the fixed formula. 
  This helped me understand that the original attempt_number + 1 was the 
  root cause of the score always landing at 70.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
