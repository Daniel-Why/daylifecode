#!bin/bash

for i in {0..9}
do
    for j in {0..9}
    do
        for k in {0..9}
        do
            for l in {0..9}
            do
                echo $(cat /etc/bandit_pass/bandit24) $i$j$k$n >> test.txt
            done
        done
    done
done