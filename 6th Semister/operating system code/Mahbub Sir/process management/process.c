#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

void demo_fork_pid_ppid() {
    printf("\n========== 1) fork + PID/PPID ==========\n");
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork failed");
        return;
    }

    if (pid == 0) {
        // Child
        printf("Child:  PID=%d, PPID=%d\n", getpid(), getppid());
        exit(0);
    } else {
        // Parent
        printf("Parent: PID=%d, ChildPID=%d\n", getpid(), pid);
        wait(NULL);
        printf("Parent: Child finished (wait done)\n");
    }
}

void demo_exec() {
    printf("\n========== 2) exec() demo ==========\n");
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork failed");
        return;
    }

    if (pid == 0) {
        // Child replaces itself with `ls -l`
        printf("Child (before exec): PID=%d\n", getpid());
        execl("/bin/ls", "ls", "-l", NULL);

        // If exec fails:
        perror("exec failed");
        exit(1);
    } else {
        wait(NULL);
        printf("Parent: exec child finished\n");
    }
}

void demo_zombie() {
    printf("\n========== 3) Zombie process demo ==========\n");
    printf("Note: Parent will NOT wait immediately. Child becomes zombie briefly.\n");

    pid_t pid = fork();

    if (pid < 0) {
        perror("fork failed");
        return;
    }

    if (pid == 0) {
        printf("Zombie Child: exiting now. PID=%d\n", getpid());
        exit(0);
    } else {
        printf("Parent: PID=%d, created child PID=%d\n", getpid(), pid);
        printf("Parent sleeping 8 seconds (child is zombie during this time)...\n");
        sleep(8);

        // Now parent collects child
        wait(NULL);
        printf("Parent: now wait() done, zombie cleared\n");
    }
}

void demo_orphan() {
    printf("\n========== 4) Orphan process demo ==========\n");
    printf("Note: Parent will exit, child will continue and get adopted (PPID changes).\n");

    pid_t pid = fork();

    if (pid < 0) {
        perror("fork failed");
        return;
    }

    if (pid == 0) {
        printf("Orphan Child: PID=%d, initial PPID=%d\n", getpid(), getppid());
        sleep(5);
        printf("Orphan Child: after parent exit, new PPID=%d\n", getppid());
        exit(0);
    } else {
        printf("Parent (will exit immediately): PID=%d, child PID=%d\n", getpid(), pid);
        printf("Parent exiting now...\n");
        exit(0); // parent exits => child becomes orphan
    }
}

int main() {
    printf("=========== PROCESS MANAGEMENT (ALL-IN-ONE) ===========\n");

    // 1) fork + pid/ppid + wait
    demo_fork_pid_ppid();

    // 2) exec demo
    demo_exec();

    // 3) zombie demo
    demo_zombie();

    // 4) orphan demo (this will terminate parent process)
    // So keep it last.
    demo_orphan();

    return 0;
}