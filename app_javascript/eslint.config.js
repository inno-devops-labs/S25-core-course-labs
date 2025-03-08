const js = require("@eslint/js");

module.exports = [
    js.configs.recommended,
    {
        files: ["src/**/*.js"],
        languageOptions: {
            ecmaVersion: "latest",
            globals: {
                document: "readonly",
                window: "readonly",
                alert: "readonly",
                setInterval: "readonly",
                clearInterval: "readonly"
            }
        },
        rules: {
            "no-unused-vars": "warn",
            "no-console": "off",
            "semi": ["error", "always"],
            "quotes": ["error", "double"],
            "no-undef": "off" // Disables undefined variable warnings for browser globals
        }
    }
];
