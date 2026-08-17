# Simple Calculator - Streamlit

## Project Overview

This project is a simple calculator application built with **Python and Streamlit**.

The application allows the user to enter two numbers, select a mathematical operation, and view the result directly in the browser.

The project was created as part of a GenAI application deployment assignment to practice deploying a Streamlit application using GitHub and Streamlit Cloud.

## Features

The calculator supports:

* Addition
* Subtraction
* Multiplication
* Division
* Division-by-zero error handling

## Technologies Used

* Python
* Streamlit
* GitHub
* Streamlit Cloud

## Project Structure

```text
simple-calculator/
│
├── app.py
├── requirements.txt
└── README.md
```

## How the App Works

The user enters:

1. First number
2. Second number
3. Mathematical operation

After clicking **Calculate**, the application displays the result.

Example:

```text
First number: 20
Second number: 5
Operation: Addition

Result: 25
```

## Installation

Clone the repository:

```bash
git clone https://github.com/adheela/simple-calculator.git
```

Move into the project folder:

```bash
cd simple-calculator
```

Install the required package:

```bash
pip install -r requirements.txt
```

## Run Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in the browser.

## Deployment

The project is prepared for deployment on **Streamlit Cloud**.

Deployment steps:

1. Push `app.py`, `requirements.txt`, and `README.md` to GitHub.
2. Open Streamlit Cloud.
3. Connect the GitHub repository.
4. Select `app.py` as the main file.
5. Deploy the application.
6. Open the generated live URL and test the calculator.

## Testing

The application can be tested with examples such as:

```text
20 + 5 = 25
20 - 5 = 15
20 * 5 = 100
20 / 5 = 4
```

Division by zero is also handled:

```text
20 / 0
```

The application displays an error instead of attempting an invalid calculation.

## GitHub Repository

```text
https://github.com/adheela/simple-calculator.git
```

## Learning

This project helped me understand the basic workflow for deploying a Streamlit application. I learned how to keep the application code and dependencies in a GitHub repository and use that repository as the source for Streamlit Cloud deployment.
