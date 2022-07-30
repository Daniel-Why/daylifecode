digit_file = open("pwd.txt","w")

for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                four_digit = "{}{}{}{}".format(str(i),str(j),str(k),str(l))
                pwd = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"+four_digit+"\n"
                digit_file.write(pwd)
digit_file.close()


