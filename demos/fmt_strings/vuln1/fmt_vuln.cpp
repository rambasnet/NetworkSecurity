#include <cstdio>
#include <cstdlib>
#include <cstring>

int main(int argc, char *argv[]) {

   static int test_val = -72;
   char text[1024];
   
   if(argc < 2) {
      printf("Usage: %s <text to print>\n", argv[0]);
      exit(0);
   }

   strcpy(text, argv[1]);

   printf("The right way to print user-controlled input:\n");
   printf("%s", text);

   printf("\n\nThe wrong way to print user-controlled input:\n");
   printf(text);
   printf("\n\n");

   // Debug output
   printf("[*] test_val @ 0x%08x = %d 0x%08x\n", &test_val, test_val, test_val);
   printf("[*] text is @ %p\n", &text);
   exit(0);
}
