#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char *ptr;

    if(argc < 3) {
        printf("Usage: %s <env variable name> <target program name>\n", argv[0]);
    }
    else {
        ptr = getenv(argv[1]); /* get env var location */
        int diff = (strlen(argv[0]) - strlen(argv[2]))*2;
        ptr += diff; /* adjust for program name */
        printf("%s will be at %p with reference to %s\n", argv[1], ptr, argv[2]);
    }
    return 0;
}
