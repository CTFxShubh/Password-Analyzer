# Password Analyzer Tool
 
## Overview

The Password Analyzer is a comprehensive tool designed to evaluate the strength of user passwords and provide detailed reports on potential vulnerabilities. It assesses various factors that contribute to password security, including common usage patterns, personal information matches, and susceptibility to both dictionary and brute-force attacks. The tool also offers actionable recommendations to enhance password security.

## Key Features

1. Password Strength Analysis: Evaluates the strength of passwords based on length, character diversity, and overall complexity. This helps users understand how robust their passwords are against potential threats.

2. Common Password Detection: Identifies if the password is among a list of commonly used passwords, which are more susceptible to attacks. This feature helps in avoiding passwords that are easily guessable.

3. Personal Information Matching: Checks if the password includes personal information such as names, dates of birth, email addresses, or phone numbers. This ensures that passwords are not easily guessable through personal data.

4. Dictionary Attack Simulation: Assesses the password's vulnerability to dictionary attacks, where attackers use precompiled lists of common words and phrases to crack passwords.

5. Brute-Force Attack Simulation: Estimates the time required to crack the password using brute-force methods, where every possible combination is tried until the correct one is found. This provides insight into the password's resilience against exhaustive search attacks.

6. Personalized Recommendations: Offers tailored suggestions for improving password security based on the analysis results. These recommendations help users create stronger, more secure passwords.

## Installation Instructions

1. Clone the Repository: Open your terminal and execute the following commands to clone the repository and navigate to the project directory:

 ```bash
 git clone https://github.com/CTFxShubh/FUTURE_CS_03.git
 cd FUTURE_CS_03
 ```

2. Prepare Your Environment

**Ensure Python is Installed:** Make sure you have Python installed on your computer. You can check if Python is installed by opening a terminal (on macOS or Linux) or Command Prompt (on Windows) and typing:

```sh
python --version
```
**If Python is not installed, you can download and install it from the official Python website**

3. Run the Script

**Run the script by typing the following command:**

```bash
python password_analyzer.py
```

**If you are using Python 3.x and have both Python 2.x and 3.x installed, you might need to use:**

 ```bash
python3 password_analyzer.py
```

4. Input a Password

**After running the script, you will be prompted to enter a password:**

```bash
Enter the password to analyze:
```

**Type the password you want to analyze and press Enter.**

5. View the Results

**The script will analyze the password and display the strength score and recommendations to improve its security:**

```bash
Password Strength Analysis:
Score: 5/8
Recommendations for Improvement:
- Increase length to at least 8 characters.
- Include at least one uppercase letter.
- Avoid using common passwords.
```

6. Modify and Re-run as Needed

**Based on the recommendations provided by the script, modify your password and re-run the script as needed to check for improvements.**

7. Additional Tips

**Run in an IDE:** You can also run the script in an Integrated Development Environment (IDE) like PyCharm, VS Code, or Jupyter Notebook, which provides a more user-friendly interface and debugging tools.

**Customize the Script:** Feel free to modify the script to include more advanced password checks or to read common passwords and dictionary words from external files.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

