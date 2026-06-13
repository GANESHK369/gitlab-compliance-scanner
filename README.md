# GitLab Compliance Scanner

## Overview

GitLab Compliance Scanner is a Python-based automation tool that helps organizations verify whether GitLab repositories comply with essential DevOps and security best practices.

The scanner connects to GitLab using the GitLab REST API and performs automated compliance checks across multiple projects. It generates a simple compliance report that helps administrators and DevOps teams identify repositories that are not following required governance standards.

## Features

### Branch Protection Validation

Checks whether the default branch of a repository is protected to prevent unauthorized changes and direct commits.

### Webhook Verification

Validates the presence of configured webhooks to ensure integrations and automated workflows are properly set up.

### Merge Request Approval Checks

Verifies whether merge request approval rules are configured, helping enforce code review and quality control processes.

### Automated Compliance Reporting

Generates an easy-to-read compliance report showing PASS or FAIL status for each repository and compliance category.

## Technology Stack

* Python 3
* GitLab REST API
* Requests Library
* Linux / Windows Compatible

## Project Structure

* compliance_scanner.py – Main execution script
* branch_protection_check.py – Branch protection validation logic
* webhook_check.py – Webhook validation logic
* mr_approval_check.py – Merge request approval verification
* config.py – GitLab configuration settings

## Sample Output

## Repository               Branch Protection   Webhook     MR Approval

TEST1                    PASS                FAIL        FAIL
TEST2                    PASS                FAIL        FAIL
TEST3                    PASS                FAIL        FAIL
ganeshK29-project        PASS                FAIL        FAIL

## Benefits

* Reduces manual compliance verification effort
* Improves repository governance
* Helps enforce DevOps best practices
* Identifies security and process gaps quickly
* Provides a foundation for advanced compliance automation

## Future Enhancements

* Export reports to CSV and Excel
* Email compliance notifications
* Generate HTML dashboards
* Integrate with CI/CD pipelines
* Support custom compliance policies
* Slack and Microsoft Teams notifications

## Author

Ganesh Karthikeyan

DevOps & Platform Support Engineer with experience in GitLab Administration, Azure, Artifactory, Black Duck, Linux, and DevOps Automation.
