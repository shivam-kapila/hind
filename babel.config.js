module.exports = {
  presets: [
    [
      "@babel/preset-typescript",
      {
        allowDeclareFields: true,
      },
    ],
    "@babel/preset-react",
    [
      "@babel/preset-env",
      {
        useBuiltIns: "usage",
        corejs: { version: "3.12.1", proposals: true },
        targets: {
          node: "16",
          browsers: ["> 0.2% and not dead", "firefox >= 44"],
        },
      },
    ],
  ],
  plugins: [
    [
      "@babel/plugin-transform-typescript",
      {
        allowDeclareFields: true,
      },
    ],
    "@babel/plugin-proposal-class-properties",
    "@babel/plugin-transform-runtime",
  ],
};
