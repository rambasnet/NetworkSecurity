#include <cstdio>
#include <cstring>
#include <string>

using namespace std;


int main(int argc, char * argv[]) {
   char c_string[10] = "sample";
   int A = -73;
   unsigned int B = 31337;
   string cpp_string = "Hello from C++";

   // Example of printing with different format string
   printf("[A] Dec: %d, Hex: %x, Unsigned: %u\n", A, A, A);
   printf("[B] Dec: %d, Hex: %x, Unsigned: %u\n", B, B, B);
   printf("[field width on B] 3: '%3u', 10: '%10u', 8: '%08u'\n", B, B, B);
   printf("[c_string] %s is @ %p\n", c_string, c_string);
   printf("[cpp_string] %s is @ 0x%08x\n", cpp_string.c_str(), &cpp_string);

   // Example of unary address operator (dereferencing) and a %x format string
   printf("variable A is at address: %p\n", &A);
   return 0;
}