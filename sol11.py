    # TODO: Find a string

def count_substring(string, sub):
    count = 0
    for i in range(0, len(string) - len(sub) + 1):
        comp = string[i:i+len(sub)]
        if(sub == comp):
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)