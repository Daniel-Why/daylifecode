#!/bin/bash
echo start >b
while true
do
echo >>b
date >>b
echo >>b
ping 192.168.99.1 -c 4 >>b
echo >>b
ping 8.8.8.8 -c 4 >> b
echo >>b
ping www.webfx.com -c 4 >>b
echo >>b
echo >>b	
echo '########################' >>b
a=$[RANDOM%110+210]
printf $a
sleep $a
echo -done!
done
