import os
import sys

def produce_train_data(input_file, output_file):
    '''
    Args:
        input_file: user behavior file
        output_file: output file
    '''

    if not os.path.exists(input_file):
        return
    linenum=0
    f = open(input_file)
    score_threshold = 4.0
    record = {}
    for line in f:
        if linenum==0:
            linenum+=1
            continue
        item = line.strip().split(',')
        if len(item)<4:
            continue
        userid, itemid, rating = item[0], item[1], float(item[2])
        if rating<score_threshold:
            continue
        if userid not in record:
            record[userid] = []
        record[userid].append(itemid)
    f.close()

    fw = open(output_file,'w+')
    for userid in record:
        fw.write(' '.join(record[userid]) + '\n')
    fw.close()



if __name__=='__main__':
    if len(sys.argv) < 3:
        print('usage: python xx.py inputfile outputfile')
        sys.exit()
    else:
        inputfile = sys.argv[1]
        outputfile = sys.argv[2]
        produce_train_data(inputfile,outputfile)
    #produce_train_data('../data/ratings.csv','../data/train_data.txt')

