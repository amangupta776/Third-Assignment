# Frappe Application Customization and Debugging

## Part 1: Custom Fields and Forms

### 1. Creating Custom Fields
- **Objective**: Add a custom field named Customer Anniversary (Date) to the Customer doctype.

### 2. Custom Form
- **Objective**: Customize the Customer form layout, add and make the Customer Anniversary field mandatory.

### 3. Validation Script
- **Objective**: Ensure Customer Anniversary date cannot be a future date.
- **Deliverables**:
  - Screenshots of the custom field creation.
  - Screenshot of the customized form.
  - Validation script.

## Part 2: Workflows

### 1. Designing a Workflow
- **Objective**: Create a workflow for the Sales Order doctype with states: Draft, Pending Approval, Approved, and Rejected.
- **Permissions**:
  - Draft to Pending Approval: Sales User
  - Pending Approval to Approved: Sales Manager
  - Pending Approval to Rejected: Sales Manager

### 2. Workflow Actions
- **Objective**: Add actions such as email notifications for state changes.
- **Deliverables**:
  - Workflow diagram.
  - Configuration details and screenshots.
  - Email notification script.

## Part 3: Print Formats

### 1. Creating a Custom Print Format
- **Objective**: Create a custom print format for Sales Invoice with company logo, custom header, item table layout, and custom footer.

### 2. Customizing the Print Format
- **Objective**: Include the Customer Anniversary field if available, using Jinja templating.
- **Deliverables**:
  - Custom print format code.
  - Screenshots of the printed Sales Invoice with the new format.

## Part 4: Scripts

### 1. Client Scripts
- **Objective**: Auto-calculate and update the Total Cost field in the Item doctype.

### 2. Server Scripts
- **Objective**: Send a notification email to the supplier when a Purchase Order is submitted.
- **Deliverables**:
  - Client script code.
  - Server script code.
  - Email notification template.

## Part 5: Permissions

### 1. Setting Up Role-Based Permissions
- **Objective**: Configure role-based permissions for the Project doctype.
  - **Roles**:
    - Project User: Can read and create projects.
    - Project Manager: Can read, create, and edit projects.
    - Project Admin: Full permissions, including delete.

### 2. Testing Permissions
- **Objective**: Test permissions with different roles.
- **Deliverables**:
  - Permission settings screenshots.
  - Results of permission testing.

## Section 1: Debugging Techniques

### 1. Using the Frappe Debugger
- **Objective**: Enable and use the Frappe debugger in your development environment.

### 2. Debugging Client Scripts
- **Objective**: Use browser developer tools to inspect elements, view console output, and set breakpoints.
- **Deliverables**:
  - Explanation and screenshots of using the Frappe debugger.
  - Screenshots or video demonstrating client script debugging.

## Section 2: Error Logs

### 1. Accessing Error Logs
- **Objective**: Access and resolve errors using Frappe error logs.

### 2. Custom Error Logging
- **Objective**: Log custom error messages and view them in the Frappe error log.
- **Deliverables**:
  - Steps to access error logs with screenshots.
  - Example of resolving a common error.
  - Custom error logging script and screenshots.

## Section 3: Console Output

### 1. Using Console Output for Debugging
- **Objective**: Use `console.log` in client scripts and `frappe.logger` in server scripts for debugging.

### 2. Analyzing Console Output
- **Objective**: Trace execution flow and identify issues using console output.
- **Deliverables**:
  - Script with console output statements.
  - Examples of console output for client and server scripts.
  - Explanation of issue resolution using console output.

## Section 4: Unit Testing

### 1. Writing Unit Tests
- **Objective**: Write unit tests for a custom function and use Frappe test runner to execute them.

### 2. Mocking Data for Tests
- **Objective**: Mock data for unit tests to cover various edge cases.
- **Deliverables**:
  - Unit test scripts.
  - Mock data examples and test results.


# ERPNext Customization: Indexing and Query Optimization for General Ledger Report

## Overview

This guide covers the following:
1. Understanding SQL Indexing and its benefits.
2. Creating necessary indexes for optimized queries.
3. Steps to create a new duplicate report for the General Ledger with optimized queries and indexing.

## Table of Contents

1. [Understanding SQL Indexing](#understanding-sql-indexing)
2. [Indexing in Our Application](#indexing-in-our-application)
3. [Creating Indexes](#creating-indexes)
4. [Creating a Duplicate General Ledger Report](#creating-a-duplicate-general-ledger-report)
5. [Optimizing Queries](#optimizing-queries)

## Understanding SQL Indexing

Indexing in SQL is a technique used to speed up the retrieval of rows from a table. An index is a data structure that provides quick access to rows in a table, based on the values of one or more columns.

### Benefits of Indexing
- **Faster Data Retrieval:** Indexes improve the speed of data retrieval operations.
- **Efficient Query Performance:** By allowing the database to quickly locate and access the data, indexes optimize the performance of queries.

### Types of Indexes
- **Single-Column Indexes:** Indexes on individual columns.
- **Composite Indexes:** Indexes on multiple columns, useful for queries that filter or sort based on multiple columns.

## Indexing in Our Application

To improve the performance of our application, we need to create indexes on columns frequently used in `WHERE`, `JOIN`, `ORDER BY`, and `GROUP BY` clauses.

## Creating Indexes

### Query 1: Supplier Invoice Details

**Original Query:**
```python
for d in frappe.db.sql(
    """ select name, bill_no from `tabPurchase Invoice`
    where docstatus = 1 and bill_no is not null and bill_no != '' """,
    as_dict=1,
):
    inv_details[d.name] = d.bill_no

Index Creation:

sql
Copy code
CREATE INDEX idx_purchase_invoice_docstatus_bill_no
ON `tabPurchase Invoice` (docstatus, bill_no);
Query 2: General Ledger Entries
Original Query:

python
Copy code
gl_entries = frappe.db.sql(
    f"""
    select
        name as gl_entry, posting_date, account, party_type, party,
        voucher_type, voucher_subtype, voucher_no, {dimension_fields}
        cost_center, project, {transaction_currency_fields}
        against_voucher_type, against_voucher, account_currency,
        against, is_opening, creation {select_fields}
    from `tabGL Entry`
    where company=%(company)s {get_conditions(filters)}
    {order_by_statement}
    """,
    filters,
    as_dict=1,
)
Index Creation:

sql
Copy code
CREATE INDEX idx_gl_entry_company
ON `tabGL Entry` (company);

CREATE INDEX idx_gl_entry_company_posting_date
ON `tabGL Entry` (company, posting_date);

CREATE INDEX idx_gl_entry_company_account
ON `tabGL Entry` (company, account);
Query 3: Account Details
Original Query:

for acc in frappe.db.sql("""select name, is_group from tabAccount""", as_dict=1):
    account_details.setdefault(acc.name, acc)
Index Creation:

CREATE INDEX idx_account_name
ON tabAccount (name);
Creating a Duplicate General Ledger Report
To create a new duplicate report for the General Ledger and add indexing:

Duplicate the Report:

Create a new report in the ERPNext system by duplicating the existing General Ledger report.
Ensure the new report includes all necessary fields and functionalities.
Optimize the Query:

Use the optimized query provided below, with the necessary indexes applied.
Optimized Query for General Ledger Report:

gl_entries = frappe.db.sql(
    f"""
    select
        name as gl_entry, posting_date, account, party_type, party,
        voucher_type, voucher_subtype, voucher_no, {dimension_fields}
        cost_center, project, {transaction_currency_fields}
        against_voucher_type, against_voucher, account_currency,
        against, is_opening, creation {select_fields}
    from `tabGL Entry`
    where company=%(company)s {get_conditions(filters)}
    {order_by_statement}
    """,
    filters,
    as_dict=1,
)
Add Indexes:
Ensure that the indexes created in the previous steps are applied to the necessary columns.
Verify that the indexes improve query performance using the EXPLAIN statement