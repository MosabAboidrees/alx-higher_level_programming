# JavaScript Warm Up

This repository contains scripts written in JavaScript for various tasks. Below is a description of each task and the corresponding script.

## Task 0: First constant, first print

This script prints "JavaScript is amazing".

### File

- `0-javascript_is_amazing.js`

### Description

This script performs the following operations:
1. **Shebang:** Specifies the Node.js interpreter to run the script.
2. **Constant Declaration:** Declares a constant variable called `myVar` with the value "JavaScript is amazing".
3. **Printing:** Uses `console.log(...)` to print the value of `myVar` to the console.

### Instructions

1. **Create the script file:**
    - Use `vim`, `vi`, or `emacs` to create and edit the file `0-javascript_is_amazing.js`.

2. **Add the required content to `0-javascript_is_amazing.js`.**

3. **Save and exit the editor:**
    - For `vim` or `vi`: Press `Esc`, then type `:wq` and press `Enter`.
    - For `emacs`: Press `Ctrl-x` `Ctrl-s` to save, then `Ctrl-x` `Ctrl-c` to exit.

4. **Make the file executable:**
    ```sh
    chmod +x 0-javascript_is_amazing.js
    ```

5. **Run semistandard to check for code compliance:**
    ```sh
    semistandard --fix 0-javascript_is_amazing.js
    ```

6. **Check the length of the file:**
    ```sh
    wc -l 0-javascript_is_amazing.js
    ```

### Example

To execute the script and see the output:
```sh
./0-javascript_is_amazing.js
```

## Output
```sh
JavaScript is amazing
```

## Task 1: 3 languages

This script prints 3 lines.

### File

- `1-multi_languages.js`

### Description

This script performs the following operations:
1. **Shebang:** Specifies the Node.js interpreter to run the script.
2. **Printing:** Uses `console.log(...)` to print three lines:
    - The first line: "C is fun"
    - The second line: "Python is cool"
    - The third line: "JavaScript is amazing"

### Instructions

1. **Create the script file:**
    - Use `vim`, `vi`, or `emacs` to create and edit the file `1-multi_languages.js`.

2. **Add the required content to `1-multi_languages.js`.**

3. **Save and exit the editor:**
    - For `vim` or `vi`: Press `Esc`, then type `:wq` and press `Enter`.
    - For `emacs`: Press `Ctrl-x` `Ctrl-s` to save, then `Ctrl-x` `Ctrl-c` to exit.

4. **Make the file executable:**
    ```sh
    chmod +x 1-multi_languages.js
    ```

5. **Run semistandard to check for code compliance:**
    ```sh
    semistandard --fix 1-multi_languages.js
    ```

6. **Check the length of the file:**
    ```sh
    wc -l 1-multi_languages.js
    ```

### Example

To execute the script and see the output:
```sh
./1-multi_languages.js
```

## Output
```sh
C is fun
Python is cool
JavaScript is amazing
```


## Task 2: Arguments

This script prints a message depending on the number of arguments passed.

### File

- `2-arguments.js`

### Description

This script performs the following operations:
1. **Shebang:** Specifies the Node.js interpreter to run the script.
2. **Argument Handling:** Uses `process.argv` to get the arguments passed to the script.
3. **Conditional Printing:** Prints different messages depending on the number of arguments:
    - If no arguments are passed, it prints "No argument".
    - If one argument is passed, it prints "Argument found".
    - If more than one argument is passed, it prints "Arguments found".

### Instructions

1. **Create the script file:**
    - Use `vim`, `vi`, or `emacs` to create and edit the file `2-arguments.js`.

2. **Add the required content to `2-arguments.js`.**

3. **Save and exit the editor:**
    - For `vim` or `vi`: Press `Esc`, then type `:wq` and press `Enter`.
    - For `emacs`: Press `Ctrl-x` `Ctrl-s` to save, then `Ctrl-x` `Ctrl-c` to exit.

4. **Make the file executable:**
    ```sh
    chmod +x 2-arguments.js
    ```

5. **Run semistandard to check for code compliance:**
    ```sh
    semistandard --fix 2-arguments.js
    ```

6. **Check the length of the file:**
    ```sh
    wc -l 2-arguments.js
    ```

### Example

To execute the script and see the output:
```sh
./2-arguments.js
```

## Output
```sh
