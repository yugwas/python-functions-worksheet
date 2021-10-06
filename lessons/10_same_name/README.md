Technically, it’s perfectly acceptable to use the same variable name for a global variable and local variables in different scopes in Python. But, to simplify your life, avoid doing this.

You can view the execution of this program at https://autbor.com/localglobalsamename/. There are actually three different variables in this program, but confusingly they are all named eggs. The variables are as follows:

➊ A variable named eggs that exists in a local scope when spam() is called.

➋ A variable named eggs that exists in a local scope when bacon() is called.

➌ A variable named eggs that exists in the global scope.

Since these three separate variables all have the same name, it can be confusing to keep track of which one is being used at any given time. This is why you should avoid using the same variable name in different scopes.