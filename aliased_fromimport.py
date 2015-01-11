from time import localtime as lt 
 
def main():
    current_time = lt()
    print 'year :', current_time[0]
    print 'month :', current_time[1]
    print 'date :', current_time[2]

if __name__ == '__main__':
    main() 