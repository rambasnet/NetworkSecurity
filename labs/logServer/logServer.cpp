#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string>
#include "./util/utility.h"
#include "./util/net_utility.h"

using namespace std;

#define PORT 200   // the port users will be connecting to

char secret[] = "secret: RB2013-RB2021";

unsigned int  target = 0x11223344;

void handle_connection(int, struct sockaddr_in *); // handle web requests
void log_data(unsigned int, char *);

int main(void) {
   int sockfd, new_sockfd, yes=1; 
   struct sockaddr_in host_addr, client_addr;   // my address information
   socklen_t sin_size;

   printf("Accepting requests on port %d\n", PORT);

   if ((sockfd = socket(PF_INET, SOCK_STREAM, 0)) == -1) { 
      fatal("creating socket!");
   }

   if (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(int)) == -1)
      fatal("setting socket option SO_REUSEADDR");
   

   host_addr.sin_family = AF_INET;      // host byte order
   host_addr.sin_port = htons(PORT);    // short, network byte order
   host_addr.sin_addr.s_addr = INADDR_ANY; // automatically fill with my IP
   memset(&(host_addr.sin_zero), '\0', 8); // zero the rest of the struct

   if (bind(sockfd, (struct sockaddr *)&host_addr, sizeof(struct sockaddr)) == -1)
      fatal("binding to socket");

   if (listen(sockfd, 20) == -1)
      fatal("listening on socket");

   while(1) {   // Accept loop
      sin_size = sizeof(struct sockaddr_in);
      new_sockfd = accept(sockfd, (struct sockaddr *)&client_addr, &sin_size);
      if(new_sockfd == -1)
         fatal("accepting connection");

      handle_connection(new_sockfd, &client_addr);
   }
   return 0;
}

/* This function handles the connection on the passed socket from the
 * passed client address.  The connection is processed as a web request
 * and this function replies over the connected socket.  Finally, the 
 * passed socket is closed at the end of the function.
 */
void handle_connection(int sockfd, struct sockaddr_in *client_addr_ptr) {
   const unsigned int buffer_len = 500;
   char buffer[buffer_len];
   unsigned int length;

   length =  get_internet_data(sockfd, buffer, buffer_len);

   printf("Got request from %s:%d\n", inet_ntoa(client_addr_ptr->sin_addr), ntohs(client_addr_ptr->sin_port));
   printf("Received %d bytes.\n", length);

   log_data(length, buffer);
   
   echo(sockfd, buffer);
   shutdown(sockfd, SHUT_RDWR);
}

/*
This function logs the buffer on standard output
*/
void log_data(unsigned int length, char *data) {
   printf("The input buffer is @:    0x%08x\n",   (unsigned int)  data);
   printf("The secret message is @:  0x%08x\n",   (unsigned int)  secret);
   printf("The target variable is @: 0x%08x\n",   (unsigned int)  &target);
   
   printf(data);

   printf("\nDEBUG: ");
   printf("The target value: %d \t 0x%08x\n",  target, target);

   printf("\n(^_^)(^_^)  Logged successfully! (^_^)(^_^)\n");
}