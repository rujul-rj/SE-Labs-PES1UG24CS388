# Lab 5 – Reflection

## 1. Understanding Static Code Analysis

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and coding standard violations. In this lab, Pylint, Bandit, and Flake8 helped identify different categories of problems in the School Bus Transport Register.

## 2. Comparison of the Three Tools

- **Pylint:** Identified code quality issues, including missing docstrings, naming convention violations, unused arguments, and poor exception handling.
- **Bandit:** Identified security vulnerabilities, including SQL injection and unsafe shell command execution.
- **Flake8:** Detected formatting violations such as excessive line lengths, missing whitespace, and incorrect spacing.

Each tool provided a different perspective on improving the program.

## 3. Issues Fixed and Improvements Made

The major improvements included replacing dynamically constructed SQL queries with parameterized queries, removing unsafe shell execution, correcting the database column definition, handling exceptions more specifically, and using context managers for file operations.

The program was also improved by adding docstrings, following Python naming conventions, and correcting formatting issues.

## 4. Contribution to Code Quality and Maintainability

Static analysis improved the security, readability, and maintainability of the program. The initial Pylint score was 4.00/10, which increased to 10.00/10 after modifications. Bandit reported no remaining security issues, and Flake8 reported no formatting violations.

This lab demonstrated that static analysis tools can identify problems early and help developers maintain cleaner, safer, and more reliable software.