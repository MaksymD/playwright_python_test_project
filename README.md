# Playwright Python Test Project

This is a Playwright-based automation project for testing web applications using Python. It follows the **Page Object Model (POM)** design pattern to ensure maintainable, scalable, and readable tests.

---

## Getting Started

These instructions will guide you through setting up and running the project on your local machine.

---

### Prerequisites

Before you begin, ensure you have the following installed:

1. **IDE**:  
   - Recommended: [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=windows).  
   - Alternatively, you can use VS Code or any other Python-compatible IDE.

2. **Python**:  
   - Recommended version: [Python 3.12](https://www.python.org/downloads/release/python-3127/).  
   - Ensure Python is added to your system's PATH during installation.

3. **Playwright for Python**:  
   - Learn more about Playwright [here](https://playwright.dev/python/docs/intro).

4. **Allure Report**:  
   - Used for generating detailed test reports. Learn more [here](https://allurereport.org/docs/install/).  
   - Ensure Java is installed, as Allure requires it to generate reports.

5. **Web Browsers**:  
   - Playwright supports multiple browsers (Chromium, Firefox, WebKit).  
   - By default, tests run in **Chrome**.

---

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**:  
   Open a terminal and run the following command to clone the repository:

   ```bash
   git clone https://github.com/MaksymD/playwright_python_test_project.git
   
2. **Create and activate a virtual environment**:  
   Navigate to the project directory and create a virtual environment:

    ```bash
    python3 -m venv venv
    ```
   Activate the virtual environment:

    `source venv/bin/activate`   # On macOS/Linux

    `venv\Scripts\activate` # On Windows

3. **Install the Necessary Packages (Disconnected from VPN):**  
   Install the required packages using pip:

   ```bash
   pip install pytest-playwright
   playwright install
   pip install allure-pytest
   pip install pytest-asyncio
   pip install pytest-ordering
   pip install httpx pyyaml
   pip install build
   python -m build
   
### Running Tests: 
To start simple test to check that all works - run this command in terminal 

```bash
  python -m pytest tests --alluredir=./allure-results  
```
This will execute all the tests located in the tests directory.

### Viewing Test Reports: 
After running the tests, you can generate and view the Allure report. Make sure you have Java installed for Allure to work.

Generate and serve the Allure report:

```bash
  allure serve ./allure-results
```

### Additional Notes: 
Web browsers: By default, tests are executed in Chrome, but you can configure them to run in other browsers like Firefox or WebKit if needed.
If you encounter any issues with dependencies or environment setup, please make sure you're using the recommended Python version and that your environment is properly activated.

### Common Issues:
Tests Fail in Headless Mode:
In some cases, tests may pass in headed mode but fail in headless mode. To fix this, ensure that your browser configurations are correctly set up for headless testing. You may need to adjust timeouts or implement waits for visibility or interactions.

### Contact:
For questions or feedback, please reach out to:
[Maksym Dotsenko](mailto:maksym.dotsenko@atos.net)