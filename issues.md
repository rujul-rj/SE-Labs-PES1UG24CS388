# Static Code Analysis – Issues Report

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Shell command injection | Security - High (B602) | 24 | subprocess.run() uses shell=True and concatenates the route value into a shell command, potentially allowing command injection. | Use subprocess.run() with a list of arguments and remove shell=True. |
| SQL injection | Security - Medium (B608) | 9 | SQL query is constructed using f-string interpolation, allowing potentially malicious input to modify the SQL statement. | Replace string interpolation with parameterized SQL queries. |
| Incorrect database column definition | Functional Bug | 5 | The column is defined as feeINTEGER instead of fee INTEGER, causing SQL operations referencing fee to fail. | Correct the column definition to fee INTEGER. |
| Bare except clause | Code Quality - Medium | 30 | The exception handler catches every type of exception, potentially hiding unexpected errors. | Catch a specific exception such as sqlite3.Error. |
| Unsafe file handling | Code Quality - Medium | 18-21 | The file is opened and closed manually, which may leave it open if an exception occurs. | Use a with statement to manage the file automatically. |
| Missing file encoding | Code Quality - Low | 18 | The open() function does not specify an encoding, which can cause inconsistent behaviour across environments. | Specify encoding="utf-8". |
| Use of assert for validation | Security - Low (B101) | 38 | Assertions can be removed when Python runs with optimization enabled. | Replace assert with an explicit conditional check. |
| Missing docstrings | Code Quality | 1, 8, 13, 17, 23, 27, 34 | The module and functions do not contain documentation strings. | Add appropriate module and function docstrings. |
| Naming convention violations | Code Quality | 8, 13, 17, 23, 27 | Function names use camelCase instead of Python's recommended snake_case convention. | Rename functions using snake_case. |
| Unused function argument | Code Quality | 13 | The driver parameter in routeRoster() is never used. | Remove the unused parameter or implement its intended functionality. |
| Excessive line length | Code Quality | 5, 9, 14, 29 | Several statements exceed the recommended line length. | Break long statements into multiple lines. |
| Missing whitespace | Code Quality | 8 | Function parameters are not separated by spaces after commas. | Follow standard Python formatting conventions. |

## Summary

The analysis identified security vulnerabilities, functional defects, exception-handling problems, resource-management issues and coding-style violations.

The most important fixes will address shell command injection, SQL injection, incorrect database schema definition and unsafe exception handling.