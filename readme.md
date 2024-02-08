# Setup Instructions
1. Clone the GitHub Repository:
Clone the GitHub repository your professor provided to your local machine. Use the following command in your terminal or command prompt: `git clone <repository_url>`
2. Understand the Repository Structure:
Explore the repository and understand its structure. Look for the calculator code and the pytest files.

3. Replace Calculator Code:
Identify the location of the calculator code in the repository. Replace the existing calculator code with your Python code that sends a Discord message.

4. Install Dependencies:
Check if there are any dependencies mentioned in the repository, and make sure to install them. Use a virtual environment to manage dependencies. You can create a virtual environment using the following commands:

`python -m venv venv` # Create a virtual environment

`source venv/bin/activate`  # Activate the virtual environment (for Linux/Mac)

or
`venv\Scripts\activate`  # Activate the virtual environment (for Windows)


5. Then, install the dependencies using:

`pip install -r requirements.txt`

6. Modify Pytest Files:
Locate the pytest files in the repository. Update these files to use your new code for testing. Make sure to replace any references to the old calculator code with your Discord message sending code.

7. Run Pytests:
Execute the pytest command to run the tests. Use the following command: `pytest`

8. Check the test results and make any necessary adjustments to your code or the tests to ensure everything is working correctly.

9. Commit Changes:
Once you have successfully replaced the calculator code, modified the pytest files, and verified that the tests pass, commit your changes using Git:

`git add .`

`git commit -m "Replace calculator code with Discord message sending code"`

`git push origin master  # Assuming you are on the master branch`


# Changes to be made to get the authorization code from a .env file

By using a .env file and python-dotenv, you can keep sensitive information, such as API tokens, separate from your code and avoid exposing them directly in your scripts.

1. Install python-dotenv
Install the python-dotenv library using the following command:

`pip install python-dotenv`

2.  Create a .env File
Create a file named .env in the same directory as your Python script. Add the following line to the .env file:

`DISCORD_TOKEN=insert token here`

Replace the token value with your actual Discord authorization token.

3. Modify Your Python Script
Update your Python script to use the python-dotenv library to load the environment variables from the .env file. You can do that by adding the following code to your python script. 

`import os`

`from dotenv import load_dotenv`

`import requests`


Load environment variables from .env
`load_dotenv()`


Get Discord token from environment variable
`discord_token = os.getenv("DISCORD_TOKEN")`


Check if the token is available

`if discord_token is None:`
    `raise ValueError("Discord token not found in the .env file")`

4. Run Your Script
Now you can run your Python script, and it will use the Discord token loaded from the .env file. If the token is not found in the .env file, a ValueError will be raised.
