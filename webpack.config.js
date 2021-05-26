const path = require("path");
const { WebpackManifestPlugin } = require("webpack-manifest-plugin");
const ForkTsCheckerWebpackPlugin = require("fork-ts-checker-webpack-plugin");
const LessPluginCleanCSS = require("less-plugin-clean-css");

const baseDir = "/static";
const jsDir = path.join(baseDir, "js");
const distDir = path.join(baseDir, "dist");
const cssDir = path.join(baseDir, "css");

module.exports = function (argv) {
  const isProd = argv.mode === "production";
  const plugins = [
    new WebpackManifestPlugin(),
    new ForkTsCheckerWebpackPlugin({
      typescript: {
        diagnosticOptions: {
          semantic: true,
          syntactic: true,
        },
        mode: "write-references",
      },
      eslint: {
        // Starting the path with "**/" because of current dev/prod path discrepancy
        // In dev we bind-mount the source code to "/code/static" and in prod to "/static"
        // The "**/" allows us to ignore the folder structure and find source files in whatever CWD we're in.
        files: "**/js/src/**/*.{ts,tsx,js,jsx}",
        options: { fix: !isProd },
      },
    }),
  ];
  return {
    entry: {
      // Importing main.less file here so that it gets compiled.
      // Otherwise with a standalone entrypoint Webpack would generate a superfluous js file.
      // All the Less/CSS will be exported separately to a main.css file and not appear in the recentListens module
      auth: [
        path.resolve(jsDir, "src/index/auth.tsx"),
        path.resolve(cssDir, "main.less"),
      ],
      landing: path.resolve(jsDir, "src/index/landing.tsx"),
      profile: path.resolve(jsDir, "src/user/profile.tsx"),
      search_page: path.resolve(jsDir, "src/index/search.tsx"),
      blog: path.resolve(jsDir, "src/blog/blog.tsx"),
      new_blog: path.resolve(jsDir, "src/blog/newBlog.tsx"),
      product: path.resolve(jsDir, "src/product/product.tsx"),
      new_product: path.resolve(jsDir, "src/product/newProduct.tsx"),
      discussion: path.resolve(jsDir, "src/discussion/discussion.tsx"),
      new_discussion: path.resolve(jsDir, "src/discussion/newDiscussion.tsx"),
    },
    output: {
      filename: isProd ? "[name].[contenthash].js" : "[name].js",
      path: distDir,
      publicPath: `${distDir}/`,
      clean: true, // Clean the output directory before emit.
    },
    devtool: isProd ? "source-map" : "eval-source-map",
    module: {
      rules: [
        {
          test: /\.(js|ts)x?$/,
          // Don't specify the babel configuration here
          // Configuration can be found in ./babel.config.js
          use: "babel-loader",
          exclude: /node_modules/,
        },
        {
          test: /\.less$/i,
          type: "asset/resource",
          loader: "less-loader",
          generator: {
            filename: isProd ? "[name].[contenthash].css" : "[name].css",
          },
          options: {
            lessOptions: {
              math: "always",
              plugins: [new LessPluginCleanCSS({ advanced: true })],
            },
          },
        },
      ],
    },
    resolve: {
      modules: ["/code/node_modules", path.resolve(baseDir, "node_modules")],
      extensions: [".ts", ".tsx", ".js", ".jsx", ".json"],
    },
    plugins,
  };
};
