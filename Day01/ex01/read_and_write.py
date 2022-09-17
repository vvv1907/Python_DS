#!/usr/local/bin/python3

def read_and_write(filename):
    
    input_file = open(filename+'.csv', 'r')
    output_file = open(filename+'.tsv', 'w')
    
    output_file.write(input_file.read()
    	.replace('\",\"', '\"\t\"')
        .replace(',false', '\tfalse\t')
        .replace(',\"', '\"')
        .replace(',true', '\ttrue\t'))
    
    input_file.close()
    output_file.close()

if __name__ == '__main__':
    read_and_write('ds')
