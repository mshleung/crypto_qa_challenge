# QA Challenges: My thoughts and conclusions

# Question 1
This question in my opinion is the fastest to finish, the algo is not very hard. I think this question mainly want to focus on if I have checked all the edge cases with pytest.

# Question 2
The hardest part of question 2 for me is to install all the required sdks for my old piece of junk Macbook Pro. I am not kidding, but installing javaSDK took me 2 hours. Anyways, more about this question, I think the interesting part is that it asks in the instructions, saying "Verify that the date is correct (matches the current date or expected date)". Originally my code only check if the smallest date is equal to todays date, but then the question was stuck in my head, why "expected date" and not current date? Then I found out my test would fail sometimes, because the 9-day forecast update at 11:30am to make the smallest date the next day. So I had the adjust my code to handle this situation. My way of solving this issue is to find all the xpath that contains "date", and then compare it to today's date to see if it is the "expected date". This is probably not the best way to solve the question in the long run, because if HK Observatory decided to change the update pattern, then this will not give the correct output. It is also only one test technically, but I counted checking the elements before landing on the forecase page as 2 more tests, so I can check if there are any UI change on the application. Oh, and as mentioned in the Question 2 folder's README, I can only make it work on Android emulator, sorry 🙏

# Question 3
Compare to question 2, question 3 is a bit easier, the hardest part is probably finding the API endpoint, and how to generate the random ID for it to parse everytime. Then of course, we need to handle different kind of response error, but it was not hard (thanks AI)

# Conclusions
It is 2026 and I would be the biggest liar if I said I did not use AI to help me with this assignment, so yes I did use AI! And gosh I was amazed by how good the AI is right now, VS code + Copilot is crazy good. It does get stupid sometimes, and if it went into a wrong rabbit hole, it will keep digging further without knowing how to get back, but if it is working the way you want, it can be very useful!
After all I think this assessment is quite fun! 