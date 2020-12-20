module.exports = {
  env: {
    browser: true,
    es6: true,
  },
  extends: [
    "plugin:react/recommended",
    "airbnb",
    "prettier",
    "prettier/@typescript-eslint",
    "prettier/react",
  ],
  globals: {
    Atomics: "readonly",
    SharedArrayBuffer: "readonly",
  },
  parser: "@typescript-eslint/parser",
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 2018,
    sourceType: "module",
  },
  plugins: ["react", "@typescript-eslint", "prettier"],
  rules: {
    "react/prop-tyes": "off",
    "react/jsx-filename-extension": "off",
    "react/jsx-props-no-spreading": "off",
    "import/extensions": "off",
    camelcase: "warn",
    "prettier/prettier": "error",
    "lines-between-class-members": [
      "error",
      "always",
      { exceptAfterSingleLine: true },
    ],
    "jsx-a11y/label-has-associated-control": ['error', {
      "assert":"either"
    }],
  },
  settings: {
    "import/resolver": {
      node: {
        extensions: [".js", ".jsx", ".ts", ".tsx"],
      },
    },
  },
};
