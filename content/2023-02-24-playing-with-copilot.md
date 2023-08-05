---
title: "Playing with Github Copilot"
date: "2023-02-24"
tags: ["Developer", "Machine Learning"]
image: ""
gradients: ["#3C8CE7", "#00EAFF"]
---

## Playing around with Google Copilot

*Note: This blog post is based on my personal experience using Github Copilot, an AI pair programming tool powered by OpenAI's GPT-3 model. Please keep in mind that the tool is constantly evolving, and my experience might differ from yours.*

### Introduction
**GitHub Copilo**t, is an *AI-powered* tool that provides code suggestions and autocompletion as you write code. It uses advanced deep learning models to offer intelligent suggestions, making coding faster and more efficient. While code suggestions exist in many IDEs, Copilot takes it a step further by generating whole lines of code and** even entire functions**.

*Please note that I have access to Copilot through my Student tier eligibility*.

### VS Code GitHub Copilot extension
To use GitHub Copilot in Visual Studio Code (VS Code), you need to install the **Copilot extension**. Simply navigate to the extensions tab in the IDE and search for `"GitHub Copilot."` Once installed, you will see a small bot icon with a **pilot goggle**, and you will be prompted to sign in.

Generating code suggestions
To demonstrate Copilot's capabilities, I created a Python script and started using comments to interact with the tool. For example, I began with the following comment:

```py
# create a list of even numbers up to 100
```
Copilot instantly provided suggestions, including the option to generate a list of even numbers up to 1. By hovering over the number, Copilot suggested alternatives such as 10 or 100, based on the context of the comment. To accept a suggestion, simply hit the Tab key.

As I continued to write comments, Copilot suggested additional code snippets, such as using list comprehension:

```py
# using list comprehension
By providing a variable name, Copilot generated the corresponding code snippet, which was a list comprehension to generate even numbers from 0 to 100:
```

```py
numbers = [x for x in range(100) if x % 2 == 0]
```

To print the generated list, Copilot even suggested the appropriate code, which I accepted by hitting Tab. The code worked flawlessly.

I then modified the comments to include the boundary conditions of 0 and 100:

```py
# create a list of even numbers up to 100 and include 0 and 100
# using list comprehension
```
Copilot adjusted the code accordingly:

```py
numbers = [x for x in range(0, 101, 2)]
```
Printing the list confirmed that the code was correct.

### Exploring all suggestions
What if you don't like the line of code Copilot has generated, or you want to explore other implementations? Copilot provides a way to view alternative suggestions. By pressing `Ctrl + Enter`, a new tab opens displaying a list of suggested implementations from which you can choose.

Another interesting aspect of Copilot is that it can generate code without using comments. Simply start typing a variable name that hints at its content, such as `prime_numbers_up_to_100`. Copilot will generate implementations that calculate prime numbers up to 100:

```py
=======

prime_numbers_up_to_100 = [x for x in range(2, 101) if all(x % y != 0 for y in range(2, x))]
print(prime_numbers_up_to_100)

=======

prime_numbers_up_to_100 = [x for x in range(1, 101) if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0]
print(prime_numbers_up_to_100)

=======

prime_numbers_up_to_100 = [x for x in range(2, 101) if not [t for t in range(2, x) if not x % t]]
print(prime_numbers_up_to_100)

=======

# ...
```

### Solving LeetCode problems
Let's put Copilot to the test by attempting to solve a coding challenge from **LeetCode**. I randomly selected the problem *"First Missing Positive"* (problem link: https://leetcode.com/problems/first-missing-positive/).

To start, I commented the problem description:

```py
# Given an unsorted integer array, find the smallest missing positive integer.
# Your algorithm should run in O(n) time and use constant extra space.
Copilot immediately suggested the following function definition:

def firstMissingPositive(nums):
    # create a set of the list
    nums = set(nums)
    # iterate from 1 to the length of the list
    for i in range(1, len(nums) + 1):
        # if the number is not in the set, return it
        if i not in nums:
            return i
    # if all the numbers are in the set, return the length of the list + 1
    return len(nums) + 1
```

To my surprise, the code passed all the test cases. When I submitted it out of curiosity, it performed better than expected, **beating 19.86% of submissions** in runtime and 24.9% in memory usage. This demonstrates the power of Copilot in generating functional code with minimal effort.

### Conclusion
My experience with Google Copilot has been impressive so far. The tool's ability to provide accurate code suggestions and generate entire functions has significantly improved my coding speed and productivity. While Copilot is not perfect and may occasionally provide incorrect or inefficient solutions, it serves as an invaluable resource for inspiration and assistance.

I look forward to further exploring Copilot's features and witnessing its evolution as it continues to learn from developers worldwide.




