import sys
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener
from antlr4.tree.Trees import Trees
from cvdLexer import cvdLexer
from cvdParser import cvdParser


# ----------------------------
# Custom Utility Functions
# ----------------------------

def parse_script(file_path: str):
    """Parse the CVD control script and print tree + summary info."""

    input_stream = FileStream(file_path, encoding='utf-8')

    lexer = cvdLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = cvdParser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(ConsoleErrorListener())

    tree = parser.script()

    print("\n✅ Parse completed successfully!\n")

    # Compact Tree
    print("=== Compact Parse Tree ===\n")
    print(Trees.toStringTree(tree, None, parser))

    # Pretty Tree
    print("\n=== Pretty Parse Tree ===\n")
    pretty_print(tree, parser)

    # Extract details
    print("\n=== Summary Report ===")
    extract_summary(tree, parser)


def pretty_print(tree, parser, indent=0):
    """Recursively print parse tree in an indented format."""
    if isinstance(tree, TerminalNode):
        text = tree.getText().strip()
        if text and text != "<EOF>":
            print("  " * indent + f"'{text}'")
        return

    rule_name = parser.ruleNames[tree.getRuleIndex()]
    print("  " * indent + rule_name)
    for i in range(tree.getChildCount()):
        pretty_print(tree.getChild(i), parser, indent + 1)


# ----------------------------
# Summary Extraction
# ----------------------------

def extract_summary(tree, parser):
    """Extract param/var/step definitions and print report."""
    params, vars_, steps = [], [], []

    collect_info(tree, parser, params, vars_, steps)

    print("\n📘 Parameters:")
    if params:
        for p in params:
            print(f"  - name: {p['name']}, value: {p['value']}, runtime: {p['runtime']}")
    else:
        print("  (none)")

    print("\n📗 Variables:")
    if vars_:
        for v in vars_:
            print(f"  - name: {v['name']}, value: {v['value']}")
    else:
        print("  (none)")

    print("\n📙 Steps:")
    if steps:
        for s in steps:
            print(f"  - name: {s['name']}, duration: {s['time']}")
    else:
        print("  (none)")


def collect_info(node, parser, params, vars_, steps):
    """Recursive AST walk to collect definitions."""
    if isinstance(node, TerminalNode):
        return

    rule_name = parser.ruleNames[node.getRuleIndex()]

    # paramDecl
    if rule_name == "paramDecl":
        runtime_flag = False
        name = None
        value = None
        for child in node.children:
            t = child.getText()
            if t == "runtime":
                runtime_flag = True
            elif name is None and t not in ["param", "runtime", "=", ";"]:
                name = t
            elif t.replace('.', '', 1).isdigit():
                value = t
        params.append({"name": name, "value": value, "runtime": runtime_flag})

    # varDecl
    elif rule_name == "varDecl":
        name = None
        value = None
        for child in node.children:
            t = child.getText()
            if name is None and t not in ["var", "=", ";"]:
                name = t
            elif t.replace('.', '', 1).isdigit():
                value = t
        vars_.append({"name": name, "value": value})

    # stepDecl
    elif rule_name == "stepDecl":
        name = None
        time = None
        for child in node.children:
            t = child.getText()
            if t.startswith('"') and t.endswith('"'):
                name = t.strip('"')
            elif t.replace('.', '', 1).isdigit():
                time = t
        steps.append({"name": name, "time": time})

    # recurse
    for i in range(node.getChildCount()):
        collect_info(node.getChild(i), parser, params, vars_, steps)


# ----------------------------
# Main
# ----------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cvd_test.py <input_file>")
        sys.exit(1)

    parse_script(sys.argv[1])
