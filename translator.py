from os import access
import sys
import re
class File_worker:
    def __init__(self, direction, type = 'r'):
        self.file_descriptor = open(direction, type)
        self.access_type = type
    
    def change_file(self, directory, new_type = 'r'):
        self.file_descriptor.close()
        self.file_descriptor = open(directory, new_type)
        self.access_type = new_type
    
    def read(self, type = "r", count = -1): #type = r - element read, sr - string read, fr - full read, cr - char read
        if self.access_type.find('w') != -1:
            print("Unavaible function! Please change access_type")
            return ""
        elif type == "fr":
            if count == -1:
                print("Non-optional variant! Please delete count or size")
            return self.file_descriptor.read()
        elif type == "sr":
            if count == -1:
                return self.readlines()
            elif count > 0:
                return self.file_descriptor.readline()*count
        elif type == "cr":
            if count == -1:
                return self.file_descriptor.read().split("")
            elif count > 0:
                return self.file_descriptor.read(count).split("")
        elif type == "r":
            if count == -1:
                return self.file_descriptor.read()
            elif count > 0:
                return self.file_descriptor.read(count)
        
    def write(self, source, count = -1): # w - write element, 
        if self.access_type.find('r') != -1:
            print("Unavaible function! Please change access_type")
            return -1
        elif source != "":
            return self.file_descriptor.write(source)
    
    def __del__(self):
        self.file_descriptor.close()
    pass

    

aaa = 3


def main():
    file_parametr = sys.argv[2].split('.')
    additional_file = file_parametr[0] + '.'
    additional_hpp_file = additional_file + "hpp"
    additional_cpp_file = additional_file + "cpp"
    program_name = file_parametr[0] + '.' + file_parametr[1]
    input_file = File_worker(program_name)
    if sys.argv[3] == "-n":
        if len(sys.argv) > 4:
            additional_hpp_file = sys.argv[4]
        if len(sys.argv) > 5:
            additional_cpp_file = sys.argv[5]
    output_interface_program = File_worker(additional_hpp_file)
    output_base_program = File_worker(additional_cpp_file)
    text = input_file.read(type = "sr")
    
    Base_construction = ""
    for line in text:
        if line[0] == "#": #preprocessor gain
            return 1
            
        
             
            
if __name__ == "__main__":
    main()