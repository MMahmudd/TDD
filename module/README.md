Here's an example of modular programming using the C language:

Module 1: math_operations.h

Module 2: math_operations.c

Main Program: main.c

In this example, the program is divided into two modules: math_operations.h and math_operations.c. The math_operations.h module contains the function declarations for various mathematical operations, and the math_operations.c module implements the functions. The main program, main.c, utilizes the functions defined in the modules.

This modular approach allows for code organization and reusability. The functions are encapsulated within modules, and the main program imports the necessary module (math_operations.h) to access the functions. The modules can be developed and maintained independently, promoting modular programming principles.

To compile and run the program, you can use a C compiler (e.g., gcc) and execute the following commands:

bash
Copy code
gcc -c math_operations.c
gcc -o main main.c math_operations.o
./main
The output will display the results of the mathematical operations performed using the modular functions.







