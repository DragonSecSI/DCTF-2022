#include "nonstd.h"
#include "sys/syscall.h"
#include "../../../common/include/kernel/syscall-definitions.h"
#include "stdlib.h"

int createprocess(const char* path, int sleep, char** args)
{
  return __syscall(sc_createprocess, (long) path, sleep, (size_t)args, 0x00, 0x00);
}

extern int main();

void _start(int argc, char** argv)
{
  exit(main(argc, argv));
}
