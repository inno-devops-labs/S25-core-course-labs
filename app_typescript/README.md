# Propositional Logic Parser & Analyzer

A web-based tool for working with propositional logic formulas. Parse, analyze, and convert propositional logic expressions without sending any data to the server.

## Features

- **Formula Parsing**: Handles complex propositional logic formulas with support for:
  - Variables (A-Z)
  - Constants (0, 1)
  - Logical operators:
    - Conjunction (/\\)
    - Disjunction (\\/)
    - Negation (!)
    - Implication (->)
    - Equivalence (~)
  - Nested expressions with parentheses

- **CNF Checking**: Verify if a formula is in Conjunctive Normal Form (CNF)
- **PCNF Generation**: Convert any valid formula to Perfect Conjunctive Normal Form
- **AST**: View the Abstract Syntax Tree of your formulas (currently in creepy JSON format)

## Usage

### Input Format

Examples of valid formulas:

- A # Single variable
- (!B) # Negation
- (A∨C) # Disjunction
- ((A∨B)∧(B∨C)) # Complex expression
- (((A∨B)∧(C->D))~E) # Using all operators

Special symbols in the examples are used for prettiness, you should use slashes for conjunction and disjunction symbols in the input field.

### Running Locally

Install dependencies:

```bash
npm install
```

Run the development server:

```bash
npm run dev
```

Open your browser and navigate to `http://localhost:9000`.

### Running Tests

```bash
npm test
```
