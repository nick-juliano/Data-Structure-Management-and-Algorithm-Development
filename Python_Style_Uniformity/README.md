# <u>Project 2</u>: Python Style Uniformity</u>

## Objectives
- Create effective and clean Python packages
- Conform to the rules established in the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
___
## Overview

With various ways to structure functions, classes, and methods within a package, a clear set of rules and standards are
necessary for clean code management. The [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
provides a format standard and best-practices rulebook for various actions within the Python language. 

<i>Note: The object of this section will be the yet-to-be-published Python package in development for my current 
research project. As such, no demonstrable example will be provided in this section, but will be referenced at a later 
date.</i>

___
## Description
A brief summary of the Google Python Style Guide:

### Language Rules
- **Imports**
  -  Use import statements for packages and modules only, not for individual classes or functions.
- **Packages**
  - Import each module using the full pathname location of the module.
- **Exceptions**
  - Exceptions are allowed but must be used carefully.
- **Global variables**
  - Avoid global variables.
- **Nested/Local/Inner Classes and Functions**
  - Nested local functions or classes are fine when used to close over a local variable. Inner classes are fine.
  - Nested functions have read-only access to variables defined in enclosing scopes.
- **Comprehensions & Generator Expressions**
  - Okay to use for simple cases.
- **Default Iterators and Operators**
  - Container types, like dictionaries and lists, define default iterators and membership test operators (“in” and 
  “not in”) 
  - Use default iterators and operators for types that support them, like lists, dictionaries, and files.
  - Do not mutate a container while iterating over it.
- **Generators** 
  - A generator function returns an iterator that yields a value each time it executes a yield statement.
  - Use as needed.
  - Use “Yields:” rather than “Returns:” in the docstring for generator functions.
- **Lambda Functions**
  - Okay for one-liners. Prefer generator expressions over map() or filter() with a lambda.
- **Conditional Expressions**
  - Conditional expressions (sometimes called a “ternary operator”) are mechanisms that provide a shorter syntax for 
  if statements. For example: `x = 1 if cond else 2.`
  - Okay for simple cases.
- **Default Argument Values** 
  - You can specify values for variables at the end of a function’s parameter list, e.g., `def foo(a, b=0):`. If 'foo' 
  is called with only one argument, `b` is set to 0. If it is called with two arguments, `b` has the value of the 
  second argument.
  - Generally okay to do.
- **Properties**
  - Properties may be used to control getting or setting attributes that require trivial computations or logic. 
  Property implementations must match the general expectations of regular attribute access: that they are cheap,
  straightforward, and unsurprising.
  - Properties should be created with the `@property` decorator
  - Do not use properties to implement computations a subclass may ever want to override and extend.
- **True/False Evaluations** 
  - Use the “implicit” false if at all possible. e.g. e.g., `if foo:` rather than `if foo != []:`
  - Boolean conditions are most often faster.
  - `0, None, [], {}, ''` are evaluated as false in a boolean context.
- **Lexical Scoping** 
  - A nested Python function can refer to variables defined in enclosing functions, but cannot assign to them. 
  Variable bindings are resolved using lexical scoping, that is, based on the static program text. Any assignment to 
  a name in a block will cause Python to treat all references to that name as a local variable, even if the use 
  precedes the assignment. If a global declaration occurs, the name is treated as a global variable.
  - Okay to use
- **Function and Method Decorators** 
  - a.k.a “the `@` notation”
  - One common decorator is @property, used for converting ordinary methods into dynamically computed attributes. 
  However, the decorator syntax allows for user-defined decorators as well.
  - Okay to use
  - Elegantly specifies some transformation on a method
  - might eliminate some repetitive code
  - should follow the same import and naming guidelines as functions.
  - Okay to use when there is a clear advantage
  - Avoid `staticmethod`
  - Use `classmethod` only when writing a named constructor or a class-specific routine that modifies necessary global 
  state such as a process-wide cache.
- **Threading** 
  - Use the Queue module’s `Queue` data type as the preferred way to communicate data between threads. Otherwise, use 
  the threading module and its locking primitives. Prefer condition variables and `threading.Condition` instead of using 
  lower-level locks.
- **Power Features** 
  - Avoid
- **Modern Python: from __future__ imports** 
  - Being able to turn on some of the more modern features via from __future__ import statements allows early use of 
  features from expected future Python versions.
  - Use of `from __future__ import` statements is encouraged.
  - Allows a given source file to start using more modern Python syntax features today.
  - Once you no longer need to run on a version where the features are hidden behind a `__future__` import, feel free to 
  remove those lines.
- Type Annotated Code
  - type hints for function or method arguments and return values
  - e.g. `def func(a: int) -> List[int]:`
  - Improve the readability and maintainability of your code.

### Style Rules

- Semicolons
  - Do not terminate your lines with semicolons, and do not use semicolons to put two statements on the same line.
- Line length
  - Maximum line length is 80 characters. 
  - Explicit Exceptions:
    - Long import statements. 
    - URLs, pathnames, or long flags in comments. 
    - Long string module level constants not containing whitespace that would be inconvenient to split across lines 
    such as URLs or pathnames.
  - Make use of Python’s implicit line joining inside parentheses, brackets and braces. 
  If necessary, you can add an extra pair of parentheses around an expression.
  - When a literal string won’t fit on a single line, use parentheses for implicit line joining.
- Parentheses
  - Use sparingly
  - It is fine, though not required, to use parentheses around tuples. Do not use them in return statements or 
  conditional statements unless using parentheses for implied line continuation or to indicate a tuple.
- Indentation
  - Indent your code blocks with 4 spaces.
  - Never use tabs or mix tabs and spaces.
  - Trailing Commas:
    - Recommended only when the closing container token `]`, `)`, or `}` does not appear on the same line as the final 
    element.
    - The presence of a trailing comma is also used as a hint to auto-format the container of items to one item per line 
    when the `,` after the final element is present.
- Blank Lines
  - Two blank lines between top-level definitions, be they function or class definitions.
  - One blank line between method definitions and between the class line and the first method.
  - No blank line following a def line.
  - Single blank lines as you judge appropriate within functions or methods.
- Whitespace
  - Follow standard typographic rules for the use of spaces around punctuation.
  - No whitespace inside parentheses, brackets or braces.
  - No whitespace before a comma, semicolon, or colon. 
  - Do use whitespace after a comma, semicolon, or colon, except at the end of the line.
  - No whitespace before the open paren/bracket that starts an argument list, indexing or slicing.
  - No trailing whitespace.
  - Surround binary operators with a single space on either side for assignment (`=`), comparisons 
  (`==, <, >, !=, <>, <=, >=, in, not in, is, is not`), and Booleans (`and, or, not`). 
  - Use your better judgment for the insertion of spaces around arithmetic operators (`+, -, *, /, //, %, **, @`).
  - Never use spaces around `=` when passing keyword arguments or defining a default parameter value, with one 
  exception: when a type annotation is present, do use spaces around the `=` for the default parameter value.
  - Don’t use spaces to vertically align tokens on consecutive lines, since it becomes a maintenance burden.
- Shebang Line
  - Most .py files do not need to start with a `#!` line. Start the main file of a program with 
  `#!/usr/bin/env python3` (to support virtualenvs) or `#!/usr/bin/python3` per PEP-394.
  - This line is used by the kernel to find the Python interpreter, but is ignored by Python when importing modules. 
  It is only necessary on a file intended to be executed directly.
- Comments and Docstrings
  - Be sure to use the right style for module, function, method docstrings and inline comments.
  - Docstrings:
    - A string that is the first statement in a package, module, class or function.
    - Can be extracted automatically through the `__doc__` member of the object and are used by `pydoc`.
    - (Try running `pydoc` on your module to see how it looks.)
    - Always use the three double-quote `"""` format for docstrings 
    - A docstring should be organized as a summary line (one physical line not exceeding 80 characters) terminated by a 
    period, question mark, or exclamation point. When writing more (encouraged), this must be followed by a blank line, 
    followed by the rest of the docstring starting at the same cursor position as the first quote of the first line. 
    - More Formatting Guidelines:
      - Modules:
        - Every file should contain license boilerplate. Choose the appropriate boilerplate for the license used by the 
        project (for example, Apache 2.0, BSD, LGPL, GPL)
        - Files should start with a docstring describing the contents and usage of the module.
      - Functions and Methods:
        - Should have a docstring unless: not externally visible, very short, or obvious
        - Should give enough information to write a call to the function without reading the function’s code.
        - Should describe the function’s calling syntax and its semantics.
        - Descriptive-style (`"""Fetches rows from a Bigtable."""`), not imperative-style 
        (`"""Fetch rows from a Bigtable."""`)
        - A method that overrides a method from a base class may have a simple docstring sending the reader to its 
        overridden method’s docstring, unless substantially different.
        - Certain aspects of a function should be documented in special sections, listed below:
          - Args:
            - List each parameter by name.
            - A description should follow the name, and be separated by a colon followed by either a space or newline.
            - If the description is too long to fit on a single 80-character line, use a hanging indent of 2 or 4 spaces
            more than the parameter name.
            - Should include required type(s) if the code does not contain a corresponding type annotation.
            - If a function accepts `*foo` (variable length argument lists) and/or `**bar` (arbitrary keyword 
            arguments), they should be listed as `*foo` and `**bar`.
          - Returns (or Yields, for generators):
            - Describe the type and semantics of the return value.
            - If the function only returns None, this section is not required.
            - may also be omitted if the docstring starts with Returns or Yields
          - Raises:
            - List all exceptions that are relevant to the interface followed by a description.
            - Do not document exceptions that get raised if the API specified in the docstring is violated.
      - Property: 
        - Should use the same style as the docstring for an attribute or a function argument.
      - Classes:
        - Should have a docstring below the class definition describing the class.
        - If your class has public attributes, they should be documented here in an Attributes section and follow the 
        same formatting as a function’s Args section.
      - Blocks an Inline Comments:
        - The final place to have comments is in tricky parts of the code.
        - Complicated operations get a few lines of comments before the operations commence.
        - Non-obvious ones get comments at the end of the line.
        - To improve legibility, these comments should start at least 2 spaces away from the code with the comment 
        character #, followed by at least one space before the text of the comment itself.
        - Never describe the code. Assume the person reading the code knows Python (though not what you’re trying to 
        do) better than you do.
      - Punctuation, Spelling, and Grammar:
        - Comments should be as readable as narrative text, with proper capitalization and punctuation.
        - Complete sentences are more readable than sentence fragments.
        - Shorter comments, such as comments at the end of a line of code, can sometimes be less formal, but you should 
        be consistent with your style.
- Strings
  - Use an f-string, the % operator, or the format method for formatting strings, even when the parameters are all 
  strings.
  - Use your best judgment to decide between `+` and `%` (or `format`).
  - Do not use `%` or the `format` method for pure concatenation.
  - Avoid using the + and += operators to accumulate a string within a loop. Instead, add each substring to a list and 
  `''.join` the list after the loop terminates, or write each substring to an `io.StringIO` buffer.
  - Be consistent with your choice of string quote character within a file. Pick `'` or `"` and stick with it.
  - Prefer `"""` for multi-line strings rather than `'''`.
  - Multi-line strings do not flow with the indentation of the rest of the program. If you need to avoid embedding extra
  space in the string, use either concatenated single-line strings or a multi-line string with textwrap.dedent() to 
  remove the initial space on each line ` ("And this too is fine if you cannot accept\n"
                   "extraneous leading spaces.")`
  - Logging:
    - For logging functions that expect a pattern-string (with %-placeholders) as their first argument: Always call them 
    with a string literal (not an f-string!) as their first argument with pattern-parameters as subsequent arguments. 
  - Errors:
    - Error messages (such as: message strings on exceptions like ValueError, or messages shown to the user) should 
    follow three guidelines:
      - The message needs to precisely match the actual error condition.
      - Interpolated pieces need to always be clearly identifiable as such.
      - They should allow simple automated processing (e.g. grepping).
- Files, Sockets, and similar Stateful Resources
  - Explicitly close files and sockets when done with them.
  - This rule naturally extends to closeable resources (database connections, mmap mappings, h5py File objects, and 
  matplotlib.pyplot figure windows.)
  - The preferred way to manage files and similar resources is using the `with` statement.
  - For file-like objects that do not support the with statement, use `contextlib.closing()`.
- TODO Comments
  - Use TODO comments for code that is temporary, a short-term solution, or good-enough but not perfect.
  - begins with the string TODO in all caps and a parenthesized name, e-mail address, or other identifier of the person 
  or issue with the best context about the problem. This is followed by an explanation of what there is to do.
  `# TODO(x----@gmail.com): Use a "*" here for string repetition.`
- Imports formatting
  - Imports should be on separate lines
  - Imports are always put at the top of the file, just after any module comments and docstrings and before module 
  globals and constants. 
  - Imports should be grouped from most generic to least generic:
    1) Python future import statements.
    2) Python standard library imports.
    3) third-party module or package imports.
    4) Code repository sub-package imports.
  - Within each grouping, imports should be sorted lexicographically, ignoring case, according to each module’s full 
  package path.
  - Code may optionally place a blank line between import sections.
- Statements
  - Generally only one statement per line.
  - You may put the result of a test on the same line as the test only if the entire statement fits on one line.
- Getters and Setters
  - Also called accessors and mutators
  - Should be used when they provide a meaningful role or behavior for getting or setting a variable’s value.
  - should be used when getting or setting the variable is complex or the cost is significant, either currently or in a 
  reasonable future.
  - If a pair of getters/setters simply read and write an internal attribute, the internal attribute should be made 
  public instead. 
  - If setting a variable means some state is invalidated or rebuilt, it should be a setter function.
  - Should follow the Naming guidelines, such as get_foo() and set_foo()
  - Alternatively, properties may be an option when simple logic is needed, or refactoring to no longer need getters and
  setters.
  - If the past behavior allowed access through a property, do not bind the new getter/setter functions to the property. 
  - Any code still attempting to access the variable by the old method should break visibly so they are made aware of 
  the change in complexity.
- Naming
  - `module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, 
  global_var_name, instance_var_name, function_parameter_name, local_var_name`.
  - Should be descriptive; eschew abbreviation.
  - Do not use abbreviations that are ambiguous or unfamiliar to readers outside your project, 
  and do not abbreviate by deleting letters within a word.
  - Always use a .py filename extension. Never use dashes.
  - Avoid:
    - single character names except counters or iterators (e.g. `i`, `j`, `k`, `v`, et al.)
    - `i` might be a fine name for 5-line code block but within multiple nested scopes, it is likely too vague.
    - dashes (`-`) in any package/module name
    - `__double_leading_and_trailing_underscore__` names (reserved by Python)
    - names that needlessly include the type of the variable
  - Conventions:
    - “Internal” means internal to a module, or protected or private within a class.
    - Prepending a single underscore (`_`) has some support for protecting module variables and functions.
    - Prepending a double underscore (__ aka “dunder”) to an instance variable or method effectively makes the variable 
    or method private to its class (using name mangling); Prefer a single underscore.
    - Place related classes and top-level functions together in a module. No need to limit yourself to one class per 
    module.
    - Use CapWords for class names, but lower_with_under.py for module names. Although there are some old modules named 
    CapWords.py, this is now discouraged because it’s confusing when the module happens to be named after a class.
    - Underscores may appear in unittest method names starting with `test` to separate logical components of the name, 
    even if those components use CapWords. One possible pattern is `test<MethodUnderTest>_<state>`; for example 
    `testPop_EmptyStack` is okay. There is no One Correct Way to name test methods. 
    - Python filenames must have a `.py` extension and must not contain dashes (`-`)
    - For mathematically heavy code, short variable names that would otherwise violate the style guide are preferred 
    when they match established notation in a reference paper or algorithm. When doing so, reference the source of all 
    naming conventions in a comment or docstring or, if the source is not accessible, clearly document the naming 
    conventions.
- Main
  - In Python, `pydoc` as well as unit tests require modules to be importable.
  - If a file is meant to be used as an executable, its main functionality should be in a `main()` function, and your 
  code should always check `if __name__ == '__main__'` before executing your main program, so that it is not executed 
  when the module is imported.
- Function length
  - Prefer small and focused functions.
  - If a function exceeds about 40 lines, think about whether it can be broken up without harming the structure of the 
  program.
  - Keeping your functions short and simple makes it easier for other people to read and modify your code.
- Type Annotations
  - General Rules
    - Familiarize yourself with [PEP-484](https://www.python.org/dev/peps/pep-0484/).
    - In methods, only annotate `self`, or `cls` if it is necessary for proper type information. 
    `e.g., @classmethod def create(cls: Type[T]) -> T: return cls()`
    - If any other variable or a returned type should not be expressed, use Any.
    - You are not required to annotate all the functions in a module.
  - Line Breaking
    - Try to follow the existing indentation rules.
    - After annotating, many function signatures will become “one parameter per line”.
    - Always prefer breaking between variables, and not, for example, between variable names and type annotations.
    - If the combination of the function name, the last parameter, and the return type is too long, indent by 4 in a 
    new line.
    - When the return type does not fit on the same line as the last parameter, the preferred way is to indent the 
    parameters by 4 on a new line and align the closing parenthesis with the `def`.
    - As in the examples above, prefer not to break types.
    - If a single name and type is too long, consider using an alias for the type. 
  - Forward Declarations
    - If you need to use a class name from the same module that is not yet defined, use a string for the class name.
  - Default Values
    - Use spaces around the `=` only for arguments that have both a type annotation and a default value.
  - NoneType
    - `NoneType` is a “first class” type, and for typing purposes, `None` is an alias for `NoneType`. If an argument 
    can be `None`, it has to be declared! You can use `Union`, but if there is only one other type, use `Optional`.
    - Use explicit `Optional` instead of implicit `Optional`. Earlier versions of PEP 484 allowed `a: str = None` to be 
    interpreted as `a: Optional[str] = None`, but that is no longer the preferred behavior.
  - Type Aliases
    - You can declare aliases of complex types. 
    - The name of an alias should be CapWorded.
  - Ignoring Types
    - You can disable type checking on a line with the special comment `# type: ignore.`
  - Typing Variables
    - If an internal variable has a type that is hard or impossible to infer, you can specify its type in a couple ways.
      - Use a `# type:` comment on the end of the line
      - Use a colon and type between the variable name and value, as with function arguments.
  - Tuples vs Lists
    - Typed lists can only contain objects of a single type. 
    - Typed tuples can either have a single repeated type or a set number of elements with different types. 
  - TypeVars
    - The Python type system has generics. The factory function `TypeVar` is a common way to use them.
    - A common predefined type variable in the `typing` module is `AnyStr`. Use it for multiple annotations that can be 
    `bytes` or `unicode` and must all be the same type.
  - String types
    - Prefer to use `str`, though `Text` is also acceptable.
  - Imports for Typing
    - For classes from the `typing` module, always import the class itself. You are explicitly allowed to import 
    multiple specific classes on one line from the `typing` module.
  - Conditional Imports
    - Use conditional imports only in exceptional cases where the additional imports needed for type checking must be 
    avoided at runtime. 
    - Alternatives such as refactoring the code to allow top level imports should be preferred.
  - Generics
    - When annotating, prefer to specify type parameters for generic types.
    - If the best type parameter for a generic is `Any`, make it explicit, but remember that in many cases `TypeVar` 
    might be more appropriate.