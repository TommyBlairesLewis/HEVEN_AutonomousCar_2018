from multiprocessing import Process

def GO():
    print('Hi\n')
    
def GO2():
    GO()
if __name__=='__main__':
    pr1 = Process(target=GO)
    pr2 = Process(target=GO2)
    pr1.start()
    pr2.start()
    pr1.join()
    pr2.join()