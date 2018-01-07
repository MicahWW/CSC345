class job {
	public int id;
	public int burstTime;
	public int arivalTime;
	public int remainingTime;
	// rest of variables to be deterimed once job "runs"
	public int completionTime;
	public int turnaroundTime;
	public int waitingTime;
	public int startTime;
	public int responseTime;

	public job(int ID, int BT, int AT) {
		id = ID;
		burstTime = remainingTime = BT;
		arivalTime = AT;
	}

	public int timeLeft() {
		return remainingTime;
	}

        public int getBurstTime() {
		return burstTime;
	}

	// "runs" the job
	// it sets remaining Time to 0 and computes the stats for the other varables
	public void run(int time) {
		remainingTime = 0;
		startTime = time;
		completionTime = time + burstTime;
		turnaroundTime = completionTime - arivalTime;
		waitingTime = turnaroundTime - burstTime;
		responseTime = startTime - arivalTime;
	}

	public String toString() {
		return ("Process ID: " + id + "\tBurst Time: " + burstTime + "\t\tCompletion Time: " + completionTime + "\tTuraround Time: " + turnaroundTime + "\tWaiting Time: " + waitingTime + "\t\tResponseTime: " + responseTime);
	}
}

public class FCFS {

	// finds the job with the lowest process id that doesn't have a remainingTime of 0
	public static job oldest(job listJob[]) {
		job a;
		int i;

		// going through list
		for(i=0; i<10; i++) {
			a = listJob[i];

			// checks for remainingTime
			// if no time is left it continues on
			if (a.timeLeft() != 0) {
				return listJob[i];
			}
		}
		// it wants to have a return statment for some reason
		System.out.println("Well it did something wrong");
		return listJob[0];
	}

	// FCFS
	public static void main(String[] args) {
	int currentTime = 0;

	// creates all the jobs
	job p1 = new job(1, 255, 0);
	job p2 = new job(2, 850, 1);
	job p3 = new job(3, 80, 2);
	job p4 = new job(4, 155, 3);
	job p5 = new job(5, 800, 4);
	job p6 = new job(6, 125, 5);
	job p7 = new job(7, 75, 6);
	job p8 = new job(8, 555, 7);
	job p9 = new job(9, 90, 8);
	job p10 = new job(10, 450, 9);

	// creates list of jobs and sets them in order in list by ID (which really doesn't matter)
	job[] jobList = new job[10];
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
	job a;

	// "runs" all of the jobs
	for (i=0; i<10; i++) {
		// finds the next job to do by finding the lowest process ID with remaining time left/hasn't been compleated (seeing as this is first come first serve)
		a  = oldest(jobList);
		a.run(currentTime);
		// keeps up with the current time by taking burst time and adding it to current time
		currentTime += a.getBurstTime();
	}

	// prints out all of jobs with all their stats (waiting time, ect)
	for (i=0; i<10; i++) {
		System.out.println(jobList[i]);
	}
	}
}
