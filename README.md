# MassMailing

THE ULTIMATE MASS MAILING CODE.

Follow the steps given below.
1. Just make a csv file with the name "test.csv".(Take a look at the file provided above.) You can use less columns as well in the file, as per your use. 
2. Write the mail body which you want to send to the people. Don't forget to write them in a f-string format in python, by changing the name column to {name}. 
3. While copying your mail body to the variables in code, write f"Dear {name}, \n ......." , instead of "Dear Tanmay, ...". Needless to say, use "\n" wherever you want a space.
4. Just write your gmail address and password in the columns, make a _test.csv_ file, as shown in the example, use f-strings in your mail bodies and incorporate those different variables used in the _test.csv_.
5. Count the number of different body types I used (for example body1, body2, header, etc.) and write your Mail accordingly. If you don't want to use some body parameter, just delete it.
6. Finally, if you want to beautify your mail using bold, italics, fonts, etc. : Write your mail in word and then convert to HTML using online converters and then paste it in the HTML section of the code.(in the form of f-string). My paragraph is commented out there as an example.
7. Now, all you need to do is just open up your terminal, and run "python3 mail.py". Then wait for the magic to happen!

A friendly advice - Don't mail 100-200 people at once. There is a slight chance that your mail might end up in their spam folder. Make 4 batches of 50 and try running the code 4 times with a 2-3 minute gap atleast, if possible.  - _Even this thing can be automated. I have left it for you as an exercise, make me proud!_
