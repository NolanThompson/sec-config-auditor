# CloudSec Insight Security Configuration Auditor

## Introduction

CloudSec Insight is a command-line utility designed to provide insightful security analysis and recommendations for AWS environments. It leverages the power of OpenAI's GPT API to analyze AWS configurations and offer actionable insights. This tool is ideal for system administrators, DevOps engineers, and security professionals who seek to enhance the security posture of their AWS infrastructure.

Users must use their own GPT API Key in order to run tests. This tool is meant to be customizable to meet your security needs. See the documentation below about being able to tailor this tool to your specific needs.

---

## Table of Contents

- [Introduction](#introduction)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

---

## System Requirements

Before using the AWS Configuration Analysis Tool, ensure that your system meets the following requirements:

- **Operating System**: Linux or macOS. Windows users may need a compatibility layer like WSL (Windows Subsystem for Linux).
- **Python**: Version 3.8 or higher.
- **OpenAI API Key**: Required for using GPT-3.5 or GPT-4 services.
- **AWS Keys and Information**: AWS access key id, AWS secret access key, and your AWS region.
- **Network Access**: Internet connection for accessing AWS and OpenAI services.

---

## Installation

Follow these steps to use CloudSec Insight:

1. **Clone the Repository**:

   - Use Git to clone the repository to your local machine:
     ```
     git clone git@github.com:NolanThompson/sec-config-auditor.git
     ```

2. **Install Dependencies**:

   - Navigate to the cloned directory:
     ```
     cd sec-config-auditor
     ```
   - Install the required Python dependencies to your virtual environment:
     ```
     pip install -r requirements.txt
     ```

---

## Configuration

### Environment Setup

1. **.env File**:

   - Create a `.env` file in the root directory.
   - Add your AWS credentials and OpenAI API key:
     ```
     AWS_ACCESS_KEY_ID=your_access_key_id
     AWS_SECRET_ACCESS_KEY=your_secret_access_key
     AWS_DEFAULT_REGION=your_aws_region
     CHATGPT_KEY=you_chat_gpt_key
     ```

---

## Usage

To use the CloudSec Inside, enter the `src` directory and run the main.py script. Make sure you've created your environment variables.

```
python main.py
```

---

## Customization

### Adding New Audit Types

- To add a new prompt for auditing your security information:
  - Open the `get_response.py` file.
  - Edit line 24 to meet your criteria for the audit.

### Modifying the rest of the tool

- Advanced users can build on top of the tool or modify existing code.

### Testing with PyTest

The AWS Configuration Analysis Tool employs `pytest`, a robust testing framework for Python, to ensure the reliability and correctness of its components. Here's how you can leverage these tests:

1. **Test Scripts Location**:

   - All test scripts are located in the `tests` directory.
   - This structure separates the application logic from the test cases, ensuring clarity and ease of maintenance.

2. **Running Tests**:

   - To run the tests, navigate to the root directory of the project.
   - Execute the following command:
     ```
     pytest
     ```
   - `pytest` will automatically discover and execute all test cases in the `tests` directory.

3. **Test Coverage**:

   - The tests cover critical functionalities of each Python script, including environment variable loading, AWS interactions, and the correct functioning of the OpenAI API integration.
   - Regularly update these tests as new features are added or modifications are made.

4. **Adding New Tests**:
   - When adding new features or modifying existing ones, correspondingly update or add new test cases.
   - Follow the naming convention `test_[feature].py` for new test files.

---

## Troubleshooting

### Common Issues and Solutions

- **Environment Variables Not Set**: Ensure that the `.env` file is correctly configured and that the Python script is reading it properly.
- **GPT Credits**: Ensure you have GPT credits available for you to use.
- **AWS Permissions**: Ensure your AWS permissions allow you to use the API to get security information for your organization.
- **Network Errors**: If you encounter network-related errors, verify your internet connection and access permissions to AWS and OpenAI services.
- **Dependency Conflicts**: If there are conflicts or issues with Python dependencies, try creating a virtual environment specifically for this project to isolate dependencies.

---

## Best Practices

- Regularly update the tool to incorporate the latest features and security enhancements.
- Keep your AWS credentials and OpenAI API key secure.
- Regularly review and customize the audit types to align with your organization's security policies.
