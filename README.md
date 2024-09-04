# Coding Best Practices Repository

## Overview

This repository contains a collection of Python scripts and supporting files designed to demonstrate coding best practices, particularly focusing on how to structure, document, and maintain code effectively. It is structured for educational purposes and can be used by instructors to teach students about various programming concepts and best practices in software development.

## Repository Structure
"""
/project-root
│
├── bin/                           # Shell scripts for automating command-line tasks
│   ├── SINGLE_command_line_arguments.sh
│   ├── LOOP_command_line_arguments.sh
│   ├── 0_bash_tutorial.sh
│   ├── 1_simple_python.sh
│   ├── 2_loop_python.sh
│   ├── 3_actual_simpled.sh
│   └── 4_actual_looped.sh
│
├── resources/                     # Resources like JSON mappings and requirements files
│   ├── diagnosis_mappings.json
│   └── requirements.txt
│
├── src/                           # Source Python scripts demonstrating various coding practices
│   ├── 0_make_reqTxt.py
│   ├── 1_building_functions.py
│   ├── 2_make_modular_code.py
│   ├── 3_use_a_main_function.py
│   ├── 4_try_and_except.py
│   ├── 5_command_line_arguments.py
│   ├── 6_create_readme.py
│   └── utils/
│       ├── garbage.py
│       ├── garbage_with_main.py
│       ├── print_num_4.py
│       └── __pycache__/
│
├── data/                          # Directory for generated log files and datasets
│
└── .git/                          # Version control directory (Git)
"""

## How to Use This Repository

### Prerequisites

- Python 3.9 or higher
- Conda (recommended) for environment management
- Git for version control
- Bash for executing shell scripts

### Setting Up the Environment

1. **Create a Conda Environment:**

    ```bash
    conda create --name codingbp python=3.9
    conda activate codingbp
    ```

2. **Install Required Packages:**

    Navigate to the repository's root directory and install the required packages:

    ```bash
    pip install -r resources/requirements.txt
    ```

### Running the Scripts

1. **Command-Line Argument Demonstrations:**

    - Run the `SINGLE_command_line_arguments.sh` script to see how command-line arguments can be used in Python scripts:

      ```bash
      bash bin/SINGLE_command_line_arguments.sh
      ```

    - Alternatively, you can run the looped version:

      ```bash
      bash bin/LOOP_command_line_arguments.sh
      ```

2. **Python Code Examples:**

    The `src/` directory contains Python scripts that demonstrate different coding best practices. Each script is named to reflect the concept it demonstrates:

    - **`0_make_reqTxt.py`:** Demonstrates how to generate a `requirements.txt` file to manage dependencies, making it easier to replicate environments and ensure code runs as expected on different systems.

    - **`1_building_functions.py`:** Shows how to build modular functions with clear naming conventions, which enhances code readability and maintainability.

    - **`2_make_modular_code.py`:** Focuses on making code modular and reusable by separating concerns and organizing code into distinct, manageable units.

    - **`3_use_a_main_function.py`:** Illustrates the importance of using a `main()` function to prevent unintended code execution when a script is imported as a module, which is a common best practice in Python development.

    - **`4_try_and_except.py`:** Compares different approaches to error handling, advocating for specific exception handling and cautious use of try/except blocks to avoid masking errors that should be handled differently.

    - **`5_command_line_arguments.py`:** Demonstrates how to use command-line arguments in Python scripts to make your code more flexible and customizable without altering the script itself. This is particularly useful in scenarios where the same script needs to be run with different configurations.

    - **`6_create_readme.py`:** Provides an example of how to automate the creation of a README file using Python. This script is a practical demonstration of how you can use Python to generate documentation that is consistently formatted and up-to-date with the contents of the project.

## Teaching Points

- **Modular Code:** The repository demonstrates how to structure Python code in a modular fashion, making it easier to maintain, test, and extend.
  
- **Error Handling:** Different strategies for error handling are explored, emphasizing the importance of specificity and understanding the impact of different approaches.
  
- **Command-Line Arguments:** Shows how command-line arguments can simplify running scripts with different configurations, improving code flexibility.
  
- **Documentation:** Emphasizes the importance of comments, docstrings, and creating a README to help others understand and use the code effectively.
  
- **Version Control:** The repository uses Git for version control, illustrating the importance of tracking changes and collaborating on code.

## Customization

- **JSON Mappings:** The `resources/diagnosis_mappings.json` file is used in some Python scripts to demonstrate how configuration data can be externalized. This file can be modified to test different configurations without changing the code.

- **Shell Scripts:** The `bin/` directory contains shell scripts that automate the execution of Python scripts with different parameters. These scripts can be customized to fit different teaching scenarios or projects.

## Contributing

If you have suggestions or improvements for these teaching materials, feel free to open an issue or submit a pull request. Collaboration and contributions are welcome!

## License

This repository is licensed under the MIT License. See the LICENSE file for more details.

---

This README is designed to help educators understand the contents of the repository and how it can be 