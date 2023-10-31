FILE *f;
f = fopen("x.log", "a+"); // a+ (create + append) option will allow appending which is useful in a log file
if (f == NULL) { /* Something is wrong   */}
fprintf(f, "I'm logging something ...\n");