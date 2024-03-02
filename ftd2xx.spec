 1 stdcall lin_FT_Open(long ptr)                               FT_Open
 2 stdcall lin_FT_Close(ptr)                                   FT_Close
 3 stdcall lin_FT_Read(ptr ptr long ptr)                       FT_Read
 4 stdcall lin_FT_Write(ptr ptr long ptr)                      FT_Write
 5 stub lin_FT_IoCtl
 6 stdcall lin_FT_ResetDevice(ptr)                             FT_ResetDevice
 7 stdcall lin_FT_SetBaudRate(ptr long)                        FT_SetBaudRate
 8 stdcall lin_FT_SetDataCharacteristics(ptr long long long)   FT_SetDataCharacteristics
 9 stdcall lin_FT_SetFlowControl(ptr long long long)           FT_SetFlowControl
10 stdcall lin_FT_SetDtr(ptr)                                  FT_SetDtr
11 stdcall lin_FT_ClrDtr(ptr)                                  FT_ClrDtr
12 stdcall lin_FT_SetRts(ptr)                                  FT_SetRts
13 stdcall lin_FT_ClrRts(ptr)                                  FT_ClrRts
14 stdcall lin_FT_GetModemStatus(ptr ptr)                      FT_GetModemStatus
15 stdcall lin_FT_SetChars(ptr long long long long)            FT_SetChars
16 stdcall lin_FT_Purge(ptr long)                              FT_Purge
17 stdcall lin_FT_SetTimeouts(ptr long long)                   FT_SetTimeouts
18 stdcall lin_FT_GetQueueStatus(ptr ptr)                      FT_GetQueueStatus
19 stdcall lin_FT_SetEventNotification(ptr long ptr)           FT_SetEventNotification
20 stub lin_FT_GetEventStatus
21 stdcall lin_FT_GetStatus(ptr ptr ptr ptr)                   FT_GetStatus
22 stdcall lin_FT_SetBreakOn(ptr)                              FT_SetBreakOn
23 stdcall lin_FT_SetBreakOff(ptr)                             FT_SetBreakOff
24 stub lin_FT_SetWaitMask
25 stub lin_FT_WaitOnMask
26 stdcall lin_FT_SetDivisor(ptr long)                         FT_SetDivisor
27 stdcall lin_FT_OpenEx(ptr long ptr)                         FT_OpenEx
28 stdcall lin_FT_ListDevices(ptr ptr long)                    FT_ListDevices
29 stdcall lin_FT_SetLatencyTimer(ptr long)                    FT_SetLatencyTimer
30 stdcall lin_FT_GetLatencyTimer(ptr ptr)                     FT_GetLatencyTimer
31 stdcall lin_FT_SetBitMode(ptr long long)                    FT_SetBitMode
32 stdcall lin_FT_GetBitMode(ptr ptr)                          FT_GetBitMode
33 stdcall lin_FT_SetUSBParameters(ptr long long)              FT_SetUSBParameters
34 stdcall lin_FT_EraseEE(ptr)                                 FT_EraseEE
35 stdcall lin_FT_ReadEE(ptr long ptr)                         FT_ReadEE
36 stdcall lin_FT_WriteEE(ptr long long)                       FT_WriteEE
37 stdcall lin_FT_EE_Program(ptr ptr)                          FT_EE_Program
38 stdcall lin_FT_EE_Read(ptr ptr)                             FT_EE_Read
39 stdcall lin_FT_EE_UARead(ptr ptr long ptr)                  FT_EE_UARead
40 stdcall lin_FT_EE_UASize(ptr ptr)                           FT_EE_UASize
41 stdcall lin_FT_EE_UAWrite(ptr ptr long)                     FT_EE_UAWrite
42 stdcall lin_FT_W32_CreateFile(ptr long long ptr long long ptr) FT_W32_CreateFile
43 stdcall lin_FT_W32_CloseHandle(ptr)                         FT_W32_CloseHandle
44 stdcall lin_FT_W32_ReadFile(ptr ptr long ptr ptr)           FT_W32_ReadFile
45 stdcall lin_FT_W32_WriteFile(ptr ptr long ptr ptr)          FT_W32_WriteFile
46 stdcall lin_FT_W32_GetOverlappedResult(ptr ptr ptr long)    FT_W32_GetOverlappedResult
47 stdcall lin_FT_W32_ClearCommBreak(ptr)                      FT_W32_ClearCommBreak
48 stdcall lin_FT_W32_ClearCommError(ptr ptr ptr)              FT_W32_ClearCommError
49 stdcall lin_FT_W32_EscapeCommFunction(ptr long)             FT_W32_EscapeCommFunction
50 stdcall lin_FT_W32_GetCommModemStatus(ptr ptr)              FT_W32_GetCommModemStatus
51 stdcall lin_FT_W32_GetCommState(ptr ptr)                    FT_W32_GetCommState
52 stdcall lin_FT_W32_GetCommTimeouts(ptr ptr)                 FT_W32_GetCommTimeouts
53 stdcall lin_FT_W32_GetLastError(ptr)                        FT_W32_GetLastError
54 stdcall lin_FT_W32_PurgeComm(ptr long)                      FT_W32_PurgeComm
55 stdcall lin_FT_W32_SetCommBreak(ptr)                        FT_W32_SetCommBreak
56 stdcall lin_FT_W32_SetCommMask(ptr long)                    FT_W32_SetCommMask
57 stdcall lin_FT_W32_SetCommState(ptr ptr)                    FT_W32_SetCommState
58 stdcall lin_FT_W32_SetCommTimeouts(ptr ptr)                 FT_W32_SetCommTimeouts
59 stdcall lin_FT_W32_SetupComm(ptr long long)                 FT_W32_SetupComm
60 stdcall lin_FT_W32_WaitCommEvent(ptr ptr ptr)               FT_W32_WaitCommEvent
61 stdcall lin_FT_GetDeviceInfo(ptr ptr ptr ptr ptr ptr)       FT_GetDeviceInfo
62 stub lin_FT_W32_CancelIo
63 stdcall lin_FT_StopInTask(ptr)                              FT_StopInTask
64 stdcall lin_FT_RestartInTask(ptr)                           FT_RestartInTask
65 stub lin_FT_SetResetPipeRetryCount
66 stub lin_FT_ResetPort
67 stdcall lin_FT_EE_ProgramEx(ptr ptr ptr ptr ptr ptr)        FT_EE_ProgramEx
68 stdcall lin_FT_EE_ReadEx(ptr ptr ptr ptr ptr ptr)           FT_EE_ReadEx
69 stub lin_FT_CyclePort
70 stdcall lin_FT_CreateDeviceInfoList(ptr)                    FT_CreateDeviceInfoList
71 stdcall lin_FT_GetDeviceInfoList(ptr ptr)                   FT_GetDeviceInfoList
72 stdcall lin_FT_GetDeviceInfoDetail(long ptr ptr ptr ptr ptr ptr ptr) FT_GetDeviceInfoDetail
73 stub lin_FT_SetDeadmanTimeout
74 stdcall lin_FT_GetDriverVersion(long ptr)                   FT_GetDriverVersion
75 stdcall lin_FT_GetLibraryVersion(ptr)                       FT_GetLibraryVersion
76 stub lin_FT_W32_GetCommMask
77 stub lin_FT_Rescan
78 stub lin_FT_Reload
79 stub lin_FT_GetComPortNumber
80 stub lin_FT_EE_ReadConfig
81 stub lin_FT_EE_WriteConfig
82 stub lin_FT_EE_ReadECC
83 stub lin_FT_GetQueueStatusEx
84 stub lin_FT_EEPROM_Read
85 stub lin_FT_EEPROM_Program
86 stub lin_FT_ComPortIdle
87 stub lin_FT_ComPortCancelIdel
