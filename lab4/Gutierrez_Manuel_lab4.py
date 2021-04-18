'''
Name: Manuel Gutierrez
Class: CS2403
Proffessor: Dr.Fuentes
TA: Nath, Anindita
Last modofied November 6 2020
'''

import bs4 as bs
import urllib.request
import hash_table_chain as htc

# You will need to install urllib and BeautifulSoup4
lowercase = ''.join(chr(i) for i in range(97,123)) + ' '

def createHashTable(word_lists):
    H=htc.HashTableChain(len(word_lists))
    for i in range(len(word_lists)):
        for j in word_lists[i]:
            lis = H.retrieve(j)
            if lis == None:
                H.insert(j,[i])
            else:
                #checks for duplicates in a single sentence 
                if i != (H.retrieve(j))[len(H.retrieve(j))-1]:
                    lis += [i]
                    H.update(j,lis)
    return H

def find_index(H,word):
    bucket = H.retrieve(word)
    return bucket

def getSentence(bucket,sentece_list):
    for i in range(10):
        #checks just in case if the word does not appear it will break out of the loop 
        if(i > len(bucket)):
            break
        print(sentence_list[bucket[i]])
        print()
        
def get_words(st):
    st = st.lower()
    st = st.replace('\r\n', ' ')
    st = ''.join( c for c in st if  c in lowercase)
    words = st.split()
    return words

def continue_process(H):
    res = 'y'
    while res == 'y':
        word = input('Enter a word to Search: ')
        bucket = find_index(H,word)
        
        print('The word '+word+' appears in '+ str(len(bucket))+' sentences in '+bn[int(selection)-1])
        print('The word '+word+' the word appeard in the Folloing sentence:')
        
        getSentence(bucket,sentence_list)
        res =input('Do you wish to continue y/n?')

if __name__ == "__main__":
    res = 'y'
    bn = ['The Call of the Wild','Dracula','The Adventure of Sherlok Holmes']
    url_list = ['http://www.gutenberg.org/files/215/215-h/215-h.htm', 'http://www.gutenberg.org/files/345/345-h/345-h.htm', 'http://www.gutenberg.org/files/1661/1661-h/1661-h.htm']
    print("Choose among the following books:")
    print('1) The Call of the Wild')
    print('2) Dracula')
    print('3) The Adventure of Sherlok Holmes')
    selection = input("selection: ")
    
    #funtes code
    url = url_list[int(selection)-1]
    word_lists = []
    sentence_list = []
    data = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(data,'lxml')
    count = 0
    for paragraph in soup.find_all('p'):
        par  = paragraph.string
        if par:
            par = par.replace('\r\n', ' ')
            sent = par.split('.')
            for s in sent:
                sentence_list.append(s+'.')         
                words = get_words(s)
                word_lists.append(words)
    H = createHashTable(word_lists)
    continue_process(H)
    
    '''
    # print('This is the first sentence:')
    # print(sentence_list[0])
    # print('This is the first word list:')
    # print(word_lists[0])
    '''
