#!/usr/local/bin/python3

class Research:
    def file_reader(self):
        with open('data.csv', 'r') as file:
            return(file.read())

def main():
    research = Research()
    print(research.file_reader())

if __name__ == '__main__':
    main()
