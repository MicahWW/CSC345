#include <stdio.h>
////////////////////////////////////////////////////////////////////////////////////////
struct job {
	int id;
	int burstTime;
	int arrivalTime;
	int remainingTime;
	// rest of variables to be determined once job "runs"
	int completionTime;
	int turnaroundTime;
	int waitingTime;
	int startTime;
	int responseTime;
};

void job_setJob(struct job* this, int Id, int Bt, int At) {
	this->id = Id;
	this->burstTime = this->remainingTime = Bt;
	this->arrivalTime = At;
}

int job_timeLeft(struct job* this) {
	return this->remainingTime;
}

int job_getBurstTime(struct job* this) {
	return this->burstTime;
}

int job_getArrivalTime(struct job* this) {
	return this->arrivalTime;
}

// "runs" the job
// it sets remaining Time to 0 and computes the stats for the other variables
void job_run(struct job* this, int time) {
	this->remainingTime = 0;
	this->startTime = time;
	this->completionTime = time + this->burstTime;
	this->turnaroundTime = this->completionTime - this->arrivalTime;
	this->waitingTime = this->turnaroundTime - this->burstTime;
	this->responseTime = this->startTime - this->arrivalTime;
}
////////////////////////////////////////////////////////////////////////////////////////
// In this funcion you must remember to pass the address of each job being processed otherwise it will try to refer a local variable which will not exist
struct job * shortest(struct job listJob[], int time) {
	// counter for for statments
	int i;
	// counter for next spot in availableJobs
	int j = 0;
	struct job * availableJobs[10];

	// finds the jobs that have come in by currentTime
	struct job * test;
	for(i=0; i<10; i++) {
		test = &listJob[i];

		// if the arrival time is lower or the same to the current time, shown as variable time, it adds it to avilableJobs and adds to j, the counter for availableJobs.
		if (job_getArrivalTime(test) <= time) {
			// checking to see if the job has already been compleated
			if (job_timeLeft(test) != 0) {
				availableJobs[j] = test;
				j++;
			}
		}
	}

	//sets default shortest job
	struct job * shortestJob;
	struct job * test2;
	shortestJob = availableJobs[0];

	for (i=1; i<j; i++) {
		test2 = availableJobs[i];
		if (job_getBurstTime(shortestJob) > job_getBurstTime(test2)) {
			shortestJob = test2;
		}
	}
	return shortestJob;
}
////////////////////////////////////////////////////////////////////////////////////////
void printJobs(struct job listJob[]) {
	int i;
	struct job printJob;
	printf("\n");
        for(i=0; i<10; i++) {
                printJob = listJob[i];
                printf("Process ID: %d\tBurst Time: %d\t\tCompletion Time: %d\tTurnaround Time: %d\tWaitingTime: %d\t\tResponse Time: %d\n",
	                printJob.id, printJob.burstTime, printJob.completionTime, printJob.turnaroundTime, printJob.waitingTime, printJob.responseTime);
        }
	printf("\n");
}
////////////////////////////////////////////////////////////////////////////////////////
int main(int argc, char *argv[]){
        int currentTime = 0;

	// creates the variables with struct job
	struct job p1;
	struct job p2;
	struct job p3;
	struct job p4;
	struct job p5;
	struct job p6;
	struct job p7;
	struct job p8;
	struct job p9;
	struct job p10;

	// gives each variable its parameters
	job_setJob(&p1, 1, 255, 0);
	job_setJob(&p2, 2, 850, 1);
	job_setJob(&p3, 3, 80, 2);
	job_setJob(&p4, 4, 155, 3);
	job_setJob(&p5, 5, 800, 4);
	job_setJob(&p6, 6, 125, 5);
	job_setJob(&p7, 7, 75, 6);
	job_setJob(&p8, 8, 555, 7);
	job_setJob(&p9, 9, 90, 8);
	job_setJob(&p10, 10, 450, 9);

	// creates list of jobs and sets them in order in list by ID (which really doesn't matter)
	struct job jobList[10];
	jobList[0] = p1;
	jobList[1] = p2;
	jobList[2] = p3;
	jobList[3] = p4;
	jobList[4] = p5;
	jobList[5] = p6;
	jobList[6] = p7;
	jobList[7] = p8;
	jobList[8] = p9;
	jobList[9] = p10;

	int i;
	struct job * test;

	for (i=0; i<10; i++) {
		// finds the next job to do by finding the lowest process ID with remaining time left/hasn't been comleated (seeing as this is first come first serve)
		test = shortest(jobList, currentTime);
		job_run(test, currentTime);
		//keeps up with the current time by taking burst time and adding it to current time
		currentTime += job_getBurstTime(test);
	}

	printJobs(jobList);
}

