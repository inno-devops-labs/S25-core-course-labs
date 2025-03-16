import { type ASTNode, EvaluateAST, Parser } from "./parser";

function binary_combinations(n: number) {
    const combinations: boolean[][] = [];
    // for every binary combination from 0..0 to 2^n
    for (let i = 0; i < (1 << n); i++) {
        const combination: boolean[] = [];
        for (let j = 0; j < n; j++) {
            // value of each variable in this combination
            combination.push(Boolean(i & (1 << j)));
        }
        combinations.push(combination);
    }
    return combinations;
}

function build_closure(interpretation: Map<string, boolean>): string {
    const variables = Array.from(interpretation.keys());
    for (let i = 0; i < variables.length; i++) {
        const variable = variables[i];
        const var_value = interpretation.get(variable)
        if (var_value == undefined) {
            throw new Error(`Variable ${variable} is not in the interpretation`);
        }
        // negate the variable if it's truthy in the current interpretation
        variables[i] = var_value ? `(!${variable})` : variable;
    }
    const closure: string[] = [];
    for (let i = 0; i < variables.length; i++) {
        // add disjunction between variables if it's not the first variable in the closure
        if (i != 0) {
            closure.push("∨");
        }
        // open nested disjunction if it's not the last variable in the closure
        if (i != variables.length - 1 && variables.length != 1) {
            closure.push("(");
        }
        closure.push(variables[i]);
    }
    // close all disjunctions.
    closure.push(")".repeat(variables.length - 1));
    return closure.join("");
}

function build_closures(falsy_interpretations: TruthTable): string {
    if (falsy_interpretations.length == 0) {
        throw new Error("There is no valid PCNF for this formula");
    }
    
    const disjunctions: string[] = [];
    for (const interpretation of falsy_interpretations) {
        disjunctions.push(build_closure(interpretation.combination));
    }

    let result = "";
    for (let i = 0; i < disjunctions.length; i++) {
        if (i != 0) {
            result += "∧";
        }
        if (i != disjunctions.length - 1 && disjunctions.length != 1) {
            result += "(";
        }
        result += disjunctions[i];
    }
    result += ")".repeat(disjunctions.length - 1);
    return result;
}

type TruthTable = { result: boolean, combination: Map<string, boolean> }[];

function build_truth_table(combs: boolean[][], variables: string[], ast: ASTNode): TruthTable {
    const table: TruthTable = [];
    for (const comb of combs) {
        const variable_map = new Map<string, boolean>();
        variables.forEach((key, idx) => variable_map.set(key, comb[idx]));

        const result: boolean = EvaluateAST(ast, variable_map);
        table.push({ result: result, combination: variable_map });
    }
    return table;
}

export function buildPCNF(formula: string): string {
    try {
        const parser = new Parser(formula);
        const ast = parser.parse();
        if (!ast) throw new Error("This formula is empty.");

        const variables = parser.variables;
        const combs = binary_combinations(variables.length);
        
        // if the formula is const-only, check whether it's falsy and return a fictive PCNF if it is
        if (variables.length === 0) {
            const result = EvaluateAST(ast, new Map());
            if (result) {
                throw new Error("There is no valid PCNF for this formula");
            } else {
                return "(X∧(!X))";
            }
        }
        
        // build truth table
        const table = build_truth_table(combs, variables, ast);
        // for each interpretation that yielded false
        const falsy_interpretations = table.filter((interpretation) => !interpretation.result);
        return build_closures(falsy_interpretations);
    }
    catch (e) {
        if (typeof e === "string") {
            throw new Error(e)
        } else if (e instanceof Error) {
            throw new Error(e.message)
        }
        return ''
    }
}
