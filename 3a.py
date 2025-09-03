MAX_SIZE=5
stack=[]
top=-1
def push(book_title):
    global top
    if top>=MAX_SIZE-1:
        print("Stack overflow! Cannot push more books.")
    else:
        top+=1
        stack.append(book_title)
        print(f"Book'{book_title}'pushed onto the stack.")
def pop():
    global top
    if top==-1:
        print("Stack Underflow!Cannot pop any book.")
    else:
        removed_book=stack.pop()
        print(f"Book'{removed_book}'popped from the stack.")
        top-=1
def peek():
    if top==-1:
        print("Stack is empty.No book to peek.")
    else:
        print(f"Top book on the stack:'{stack[top]}'")
def display():
    if top==-1:
        print("Stack is Empty:")
    else:
        print("Books in stack (Top to Bottom):")
        for i in range(top,-1,-1):
            print(f"{i+1}.{stack[i]}")
push("Harry potter")
push("To kill a mocking bird")
push("Mahabharatham")
push("The Alchemist")
push("Fire of wings")
push("Ramayanam")

display()
peek()
pop()
pop()
display()
peek()
