#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void badfunction(char *data) {
    char input[200];
    strcpy(input, data);
    printf("Hello, ");
    printf(input);
    printf("\ninput is @ 0x%08x\n", &input);
    //unsigned int ebp asm("ebp");
    //printf("return address @ 0x%08x\n", (ebp+4));
}

int main(int argc, char* argv[]) {
    if (argc == 1) {
        printf("Usage: %s <name>\n", argv[0]);
        exit(0);
    }
    badfunction(argv[1]);
    printf("%s\n", "good bye!");
    return 0;
}