# Playwright Python Test Project

This is a Playwright-based automation project for testing web applications using Python.  
It follows the Page Object Model (POM) design pattern for more maintainable and readable tests.

## Getting Started

These instructions will help you set up and run the project on your local machine. 

### Prerequisites
- **IDE:** We recommend [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=windows).
- **Python 3.x:** Recommended version is [Python 3.9](https://www.python.org/downloads/release/python-31011/).
- **Playwright for Python:** Learn more [here](https://playwright.dev/python/docs/intro).
- **Web browser:** The project supports multiple browsers (but UI tests runs by default in Chrome Browser).

### Installation

1. Download and install **PyCharm**, **Git**, and **Python** as outlined in "Prerequisites".
2. **Clone the repository:**
```bash
   git clone <your-repo-url>
```

3. Build project (disconnected from VPN):
```bash 
   pip install pytest-playwright
   playwright install
   pip install build
   python -m build
```

### TESTS: To start simple test to check that all works - run this command in terminal 
```bash
   python -m pytest .\tests
```
### REPORT: To check the report after tests - run this command in terminal (java need to be installed)
```bash
   allure serve
```

For questions or feedback, please contact:
[Maksym Dotsenko](mailto:maksym.dotsenko@atos.net)