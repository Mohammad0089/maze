from stack import myStack


rev_str =  myStack()

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string=""

for i in string:
    rev_str.push(i)
    
while not rev_str.is_empty():
    reversed_string += "".join(rev_str.pop())

if __name__ == "__main__":
    print(reversed_string)