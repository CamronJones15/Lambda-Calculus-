# Lambda-Calculus-
Overview

This project implements a simple Lambda Calculus evaluator in Python. It demonstrates how computation works using only functions, variables, and function application. The program focuses on beta reduction, which is the core rule used to evaluate lambda expressions.

Features
Represents lambda expressions using Python classes:
Variables (Var)
Functions (Lambda)
Function applications (Apply)
Performs beta reduction
Displays step-by-step evaluation
Designed to be simple and beginner-friendly
Key Concepts
Lambda Expression

A function is written as:
λx. expression

Application

Applying a function:
(function argument)

Beta Reduction

The main evaluation rule:
(λx. E) A → E[x := A]

This means replacing x in expression E with A.

File Structure

project/
│── main.py Lambda Calculus evaluator
│── README.md Project documentation

How to Run
Make sure Python 3 is installed
Run the script:
python main.py
Example

Input expression:
(λx.x) y

Output:
Start: ((λx.x) y)
Step 1: y
Done: y

How It Works

Expression Types:

Var represents a variable
Lambda represents a function
Apply represents function application

Substitution:
Replaces variables with values during evaluation

Beta Reduction:
Applies functions to arguments

Evaluation Loop:
Repeatedly reduces expressions until no changes occur

Limitations
No parsing from strings; expressions must be built manually
No full alpha conversion (variable renaming to avoid conflicts)
Limited to basic beta reduction
No optimization or advanced evaluation strategies
Learning Purpose

This project helps illustrate how functional computation works at a low level and provides a foundation for understanding functional programming languages such as Haskell. It also introduces evaluation strategies and substitution.

Possible Improvements
Add a parser for user input
Implement alpha conversion
Support normal-order and applicative-order evaluation
Add detection for infinite loops
Authors

Camron Jones
Fernando Rios Cruz 

Summary

This project demonstrates that all computation can be reduced to simple function application and substitution.
