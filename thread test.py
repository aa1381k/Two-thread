#user input word program
#two thread
import threading

def user_input():
    while True:
        user_input_word=input()
        if user_input_word=="a":
            print("this is a")
        if user_input_word=="b":
            print("this is b")
        if user_input_word=="q":
            break 

def main ():
    print("start of program")
    thread = threading.Thread(target=user_input)
    thread.start()
    thread.join()
    print("end of program")

if __name__=='__main__':
    main()