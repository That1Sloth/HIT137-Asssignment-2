# Assignment 2 - Question 2

def format_number(value) -> str:
    if isinstance(value, int):
        return str(value)

    if isinstance(value, float):
        if value.is_integer():
            return str(int(value))

        return f"{value:.4f}".rstrip("0").rstrip(".")
    return str(value)

def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        character = expression[i]  
        if character.isspace():
            i += 1 
            continue

        if character.isdigit():
            start = i
            while i < len(expression) and expression[i].isdigit():
                 i += 1
            if i < len(expression) and expression[i] == ".":
                i += 1
                decimal_start = i
                while i < len (expression) and expression[i].isdigit():
                        i += 1
                if decimal_start == i:
                        raise ValueError("Invalid number")
            number_text = expression[start:i]
            number_value = float(number_text)

            tokens.append (("NUM", number_value))
            continue

        if character in "+-*/%^":
            tokens.append(("OP", character))
            i += 1
            continue

        if character == "(":
            tokens.append(("LPAREN", character))
            i += 1
            continue
        if character == ")":
            tokens.append(("RPAREN", character))
            i += 1
            continue

        raise ValueError("Invalid character")
    tokens.append(("END", None))
    return tokens
tokens = []
position = 0

def current_token():
     return tokens[position]
def advance():
    global position
    token = tokens[position]
    position += 1
    return token

def parse_primary():
    token_type, token_value = current_token()

    if token_type == "NUM":
         advance()
         return ("num", token_value)
    if token_type == "LPAREN":
        advance()
        node = parse_expression()
    
        if current_token()[0] != "RPAREN":
            raise ValueError("Missing closing parenthesis")
        advance()
        return node
    raise ValueError("Expected numbers or parenthesis")
def parse_power():
    left = parse_primary()

    if current_token() == ("OP", "^"):
        advance()
        right = parse_power()
        return ("^", left, right)
    return left
def parse_unary():
    if current_token() == ("OP", "-"):
        advance()
        operand = parse_unary()
        return ("neg", operand)
    if current_token() == ("OP", "+"):
        raise ValueError("Unary plus is not supported")
    return parse_power()
def parse_term():
    left = parse_unary()
    while True:
        token = current_token()
        if token[0] == "OP" and token[1] in "*/%":
            operator = token[1]
            advance()
            right = parse_unary()
            left = (operator, left, right)
        elif token[0] == "LPAREN":
            right = parse_unary()
            left = ("*", left, right)
        else:
            break
    return left
def parse_expression():
    left = parse_term()
    while True:
        token = current_token()
        if token[0] == "OP" and token[1] in "+-":
            operator = token[1]
            advance()
            right = parse_term()
            left = (operator, left, right)
        else:
            break
    return left
def parse(token_list):
    global tokens
    global position

    tokens = token_list
    position = 0
    tree = parse_expression()
    if current_token()[0] != "END":
        raise ValueError("Unexpected token")
    return tree
def format_tree(node):
    if node[0] == "num":
        return format_number(node[1])
    if node[0] == "neg":
        return "(neg " + format_tree(node[1]) + ")"

    operator = node[0]
    left = format_tree(node[1])
    right = format_tree(node[2])

    return"(" + operator + " " + left + " " + right + ")"
def evaluate_tree(node):
    if node[0] == "num":
        return node[1]
    if node[0] == "neg":
        return evaluate_tree(node[1])
    operator = node[0]
    left = evaluate_tree(node[1])
    right = evaluate_tree(node[2])
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
            return left * right
    if operator == "/":
            return left / right
    if operator == "^":
            return left ** right
    if operator == "%":
            return left % right
    raise ValueError("Unknown operator")

test_tokens = tokenize("7 ^ 2")
test_tree = parse(test_tokens)
test_result = evaluate_tree(test_tree)

print("Question 2")
print("TOKENS:", test_tokens)
print("RAW TREE:", test_tree)
print("FORMATTED TREE:", test_tree)
print("RESULT:", format_number(test_result))
