# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>
# include <sys/wait.h>

int main() {
	int chid;
	printf("P: Statement 1 \n");
	chid = fork();	
	
	if (chid == 0) {
		printf("C: Statement 3 \n");
		exit(0);
	}
	
	printf("P: Statement 2 \n");
	wait(0);
	printf("P: Statement 4 \n");
	
	return 0;
}
