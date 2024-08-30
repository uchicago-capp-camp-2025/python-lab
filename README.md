# CAPP Camp Python Workflow Lab

The goal of this lab is to help you become more comfortable with working with Python, and the workflow introduced today.

Since you are not expected to know how to write Python at this point this may feel intimidating, but for this lab focus on what we've covered and feel free to discuss with peers.

In this lab you will be trying to get a program running by correcting some errors.

## Tips

- The focus of this lab is on the workflow we discussed: run the code, see an error, diagnose & fix, repeat.
- Remember, the '#' character is a comment. You'll notice VSCode colors everything after that on a line line differently. Code following a '#' is not run.
- Try to do this without relying too much on external resources or tools, you of course can and will use those in the future, but for today- practice with what is in front of you.
- Don't let the fact that you likely do not understand the code yet get in your way, focus on the error messages you receive and they'll guide you to working code.
- Feel free to experiment and make changes to the code to better understand it! You can always use `git diff` and `git restore` to undo those changes as needed.

## The Game

Within `game.py` you will find a small Python script that allows you to play a guessing game.

In our game a random word is chosen from a list and players have six tries to guess the word-- guessing one letter at a time.

Unfortunately it has a few bugs right now that we're going to need to fix.

## Part 1 - Syntax Errors

There are two intentional typos in the code you've been given that you'll need to fix.

To find these, try running the code via `python3 game.py` and look at the first error you get:

```
$ python3 game.py
  File "/home/jturk/capp-camp-python-lab/game.py", line 24
    revealed = ["_", "_", "_"
               ^
SyntaxError: '[' was never closed
```

Consider what this error message is telling you, and make the appropriate fix.

Once that's done, try running the code again and you will encounter one more SyntaxError.

Continue the cycle of fixing and running the program until you no longer see a SyntaxError. (When you see a TypeError, it is time to move to the next section.)

**Reminder: Now that you've solved one part of the assignment, it is a good time to do a commit (and push) so you don't lose your work.**

For example:

```
$ git add -u
$ git commit -m "solved part 1"
$ git push origin master
```

(You can also use `git commit -am "solved part 1"` to combine `git add -u` and `git commit` into a single step.)

## Part 2 - Type Error

After fixing the two typos, you will encounter a different kind of error. A TypeError indicates that you are attempting to use data in a way that is not possible for that data's type.

For example, there is no value Python can give for `"hello" + 123`, since this code adds variables of `str` and `int` type.
So instead, you will see a `TypeError`.

Fix the `TypeError` that arises, and you should be able to begin to play the game. Before you do, make another commit.

## Part 3 - Runtime Error

The code should now start to run, but depending on what letter you pick it may crash.
Unlike syntax errors which can be detected automatically, some errors only arise under precise conditions.

This is because we often need the interpreter to reach the code with an error to know that such an error exists. For this reason you'll see these referred to as "runtime" errors.

Run the game via `python3 game.py` as before, and try entering the letter "b" as your first guess. The game should reflect the fact that there is no "b" in the word.

Try and find a letter that crashes the program. Use the resulting error message as you did before, and fix the error.

Remember to make a commit here as well!

## Part 4 - Second Runtime Error

There's still another bug lurking in the program.

For this one, we won't give you the exact condition right away. Experiment with different input to try and trigger it. Thoroughly testing your program is a skill in and of itself.

If you aren't having luck, consider the different things that the program is supposed to do. Track your guesses remaining, what letters have already been guessed, etc. Have you explored all of the functionality?

If you'd like a hint take a look at hint3.md.

Once resolved, be sure to commit!

## Part 5 - Logic Error

Not all errors in code result in an error message, sometimes the code just does the incorrect thing and continues happily along.

You have likely already noticed that the word does not change between runs of the game.

This is not a very fun game as a result, but without an error to go on it takes some understanding of the code to determine why this might be the case.

**Since you are not expected to know how to read Python yet, this may be more of a stretch than the earlier assignments.**

There is a hint in hint4.md if you are stuck.

## Submitting Your Assignment

Once your assignment is complete, be sure you have committed all changes and pushed your code to your GitHub Classroom repository using the command `git push`. This will sync the code on your remote GitHub branch (`main`) with the code from your current local branch of the same name. Afterwards, navigate to your repository and confirm that the code updates are present. View the commits you made and the files that have changed.

Finally, go to the CAPP Camp [Gradescope course](https://www.gradescope.com/courses/834709) and click on the "Python Lab" assignment. Follow the instructions there for submitting your repository. An auto-grader will then run. If you completed the assignment correctly, your code should pass without any errors.
