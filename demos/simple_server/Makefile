# rule for compiling program
# Note: -m32 is required to compile into object files and the final binary
COMPILER = g++
COMPILER_FLAGS = -c -g -Wall -std=c++17 -m32
BUILD_FLAGS = -m32 -fno-stack-protector -z execstack -no-pie

# list .cpp files separated by space
CPP_FILES = main.cpp

# executable program name
PROGRAM_NAME = simple_server.exe

# rule for compiling and building program
# make or make all triggers the following rule
build:
	# disable ASLR
	echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
	# compiles .cpp to object file .o
	$(COMPILER) $(COMPILER_FLAGS) $(CPP_FILES)
	# builds executable from object files
	$(COMPILER) $(BUILD_FLAGS) -o $(PROGRAM_NAME) *.o

# rule for running programming
# make run triggers the following rule
run:
	./$(PROGRAM_NAME)

# rule for clean up
# make clean triggers the following rule
clean:
	rm -f $(PROGRAM_NAME) *.o