\# Student Task Manager — TeamCity CI Pipeline



\## Project Overview

This project demonstrates Continuous Integration (CI) using JetBrains TeamCity. A simple Python Student Task Manager is tested automatically whenever changes are pushed to GitHub.



\## Technologies Used

\- Python 3

\- Git and GitHub

\- JetBrains TeamCity

\- Python unittest framework

\- XML test reports



\## Application

The Student Task Manager supports:

\- Adding tasks

\- Completing tasks

\- Handling invalid tasks



\## CI Pipeline

1\. Developer modifies the Python source code or unit tests.

2\. Changes are committed and pushed to GitHub.

3\. TeamCity detects the GitHub changes through a VCS trigger.

4\. TeamCity checks out the repository.

5\. The build step executes Python unit tests.

6\. XML test reports are generated and published as build artifacts.

7\. TeamCity marks the build as successful or failed based on the test results.



\## Demonstration Results

\- Successful build: all three unit tests pass.

\- Failed build: an intentionally incorrect assertion causes a test failure.

\- Recovery: correcting the assertion and pushing the fix results in a successful build.



\## How to Run Tests Locally

From the project directory, run:



```bash

python -m unittest -v

```



\## Conclusion

This project demonstrates automated testing, version control integration, build status reporting, and test artifact publishing using a local TeamCity CI environment.It is very useful to understand about the tool teamcity.

Demonstration: TeamCity automatically builds the project after a GitHub push.
We are demonstrating today.

We are demonstrating today.
We are demonstrating today 28th.


