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

* C++ auto initializes global variables, does not initialize local variables. I'm not sure if class vars get auto initialized

* Type mismatch:
  * c++ will not give you a type error, for example if we try and assign a double to a variable initialized as an int; it will just drop it and return no error

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
  * .cpp, .cxx, .cc, .h, .hp
* Compilation (turns to assembly)
  * .s, .asm
* Assembly (goes from assembly to machine code) (this is where we get to non human readable files)
  * .o, .obj
* Linking (combining everything to make a self contained executable)
  * .exe, .out


* Strings are not a reference type in c++, unlike java
* String are also mutable in c++, because the are not reference types
* In C++, a literal like "Hello" is stored in a read-only section of memory and is essentially an immutable array of characters (const char*). However, the std::string class used in modern C++ is designed to be modified.

if we can set a pass by reference to const to it doesn't get edited and pass by reference is more memory efficient, why would we ever pass by value?

understand arrays passed to functions

Go back over arrays and static exercise

Is there any reason we would want to use string literals over the std::string class?

### Memory Segments of a program

* Code/text Segment
  * Stores actual code instructions
* Data Segment
  * for initialized global variables
* BSS Segment
  * stores uninitialized or zero-initialized global and static variables
  * The .bss section is guaranteed to be all zeros when the program is loaded into memory.
* Stack Segment
  * function calls, local variables
  * variables declared and defined in main function are also stack because its just a function
  * if a local variable is not initialized, it will get a random value from what occupied the memory beforehand
  * stack grows down
* Heap Segment
  * Heap stores objects 
  * heap grows up 

constant data types -----> code and/or data. 

static vars are initialized at compile time

**Learn different types of registers for exam next friday**

On x86-64 architecture, the return value is almost always placed in the RAX register

each time we get larger word sizes, we add letters to the register names (ax, eax, rax)
register names are backwards compatible
Storing values to a register via move 

(integer) Multiplication and division typically uses two registers because of potential overflow issues 

What registers are general purpose? 

bit shifting and bitwise operations 

bit masking (don't think we need to know details for the exam)

creating "loops" in assembly with jump 

know nop – no operation; does nothing; useful for timing

review namespace vs library 


order of operations for some reason? 

**Maybe**
cin vs getline (why using them together causes problems, cin.ignore)
getline also only takes in string
function declaration vs definition, prototype (maybe)
names spaces and headers
Then have compilation process?
converting to hexidecimal


**Definitely**
so have memory stack
auto initialization when and where
why you can't return local variables by reference (because you are returning an address on the stack that will get destroyed once the stack frame is gone)

Basic computer architecture (Von neumann, CPU components, system Bus (data bus, address bus, control bus, bus is wires + protocols), types of memories, AX, BX, CX, DX registers, flag registers, program counter, instruction register, cache )
High level explanation of a register
fetch decode execute cycle: what does each step do?
ax, eax, reax register sizes

a quick note on big vs little endian
Then have assembly portion!!
