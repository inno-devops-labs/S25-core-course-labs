import { type Token, TOKENS, tokenize } from "./tokenizer";

// AST Node types
interface Identifier {
    type: 'Identifier';
    value: string;
}

interface Constant {
    type: 'Constant';
    value: boolean;
}

interface UnaryOperation {
    type: 'UnaryOperation';
    operator: TOKENS.NEG;
    child: ASTNode;
}

interface BinaryOperation {
    type: 'BinaryOperation';
    operator: TOKENS.DISJ | TOKENS.CONJ | TOKENS.EQUA | TOKENS.IMPL;
    left: ASTNode;
    right: ASTNode;
}

export type ASTNode = Identifier | Constant | UnaryOperation | BinaryOperation;

export function EvaluateAST(node: ASTNode, values: Map<string, boolean>): boolean {
    switch (node.type) {
        case 'BinaryOperation': {
            return evaluateBinaryFormula(node, values);
        }
        case 'UnaryOperation': {
            return evaluateUnaryFormula(node, values);
        }
        case 'Identifier': {
            const val = values.get(node.value) 
            if (val != undefined) { return val }
            else {
             throw new Error('Undefined variable in the table: ' + node.value);
        }
    }
        case 'Constant': {
            return node.value
        }
        default: throw new Error("Unexpected AST node type.")
    }
}

function evaluateBinaryFormula(node: BinaryOperation, values: Map<string, boolean>): boolean {
    const left = EvaluateAST(node.left, values)
    const right = EvaluateAST(node.right, values)
    switch (node.operator) {
        case TOKENS.DISJ: {
            return left || right;
        }
        case TOKENS.CONJ: {
            return left && right;
        }
        case TOKENS.IMPL: {
            return !left || right;
        }
        case TOKENS.EQUA: {
            return left === right;
        }
        default: {
            throw new Error("Unexpected binary formula operator.")
        }
    }
}

function evaluateUnaryFormula(node: UnaryOperation, values: Map<string, boolean>): boolean {
    switch (node.operator) {
        // eslint-disable-next-line @typescript-eslint/no-unnecessary-condition
        case TOKENS.NEG: {
            return !EvaluateAST(node.child, values);
        }
        default: {
            throw new Error("Unexpected unary formula operator.")
        }
    }
}

export class Parser {
    private tokens: Token[];
    private position: number;
    private formula: string;
    private _variables: string[];

    constructor(formula: string) {
        this.tokens = [];
        this.position = 0;
        this.formula = formula
        this._variables = []
    }

    private add_variable(value: string) {
        if (!this._variables.includes(value)) {
            this._variables.push(value);
        }
    }

    private match_IDTF(): Identifier | null {
        const token = this.tokens[this.position];

        if (token.type === TOKENS.IDTF) {
            this.position++;
            this.add_variable(token.value);
            return { type: 'Identifier', value: token.value } as Identifier;
        }

        return null;
    }

    private match_CONST(): Constant | null {
        const token = this.tokens[this.position];

        if (token.type === TOKENS.CONST) {
            this.position++;
            return { type: 'Constant', value: token.value === '1' } as Constant;
        }

        return null;
    }

    private match_LPARENTHESIS(): boolean {
        const token = this.tokens[this.position];

        if (token.type === TOKENS.LPARENTHESIS) {
            this.position++;
            return true;
        }

        return false;
    }

    private match_RPARENTHESIS(): boolean {
        const token = this.tokens[this.position];

        if (token.type === TOKENS.RPARENTHESIS) {
            this.position++;
            return true;
        }

        return false;
    }

    private match_NEG(): boolean {
        const token = this.tokens[this.position];

        if (token.type === TOKENS.NEG) {
            this.position++;
            return true;
        }

        return false;
    }

    private match_binary_operator(): TOKENS.DISJ | TOKENS.CONJ | TOKENS.EQUA | TOKENS.IMPL | null {
        const token = this.tokens[this.position];

        if (
            token.type === TOKENS.DISJ ||
            token.type === TOKENS.CONJ ||
            token.type === TOKENS.EQUA ||
            token.type === TOKENS.IMPL
        ) {
            this.position++;
            return token.type;
        }

        return null;
    }

    private match_formula(): ASTNode | null {
        return (
            this.match_CONST() ??
            this.match_IDTF() ??
            this.match_unary_formula() ??
            this.match_binary_formula()
        );
    }

    parse(): ASTNode | null {
        this.tokens = tokenize(this.formula);
        if (this.tokens.length === 0) {
            return null;
        }
        const parsed = this.match_formula()
        if (parsed && this.position === this.tokens.length) {
            return parsed;
        }
        else {
            throw new Error("Parsing didn't succeed on token " + String(this.position + 1) + ": \" " + this.tokens[this.position].value);
        }
    }

    get variables(): string[] {
        return this._variables;
    }

    private match_unary_formula(): UnaryOperation | null {
        const startPos = this.position;

        if (this.match_LPARENTHESIS() && this.match_NEG()) {
            const child = this.match_formula();

            if (child && this.match_RPARENTHESIS()) {
                return { type: 'UnaryOperation', operator: TOKENS.NEG, child: child };
            }
        }

        this.position = startPos;
        return null;
    }

    private match_binary_formula(): BinaryOperation | null {
        const startPos = this.position;

        if (this.match_LPARENTHESIS()) {
            const left = this.match_formula();

            if (left) {
                const operator = this.match_binary_operator();

                if (operator) {
                    const right = this.match_formula();

                    if (right && this.match_RPARENTHESIS()) {
                        return { type: 'BinaryOperation', operator: operator, left: left, right: right };
                    }
                }
            }
        }

        this.position = startPos;
        return null;
    }
}
