import { expect, describe, test } from 'vitest';
import { Parser } from "./parser";
import { isCNF } from "./cnf_checker";

export interface TestCase {
    formula: string;
    expected: boolean;
    description: string;
}

export const parsing_tests: TestCase[] = [
    { formula: "", expected: true, description: "Empty formula" },
    { formula: "A", expected: true, description: "Single variable" },
    { formula: "1", expected: true, description: "Single constant" },
    { formula: "(!B)", expected: true, description: "Negation" },
    { formula: "(A\\/C)", expected: true, description: "Disjunction" },
    { formula: "((A\\/B)\\/C)", expected: true, description: "Nested disjunction" },
    { formula: "((A\\/(!B))\\/(!C))", expected: true, description: "Nested disjunction with negations" },
    { formula: "((A\\/(B\\/(!C)))/\\((!D)\\/((!E)\\/F)))", expected: true, description: "Nested disjunction and conjunction with negations" },
    { formula: "(((A\\/B)/\\(C->D))~(E\\/F))", expected: true, description: "All binary operators" },
    { formula: "(((A\\/B)/\\(C->D))<->(E\\/F))", expected: false, description: "Failing an invalid operator in tokenizer" },
    { formula: "(A\\/(B\\/C))/\\(A\\/((!B)\\/C))", expected: false, description: "Missing parenthesis" },
    { formula: "(!(B\\/C))", expected: true, description: "Negation of a binary formula" }
];

export function test_parsing(testCase: TestCase): void {
    if (testCase.expected) {
        // Should parse successfully
        const parser = new Parser(testCase.formula);
        const ast = parser.parse();
        expect(ast).toBeDefined();
    } else {
        // Should throw an error
        expect(() => {
            const parser = new Parser(testCase.formula);
            parser.parse();
        }).toThrow();
    }
}

export const CNF_tests: TestCase[] = [
    {
        formula: "((A\\/B)/\\(B\\/C))",
        expected: true,
        description: "Simple CNF",
    },
    {
        formula: "A",
        expected: true,
        description: "Very simple CNF",
    },
    {
        formula: "((A\\/B)/\\((B\\/C)/\\(A\\/C)))",
        expected: true,
        description: "Right-nested CNF",
    },
    {
        formula: "(((A\\/B)/\\(B\\/C))/\\(A\\/C))",
        expected: true,
        description: "Left-nested CNF",
    },
    {
        formula: "(((A\\/B)/\\(B\\/C))/\\((A\\/C)/\\(C\\/D)))",
        expected: true,
        description: "Combined nested CNF",
    },
    {
        formula: "((A\\/B)/\\((B\\/C)/\\((A\\/C)/\\(C\\/D))))",
        expected: true,
        description: "Deeply nested CNF",
    },
    {
        formula: "(((A\\/B)\\/C)~(D\\/E))",
        expected: false,
        description: "Non-CNF formula (equality instead of conjunction)",
    },
    {
        formula: "((A\\/B)/\\((B/\\C)\\/D))",
        expected: false,
        description: "Non-CNF formula (conjunction inside)",
    },
];

export function TestCNF(testCase: TestCase): void {
    const parser = new Parser(testCase.formula);
    const ast = parser.parse();
    const result = isCNF(ast);
    
    expect(result).toBe(testCase.expected);
}

describe('CNF Checker', () => {
    test.each(CNF_tests)('$description', (testCase) => {
        TestCNF(testCase);
    });
});

describe('Parser', () => {
    test.each(parsing_tests)('$description', (testCase) => {
        test_parsing(testCase);
    });
});