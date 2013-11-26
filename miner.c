#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>
#include <sqlite3.h>
#include <sys/socket.h>


static int cb_check_difficulty(void *data, int argc, char **argv,
        char **azColName)
{
    int sockfd, portno, difficulty;
    struct hostent *server;

    portno = atoi(argv[1]);
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        error("Cannot create socket.\n");
        exit(0);
    }
    server = gethostbyname(argv[0]);
    if (server == NULL) {
        fprintf(stderr, "No such server %s\n", argv[0]);
        exit(0);
    }

    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INIT


    printf("%s, %d\n", argv[0], sockfd);
    return 0;

}

int check_difficulty()
{
    sqlite3 *db;
    char *sql;
    int rc;

    char *zErrMsg = 0;
    const char* data = "Callback called";

    sql = "SELECT ip, port FROM data WHERE relay=1 ORDER BY RANDOM()";

    rc = sqlite3_open("nodes.db", &db);
    if (rc) {
        fprintf(
            stderr,
            "Cannot open database: %s\n",
            sqlite3_errmsg(db)
        );
        exit(0);
    }

    rc = sqlite3_exec(
        db, sql, cb_check_difficulty, (void*)data,
        &zErrMsg
    );
    sqlite3_close(db);

}


static void * mine(void *arg)
{
    int difficulty;
    difficulty = check_difficulty();
}

void main()
{
    int threads = 1, i = 0, ret = -1;
    char *res;

    pthread_t * thread = malloc(sizeof(pthread_t)*threads);

    for (i = 0; i < threads; i++) {

        ret = pthread_create(&thread[i], NULL, &mine, NULL);

        if(ret != 0) {
            printf ("Create pthread error!\n");
            exit (1);
        }
    }
    for (i = 0; i < threads; i++) {
        pthread_join(thread[i], (void**)&res);
    }

}
