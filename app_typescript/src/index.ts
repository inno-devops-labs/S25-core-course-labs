import { type ASTNode, Parser } from './parser';
import { isCNF } from './cnf_checker';
import './styles.css';
import { buildPCNF } from './pcnf_builder';

class PropositionalLogicUI {
    private formulaInput: HTMLTextAreaElement;
    private checkCnfButton: HTMLButtonElement;
    private buildPcnfButton: HTMLButtonElement;
    private resultDiv: HTMLDivElement;
    private astOutput: HTMLDivElement;

    constructor() {
        this.formulaInput = document.getElementById('formula-input') as HTMLTextAreaElement;
        this.checkCnfButton = document.getElementById('check-cnf') as HTMLButtonElement;
        this.buildPcnfButton = document.getElementById('build-pcnf') as HTMLButtonElement;
        this.resultDiv = document.getElementById('result') as HTMLDivElement;
        this.astOutput = document.getElementById('ast-output') as HTMLDivElement;

        this.initializeEventListeners();
    }

    private initializeEventListeners(): void {
        this.checkCnfButton.addEventListener('click', () => { this.checkCNF(); });
        this.buildPcnfButton.addEventListener('click', () => { this.buildPCNF(); });
    }

    private checkCNF(): void {
        try {
            const formula = this.formulaInput.value.trim();
            if (!formula) {
                this.showError('Please enter a formula');
                return;
            }

            const parser = new Parser(formula);
            const ast = parser.parse();
            
            if (!ast) {
                this.showError('Invalid formula');
                return;
            }

            const isCnf = isCNF(ast);
            this.showResult(
                isCnf ? 'Formula is in CNF' : 'Formula is NOT in CNF',
                isCnf ? 'success' : 'error'
            );
            this.showAST(ast);
        } catch (error) {
            if (error instanceof Error) {
                this.showError(error.message);
            }
            else if (typeof error === 'string') {
                this.showError(error);
            }
            else {
                this.showError('An error occurred');
            }
        }
    }

    private buildPCNF(): void {
        try {
            const formula = this.formulaInput.value.trim();
            if (!formula) {
                this.showError('Please enter a formula');
                return;
            }

            const pcnf = buildPCNF(formula);
            this.showResult('PCNF of the formula:', 'success');
            this.showPCNF(pcnf);
        } catch (error) {
            if (error instanceof Error) {
                this.showError(error.message);
            }
            else if (typeof error === 'string') {
                this.showError(error);
            }
            else {
                this.showError('An error occurred');
            }
        }
    }

    private showResult(message: string, className = ''): void {
        this.resultDiv.textContent = message;
        this.resultDiv.className = 'result-box ' + className;
    }

    private showError(message: string): void {
        this.showResult(message, 'error');
    }

    private showAST(ast: ASTNode): void {
        this.astOutput.textContent = JSON.stringify(ast, null, 4);
    }

    private showPCNF(pcnf: string): void {
        this.astOutput.textContent = pcnf;
    }
}

// Initialize the UI when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new PropositionalLogicUI();
});
