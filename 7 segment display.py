#7 segment display

dis=[1111110,#0
     0110000,#1
     1101101,#2
     1111001,#3
     0110011,#4
     1011011,#5
     1011111,#6
     1110000,#7
     1111111,#8
     1111011,#9
     ]
def print_num(num):
    global digits
    digs=str(num)
    lines={'' for lin in range(5)}
    for d in digs:
        seg=[['','',''] for lin in range(5)]
        ptrn=dis[ord(d)-ord('0')]
        if ptrn[0]==1:
            seg[0][0]=seg[0][1]=seg[0][2]='#'
        if ptrn[1]==1:
            seg[0][2]=seg[1][2]=seg[2][2]='#'
        if ptrn[2]==1:
            seg[2][2]=seg[3][2]=seg[4][2]='#'
        if ptrn[3]==1:
            seg[4][0]=seg[4][1]=seg[4][2]='#'
        if ptrn[4]==1:
            seg[2][0]=seg[3][0]=seg[4][0]='#'
        if ptrn[5]==1:
            seg[0][0]=seg[1][0]=seg[2][0]='#'
        if ptrn[6]==1:
            seg[2][0]=seg[2][1]=seg[2][2]='#'
        for lin in range(5):
            lines[lin]+=''.join(seg[lin])
        lin in lines:
        print(lin)
print_num(int(input("Enter number:"))
