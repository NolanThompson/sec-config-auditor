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
- **Azure Key**: Azure ID key
- **jq**: Command-line JSON processor (for processing the prompt-config.json file).

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

   - Install `jq`
     `jq` is a command-line JSON processor required for handling the `prompt-config.json` file. Install it as per your operating system:

   #### For Ubuntu/Debian Linux

   ```bash
   sudo apt-get update
   sudo apt-get install jq
   ```

   #### For CentOS/RHEL Linux

   ```bash
   sudo yum install jq
   ```

   #### For Fedora Linux

   ```bash
   sudo dnf install jq
   ```

   #### For macOS (using Homebrew)

   ```bash
   brew install jq
   ```

   #### For Windows (using Chocolatey)

   Install Chocolatey first from [https://chocolatey.org/install](https://chocolatey.org/install), then run:

   ```bash
   choco install jq
   ```

   Alternatively, download the `jq` executable from its [GitHub releases page](https://github.com/stedolan/jq/releases) and add it to your system path.

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
     CHATGPT_KEY=your_chat_gpt_key
     AZURE_SUBSCRIPTION_ID=your_azure+subscription_id
     ```

2. **Make the Shell Script Executable**:

   - In the root directory, you'll find the `run_audit.sh` shell script. To make it executable, run the following command while in the directory:

     ```bash
     chmod +x run_audit.sh
     ```

   - This command changes the file's mode to allow execution. Once this is done, you can run the script using `./run_audit.sh [flag]`.

---

## Usage

To use the CloudSec Inside, enter run the `./run_audit.sh [provider] [flag]`, including the "summary" flag or the "recommendations" flag to select which audit you'd like to perform and the "aws" or "azure" flag for which provider you'd like to use.

```
./run_audit.sh aws summary
```

```
./run_audit.sh azure recommendations
```

---

## Customization

### Adding New Audit Types

- To add a new prompt for auditing your security information:
  - Open the `prompt_config.py` file.
  - Add a new flag as the key and prompt as the value for a new key-value pair in the given JSON.

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

- **Environment Variables Not Set**: Confirm that the `.env` file in the root directory is properly configured with your AWS credentials and OpenAI API key. This file should include `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION`, and `CHATGPT_KEY`.

- **GPT Credits**: Check if you have sufficient credits for using OpenAI's GPT services. Running out of credits can prevent the tool from functioning correctly.

- **AWS Permissions**: Verify that your AWS credentials have the necessary permissions to access and retrieve security information for your AWS resources. Insufficient permissions can lead to errors in data retrieval.

- **Network Errors**: If you face network-related issues, ensure that your internet connection is stable and that there are no restrictions blocking access to AWS and OpenAI services.

- **Dependency Conflicts**: In case of conflicts with Python dependencies, consider setting up a virtual environment specifically for this project. This isolates the project dependencies from your global Python environment and can resolve conflicts.

- **Shell Script Execution**: If the `run_audit.sh` script is not running, check that it has been made executable. You can do this by running `chmod +x run_audit.sh` in the root directory of the project.

## Best Practices

- Regularly update the tool to incorporate the latest features and security enhancements.
- Keep your AWS credentials and OpenAI API key secure.
- Regularly review and customize the audit types to align with your organization's security policies.
