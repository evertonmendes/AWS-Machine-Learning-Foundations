'''
Testing
    Testing your code is essential before deployment. It helps you catch errors and faulty conclusions before they make any major impact. 
    -Unit Tests
        To catch these errors, you have to check for the quality and accuracy of your analysis in addition to the quality of your code. Proper testing is necessary to avoid unexpected surprises and have confidence in your results.
        Test-driven development (TDD): A development process in which you write tests for tasks before you even write the code to implement those tasks.
        Unit test: A type of test that covers a “unit” of code—usually a single function—independently from the rest of the program.
        The advantage of unit tests is that they are isolated from the rest of your program, and thus, no dependencies are involved.
        However, passing unit tests isn’t always enough to prove that our program is working successfully. To show that all the parts of our program work with each other properly, communicating and transferring data between them correctly, we use integration tests
        -pytest
            Create a test file starting with test_
            Define unit test functions that start with test_ inside the test file
            Enter pytest into your terminal in the directory of your test file and it detects these tests for you.
        Test-driven development: Writing tests before you write the code that’s being tested.


Logging
    Logging is valuable for understanding the events that occur while running your program.
    Be professional and clear, Be concise and use normal capitalization
    Choose the appropriate level for logging
    Provide any useful information

Code reviews

    Questions to ask yourself when conducting a code review
First, let's look over some of the questions we might ask ourselves while reviewing code. These are drawn from the concepts we've covered in these last two lessons.

Is the code clean and modular?
    Can I understand the code easily?
    Does it use meaningful names and whitespace?
    Is there duplicated code?
    Can I provide another layer of abstraction?
    Is each function and module necessary?
    Is each function or module too long?
Is the code efficient?
    Are there loops or other steps I can vectorize?
    Can I use better data structures to optimize any steps?
    Can I shorten the number of calculations needed for any steps?
    Can I use generators or multiprocessing to optimize any steps?
Is the documentation effective?
    Are inline comments concise and meaningful?
    Is there complex code that's missing documentation?
    Do functions use effective docstrings?
    Is the necessary project documentation provided?
Is the code well tested?
    Does the code high test coverage?
    Do tests check for interesting cases?
    Are the tests readable?
    Can the tests be made more efficient?
Is the logging effective?
    Are log messages clear, concise, and professional?
    Do they include all relevant and useful information?
    Do they use the appropriate logging level?



Rather than commanding people to change their code a specific way because it's better, it will go a long way to explain to them the consequences of the current code and suggest changes to improve it. They will be much more receptive to your feedback if they understand your thought process and are accepting recommendations, rather than following commands. They also may have done it a certain way intentionally, and framing it as a suggestion promotes a constructive discussion, rather than opposition.
Keep your comments objective
    Try to avoid using the words "I" and "you" in your comments. You want to avoid comments that sound personal to bring the attention of the review to the code and not to themselves.
Provide code examples
    When providing a code review, you can save the author time and make it easy for them to act on your feedback by writing out your code suggestions


'''