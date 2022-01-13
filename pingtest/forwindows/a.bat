@echo on >a.log
:begin
echo %date% %time% >>a.log

ping 192.168.99.1 >> a.log

ping 8.8.8.8 >>a.log

ping www.youtube.com >>a.log

set /a t=%random%%%100+250

TIMEOUT /T %t%

echo waiting.......

echo ---------- >>a.log


goto begin