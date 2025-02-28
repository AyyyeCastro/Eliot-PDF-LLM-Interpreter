# Eliot-PDF-LLM-Interpreter
PDF Analysis using local LLM's (Seq2Seq [T5, etc..] + Casual; Deep Reasoning [DeepSeek R1]) and prompt engineering, for summarization, analysis and extraction. Python-based application, built with the Flask framework and a modern JavaScript frontend.


# How to run Eliot
* Follow instructions below; including Pre-reqs.
* For recruiters -> watch demo video [here when It's ready ~]

## Prerequisites

*   **Python 3:** You need to have Python 3 installed on your system.  We recommend Python 3.8 or later.
*    You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
*    
   If you're unsure whether you have Python 3 installed, open a terminal and type `python3 --version` (or `python --version` on Windows).  
   It should show a version number like `Python 3.9.7`.

*   **Git:**  You'll need Git to download the project code.  
      You can download it from [https://git-scm.com/downloads](https://git-scm.com/downloads). 
      You can check to see if you have it by opening a terminal and typing `git --version`.


## Setup Instructions

Follow these steps to get the application running:

1.  **Clone the Repository:**

    Open a terminal (or Command Prompt/PowerShell on Windows) and navigate to the directory where you want to store the project.  
    Then, run the following command:

    ```bash
    git clone [https://github.com/AyyyeCastro/Eliot-PDF-LLM-Interpreter.git](https://github.com/AyyyeCastro/Eliot-PDF-LLM-Interpreter.git)
    ```

2.  **Navigate to Eliot's Directory:**

    Change your current directory to the newly created project folder:

    ```bash
    cd Eliot-PDF-LLM-Interpreter
    ```

3.  **Create a Virtual Environment (Important!):**

    A virtual environment is a way to isolate the project's dependencies, and keep your PC "safe". 
    This is *highly recommended* to avoid (version) conflicts with other programs you might have.

    *   **For Windows:**

        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

    *   **For macOS / Linux:**

        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

    After running the activation command, you should see `(venv)` at the beginning of your terminal prompt. 
    This indicates that the virtual environment is active.  
    *If you close the terminal, you'll need to re-activate the virtual environment the next time you work on the project.*

4.  **Install Dependencies:**

    With the virtual environment activated, install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    This command reads the `requirements.txt` file (which lists all the necessary packages) and installs them into your virtual environment. 
   This might take a few minutes, especially the first time, as it may need to download model data.

5.  **Run the Application:**

    Start the Flask application with this command:

    ```bash
    python llm.py
    ```

    You should see output in the terminal indicating that the application is running, typically something like:

    ```
     * Serving Flask app 'LLM'
     * Debug mode: on
     * Running on [http://127.0.0.1:5000](https://www.google.com/search?q=http://127.0.0.1:5000)
    ```

6.  **Access the Application:**

    Open your web browser (e.g., Chrome, Firefox, Safari, Edge) and go to the following address:

    ```
      http://127.0.0.1:5000

    ```
    Or the address specified in the previous step that the terminal output to you.

    You should now see, and be running, Eliot!

## Using the Application
1. Read the documentation page first.
2. Go to the "Eliot" tab to begin expirementing! 
      First time running will always be the slowest (downloads models).
3. Choose a LLM to interpret your PDF! READ THE DOCUMENTATION FIRST.
4. Insert (attatch) a PDF file, give Eliot a prompt (if applicable) and click send for the magic!
5. Be patient on first run! Models are being downloaded for the first-run, for on-device/local use. 
6. Enjoy the results.

## Troubleshooting

*   **`ModuleNotFoundError`:** If you get an error saying a module is not found (e.g., `ModuleNotFoundError: No module named 'flask'`), make sure you have activated the virtual environment (step 3) and installed the dependencies (step 4).
*  **Port already in use Error**: Change `app.run(debug=True)` to `app.run(debug=True, port=8000)` in the `llm.py` script.

## Stopping the Application
When finished, click `ctrl + c` within your terminal. 
(the terminal is the "hacker" looking menu you've been typing in! Don't worry, this isn't an episode of NCIS. I am not taking over your PC!)
