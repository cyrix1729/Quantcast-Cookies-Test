#sys used for reading arguments passed in (file name, date)
import sys

def getFileName(): #returns array of cookies that match given date
    try:#Matching file name found
        file_name = sys.argv[1]
        return file_name
    except: #no matching file found
        print('File not found.')
        sys.exit()
    
def getLines(file_name):
    with open(file_name, 'r') as file: 
            lines = file.readlines() 
    return lines

def getCookies(lines):
    
    matching_cookies = [] #array of cookies matching specified date
    date = sys.argv[len(sys.argv)-1] #date given in command line
    for i in range(1, len(lines)): #start at 1 to skip 'cookies, timestamp' line
        if checkDate(lines[i], date): #only run for lines that match date
            char = 0 
            cookie = '' 
            
            while lines[i][char] != ',': #',' -> end of cookie
                cookie+= lines[i][char] 
                char +=1
            matching_cookies.append(cookie)
            
        else: continue
    return matching_cookies
    

def checkDate(line,date): #returns boolean whether date of given line matches date given in command line 
    line_date = '' #date of the line passed in
    in_date = False #if inside date part of line (between ',' and 'T')
    for char in line:
        if char==',': 
            in_date = True
            continue
        if in_date:
            if char == 'T': #where date finishes and time starts
                break
            line_date+=char
    return True if line_date == date else False
    

def mostActive(cookies):
#Get value of max occurrences of any cookie
    ht = {}#hash table to store {cookie: frequency}
    max_freq = 0
    for ck in cookies:
        if ck in ht:
            ht[ck]+=1
        else:
            ht[ck] = 1
            
        if ht[ck] > max_freq: 
            max_freq = ht[ck]
#checks which elements in hash table store max_freq value
    most_active = set()#set to store most frequent cookies with no duplicates 
    for ck in cookies:
        if ht[ck] == max_freq:
            most_active.add(ck)
    return most_active

def printSet(most_active):
    for ck in most_active:
        print(ck)
    
def main():
    file_name = getFileName()
    file_lines = getLines(file_name)
    if len(file_lines) < 2: #One line needed for header in csv file
        print(file_name + ' contains no Tuples (data).')
        sys.exit()
    cookies = getCookies(file_lines) #returns all cookies from date given and stores in an array
    most_active = mostActive(cookies) #prints most active cookie from array of cookies given
    printSet(most_active) #prints sets line by line


if __name__ == '__main__':
    main()