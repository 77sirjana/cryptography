alpha =" ABCDEFGHIJKLMNOPQRSTUVWXYZ "
print (" Lenght of alpha : {}". format (len( alpha ) ) )

# input a word and it will change to uppercase
str_in = input (" Enter a word , like HELLO :") . upper ()

 # input a number in integer
shift = int( input (" Input Shift value , like 3: ") )
n = len( str_in )
msg_cipher = " "

for i in range ( n ) :
    c = str_in [ i ]
    loc = alpha . find ( c )
    print ( i , c , loc ) # used to see intermediate result , can be omitted
    newloc = ( loc + shift ) % 26
    msg_cipher += alpha [ newloc ]

print (" Plain text : ", str_in )
print (" Shift Value : ", shift )
print (" Cipher text : ", msg_cipher )
