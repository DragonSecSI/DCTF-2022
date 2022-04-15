// ConsoleApplication1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <Windows.h>
#include <Shlwapi.h>
#include <strsafe.h>
#include <filesystem>

#pragma comment(lib, "Shlwapi.lib")

using namespace std;

wstring decrypt(int encrypted[], int length) {
    wstring plain = L"";
    for (int i = 0; i < length; i++) {
        plain = plain + (wchar_t) (encrypted[i] ^ 0x96);
    }
    //wcout << plain << endl;
    return plain;
}

void flag(int bytes[], int length) {
    wstring flag = decrypt(bytes, length);
    LPCWSTR lpFlag = flag.c_str();
    wchar_t wBuf[1024];
    wsprintfW(wBuf, lpFlag);
}

int main()
{
    const wchar_t path[] = L"\\DCTF.DLL";
    LPCWSTR lpPath;
    lpPath = path;
    int almost_there[] = { 215, 250, 251, 249, 229, 226, 182, 226, 254, 243, 228, 243, 184, 184, 184 };
    int body[] = { 210, 213, 194, 208, 184, 210, 218, 218, 182, 248, 249, 226, 182, 240, 249, 227, 248, 242, 183 };
    int title[] = { 210, 218, 218, 182, 216, 249, 226, 182, 208, 249, 227, 248, 242 };
    wstring dll_exists = decrypt(almost_there, 15);
    wstring message_body = decrypt(body, 19);
    wstring message_title = decrypt(title, 13);
    LPCWSTR lpDllExists = dll_exists.c_str();
    LPCWSTR lpMessageBody = message_body.c_str();
    LPCWSTR lpMessageTitle = message_title.c_str();
    LPWSTR lpBuf;
    wchar_t dir[1024];
    lpBuf = dir;
    GetCurrentDirectory(1024, dir);
    StrCatW(dir, path);
    if (PathFileExists(dir)) {
        wcout << lpDllExists << endl;
    }
    else {
        int msgboxID = MessageBox(NULL,
            lpMessageBody,
            lpMessageTitle,
            MB_OK
        );
        switch (msgboxID) {
        case MB_OK:
            exit(0);
        default:
            exit(0);
        }
    }
    int buf[] = { 210, 213, 194, 208, 237, 243, 161, 160, 164, 175, 164, 167, 160, 164, 175, 161, 242, 166, 247, 163, 166, 242, 163, 160, 167, 164, 165, 175, 245, 243, 247, 164, 161, 160, 162, 163, 240, 235 };
    flag(buf, 38);
}
