When you run this program, the output looks like this:

Hello, Alice  
Hello, Bob

You can view the execution of this program at https://autbor.com/hellofunc2/. The definition of the hello() function in this program has a parameter called name ➊. Parameters are variables that contain arguments. When a function is called with arguments, the arguments are stored in the parameters. The first time the hello() function is called, it is passed the argument 'Alice' ➌. The program execution enters the function, and the parameter name is automatically set to 'Alice', which is what gets printed by the print() statement ➋.

One special thing to note about parameters is that the value stored in a parameter is forgotten when the function returns. For example, if you added print(name) after hello('Bob') in the previous program, the program would give you a NameError because there is no variable named name. This variable is destroyed after the function call hello('Bob') returns, so print(name) would refer to a name variable that does not exist.

This is similar to how a program’s variables are forgotten when the program terminates. I’ll talk more about why that happens later in the chapter, when I discuss what a function’s local scope is.