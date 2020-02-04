buff_size = 5
buff = [0] * buff_size
READ_INDEX = 0
WRITE_INDEX = 0
EMPTY = True

def write_buffer(value):
    global WRITE_INDEX, READ_INDEX, EMPTY
    buff[WRITE_INDEX] = value
    if READ_INDEX == WRITE_INDEX and not EMPTY:
        READ_INDEX = move_forward(READ_INDEX)
    WRITE_INDEX = move_forward(WRITE_INDEX)
    EMPTY = False
        
def read_buffer():
    global READ_INDEX, WRITE_INDEX, EMPTY
    if not EMPTY:
        print(buff[READ_INDEX])
        READ_INDEX = move_forward(READ_INDEX)
    if READ_INDEX == WRITE_INDEX: EMPTY = True

def move_forward(index):
    global EMPTY
    return (index+1)%buff_size
    
if __name__ == "__main__":
    print(buff)
    write_buffer(1)
    write_buffer(2)
    write_buffer(3)
    write_buffer(4)
    write_buffer(5)
    write_buffer(6)
    write_buffer(7)
    write_buffer(8)
    write_buffer(9)
    write_buffer(10)
    write_buffer(11)
    print(buff)
    read_buffer()
    read_buffer()
    read_buffer()
    read_buffer()
    read_buffer()
    read_buffer()
    read_buffer()
    read_buffer()
    print("WRITE INDEX :  " + str(WRITE_INDEX))
    print("READ INDEX : " + str(READ_INDEX))
