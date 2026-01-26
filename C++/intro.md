# Intro

* isn't python and java both in the middle category of both interpreted and compiled? both are compiled to byte code
  * python goes to byte code but doesn't have JIT within the standard interpreter
* Like python is slower because of lack of JIT and dynamic typing

* Java has default initialization while c++ doesn't. This is only true in java for class
  * In Java, instance variables (non-static fields within a class) and static variables (class fields) are automatically initialized with a default value if they are not explicitly assigned one by the programmer
  * the error "variable might not have been initialized" occurs when you try to use a **local** variable in a method that the compiler determines may not have been assigned a value in all possible execution paths. Unlike class member variables, local variables do not receive a default value from the Java compiler.
  * Default variable is usually 0 or null, 
  * Data Type & Default Value (for fields)
  * byte: 0
  * short: 0
  * int: 0
  * long: 0L
  * float: 0.0f
  * double: 0.0d
  * char: '\u0000'
  * String (or any object): null
  * boolean: false*

## C++ Compilation process

* There is no advantage to intermediate object files with a single source compilation. With multiple sources you can speed up builds when making source code changes. That is, you only need to re-compile those source files with changes and then re-link the object files.

* A long time ago computers weren't as good as today. Compiling all files of a project in one step was literally impossible; there wasn't enough memory nor cpu power to process it.

* To make it possible to compile big programs an intermediate step was developed in form if object files. Compilers will first generate machine code from a single small .c source file in one step. Then linker will take all object files and link them together. That allowed to write compilers in the 70s and make it possible to compile very very big programs just by using many .c source files.


From Code to Executable:
• Preprocessing
o Preprocessor handles macros, header files, and conditional compilation.
o It replaces #define macros, expands #include directives, and processes #ifdef conditions
o Output: A text file with all macros replaced and includes expanded.
o We can force the compiler to stop after this phase: g++ -E main.cpp -o main.i
• Compilation
o Performs syntax checking and optimization
o Converts preprocessed C++ to assembly code
o Output of this phase is assembly language code
o We can force the compiler to stop after this phase: g++ -S main.cpp -o main.s
• Assembly
o Translates assembly language source code to machine language
o Output of this phase is object files (.o)
o We can force the compiler to stop after this phase: g++ -c main.cpp -o main.o
• Linking
o Combines object files and creates the final executable file
o If libraries are missing, linking will fail!
o g++ main.o -o main

* namespaces prevent conflict between functions with the same name
  * std::cout = standard character output
  * if you wanted to declare the namespace at the top of the file, then you could drop the std::

[What's the problem with "using namespace std;"?](https://stackoverflow.com/questions/1452721/whats-the-problem-with-using-namespace-std)

### The Four Steps

* Preprocessing
* Compilation (turns to assembly)
* Assembly (goes from assembly to machine code) (this is where we get to non human readable files)
* Linking