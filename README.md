# Design Patterns in Python

This repository contains implementations of popular design patterns in Python, organized by pattern type. Each pattern is implemented in its own folder with a `main.py` file to demonstrate usage.

The project also includes a GitHub Actions workflow to ensure consistent code formatting using [Black](https://github.com/psf/black), a Python code formatter.

## Repository Structure
```plaintext
.
├── LICENSE
├── README.md
├── observer
│   └── main.py
├── repo_structure.txt
├── requirements.txt
├── singleton
│   └── main.py
└── strategy
    └── main.py

3 directories, 7 files
```
```plaintext
pattern_practice/
├── .github/
│   └── workflows/
│       └── auto-format.yml        # GitHub Actions workflow for auto-formatting with Black
├── observer/
│   └── main.py                    # Observer pattern implementation entry point
├── singleton/
│   └── main.py                    # Singleton pattern implementation entry point
├── README.md                      # Project documentation
└── requirements.txt               # Project dependencies
```


### Directory Details

- **`.github/workflows/auto-format.yml`**: This GitHub Actions workflow automatically applies Black formatting to the code whenever changes are pushed to the repository.
- **`observer/`**: Contains the implementation of the **Observer** design pattern. Run `main.py` to execute the example.
- **`singleton/`**: Contains the implementation of the **Singleton** design pattern. Run `main.py` to execute the example.
- **`requirements.txt`**: Lists the Python dependencies for this project. Ensure all dependencies are installed before running the examples.

## Getting Started

### Prerequisites

1. **Install Python**: Ensure that Python 3.6+ is installed on your machine.
2. **Install Dependencies**: Run the following command to install dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt

### Running the examples

Each design pattern has its own directory with a main.py file. You can run the example for a pattern by executing the main.py file in that directory. For example:

Observer Pattern:

    python observer/main.py

Singleton pattern:

    python singleton/main.py

## GitHub Actions for Code Formatting

This project includes a GitHub Actions workflow that automatically formats the code using Black upon each push. Any unformatted code will be reformatted and committed back to the repository automatically.

### How It Works

- **Trigger**: The workflow is triggered on every push to the main branch.
- **Auto-Formatting**: The workflow uses Black to apply consistent formatting to all `.py` files.
- **Push Changes**: If formatting changes are applied, they will be committed and pushed back to the branch automatically.

## Contributing

Feel free to explore the design patterns and suggest improvements. When contributing, please follow these guidelines:

1. Ensure your code is formatted according to Black's standards.
2. Place each new design pattern in its own folder with a `main.py` entry point.

---

Thank you for checking out this design pattern practice repository!

