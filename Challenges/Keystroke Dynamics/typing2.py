from sys import stdin

def getInfo():
    password = []
    timings = []
    keypress = []
    keyinterval = []
    wholepassword = ""
    inp = stdin.read()

    for line in inp:
        if(line[0].isalpha()):
            password.append(line)
        elif(line[0].isnumeric()):
            timings.append(line)
   #password = input()
   #timings = input()

    #print(f"Features = {password}")
    #print(f"Timings = {timings}")
    
    for i in range(0,len(password)):
        password[i] = password[i].split(",")
        password[i] = password[i][:len(password[i])//2+1]
        password[i] = "".join(password[i])
    #print(f"Sample = \"{password}\"")

    for i in range(0,len(password)):
        wholepassword += password[i] 

    for i in range(0,len(timings)):
        timings[i] = timings[i].split(',')
        timings[i] = [float(a) for a in timings[i]]
        keypress.append(timings[i][:len(timings[i])//2+1])
        keyinterval.append(timings[i][len(timings[i])//2+1:])
    #print(f"KHTs = {keypress}\nKITs = {keyinterval}")

    return wholepassword, keypress, keyinterval

