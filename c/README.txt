Thanks for downloading the C branch of savesys.

To get started, go into savesys.c and change the pre-processor macros
to the name and length you'd like your save file to be.

Example function usage:

#include "savesys.h"

save_exists();
save_writer(5, 7);
int * save = save_reader();
