@echo off

REM check params
IF "%~1"=="" (
echo please in put params!
exit /b
 )

REM check first param
IF /I "%~1"=="-n" (
REM output time
set ENV_Path=%E%
echo %time% ENV is: %E%
) ELSE IF /I "%~1"=="-m" (
REM check second param
IF "%~2"=="" (
echo please input data！
exit /b
)

REM count length
setlocal enabledelayedexpansion
set "data=%~2"
set count=1
:loop
if not "!data:~%count%,1!" == "" (
set /a count+=1
goto loop
)

echo the length is: %count%
:end
exit /b
) ELSE (
echo unknow param:%~1
)

exit /b