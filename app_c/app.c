#include <time.h>
#include <mongoose.h>
#include <stdio.h>
#include <stdlib.h>

const int TIMEZONE = 3;

char page_template[200];
char page_render[250];

// Load file from given path into given buffer
int load_template(char* buffer, size_t buffer_size, char* path) {
    FILE* fp = fopen(path, "r");

    if (fp == NULL) {
        printf("Could not open template file!");
        return -1;
    }

    long long length;

    fread (buffer, sizeof(char), buffer_size, fp);
    length = ftell(fp);
    buffer[length] = '\0';

    fclose(fp);
    return 0;
}

// Compute timestamp to print on the page
char* compute_time() {
    char time_string[128];

    // Get current time in UTC (GMT)
    time_t timestamp = time(&timestamp);
    struct tm moscow_time = *gmtime(&timestamp);

    // Convert time to Moscow timezone
    moscow_time.tm_hour += TIMEZONE;
    mktime(&moscow_time);

    return asctime(&moscow_time);
}

// Event handler
static void ev_handler(struct mg_connection *c, int ev, void *ev_data) {
    if (ev == MG_EV_HTTP_MSG) {
        struct mg_http_message *hm = (struct mg_http_message *) ev_data;
        if (mg_match(hm->uri, mg_str("/"), NULL)) {
            // If we are on the root, return the
            // formatted page with the timestamp

            printf("Get main page\n");

            // Insert timestamp into template
            snprintf(page_render,
                     sizeof(page_render),
                     page_template,
                     compute_time());

            // Send page to user
            mg_http_reply(c,
                          200,
                          "Content-Type: text/html\r\n",
                          "%s",
                          page_render);
        } else if (mg_match(hm->uri, mg_str("/static/style.css"), NULL)) {
            // If we are trying to access style.css, serve it

            printf("Get CSS sheet\n");

            struct mg_http_serve_opts opts = {0};
            opts.root_dir = "resources";
            mg_http_serve_dir(c, ev_data, &opts);
        } else {
            // In any other case, reply with an error

            printf("Get invalid page\n");

            mg_http_reply(c,
                          500,
                          "",
                          "{%m:%m}\n",
                          MG_ESC("error"),
                          MG_ESC("Unsupported URI"));
        }
    }
}

// Main function
int main(int argc, char *argv[]) {
    // Loading page template
    if (load_template(page_template,
                      200,
                      "./resources/templates/template.html")) {
        return -1;
    }

    if (argc < 2) {
        printf("No host address provided");
        return -1;
    }

    // Setting up http server
    struct mg_mgr mgr;
    mg_mgr_init(&mgr);
    mg_http_listen(&mgr, argv[1], ev_handler, NULL);
    printf("Server listening on %s...\n", argv[1]);
    for (;;) {
        mg_mgr_poll(&mgr, 1000);
    }
    return 0;
}
