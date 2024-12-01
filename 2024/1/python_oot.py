import os

class AOCExceptions(Exception):
    pass

class NoNewLineError(AOCExceptions):
    def __init__(self, message="", error=None) -> None:
        super().__init__(message)
        self.message=message
    def __str__(self):
        return "No new line at end of file!"
    
class InvalidLineError(AOCExceptions):
    def __init__(self, message="", line=None) -> None:
        if line is None:
            line = "(No Line Given)"
        super().__init__(message)
        self.message=message
        self.line = line
    def __str__(self):
        return f"Sequence \"   \" not found in line {self.line}!"

class InvalidInputError(AOCExceptions):
    def __init__(self, message="", input=None) -> None:
        if input is None:
            input = "(No Input Given)"
        super().__init__(message)
        self.message=message
        self.input = input
    def __str__(self):
        return f"Input {self.input} is invalid!"


class FileExctractor:
    HERE = os.path.dirname(__file__)
    def __init__(self, filename, path = HERE) -> None:
        self.input_file = os.path.join(self.HERE, filename)
        self.path_to_data()
        self.lines_sanitizer()

    def path_to_data(self):
        with open(self.input_file) as my_file:
            self.input_data = my_file.read()
            self.input_lines = self.input_data.split("\n")
    
    def lines_sanitizer(self):
        empty_newline = self.input_lines.pop()
        if empty_newline != "":
            raise NoNewLineError()
        print(self.input_lines)

class Solver:

    def __init__(self, filename, path=None) -> None:
        self.lines = self.extract_lines(filename, path)
    
    def extract_lines(self, filename, path):
        if path:
            extractor_object = FileExctractor(filename=filename, path=path)
        else:
            extractor_object = FileExctractor(filename=filename)
        return extractor_object.input_lines
    
    def solve(self):
        self.generate_lists()
    
    def validate_gap(self, line:str):
        if "   " not in line:
            raise InvalidLineError(line=line)
        
    def line_splitter(self,line:str, separator:str):
        return line.split(separator)
    
    def validate_integer_string(self, integer_string:str):
        import re
        if not re.match("^\d+$", integer_string):
            raise InvalidInputError(input=integer_string)


    def convert_to_int(self, entry:str)-> int:
        self.validate_integer_string(entry)
        return int(entry)

    def integer_distance(self, entry_one:int, entry_two:int):
        return abs(entry_one - entry_two)

    def generate_lists(self):
        left_list = AOCIntList()
        right_list = AOCIntList()
        for line in self.lines:
            self.validate_gap(line)
            left, right = self.line_splitter(line=line, separator="   ")
            left_int = self.convert_to_int(left)
            right_int = self.convert_to_int(right)
            left_list.append(left_int)
            right_list.append(right_int)
        self.left = left_list
        self.right = right_list
        length = len(self.left)
        self.accumulator = 0
        for _ in range(length):
            left_minimum = self.left.pop_minimum()
            right_minimum = self.right.pop_minimum()
            current_distance = self.integer_distance(left_minimum, right_minimum)
            self.accumulator += current_distance
    
    def result(self):
        if hasattr(self, "accumulator"):
            print(f"The result is {self.accumulator}")
        
        


class AOCIntList(list):
    
    def __init__(self):
        self.validate_list()

    def validate_list(self):
        length = len(self)
        valid = True
        for index in range(length):
            valid = valid and (type(self[index])==int)
        return valid


    def pop_minimum(self):
        if len(self) >= 1:
            if self.validate_list():
                minimum = min(self)
                index = self.index(minimum)
                min_ejected = self.pop(index)
                return min_ejected


    


if __name__ == "__main__":
    solver_object = Solver("input.txt")
    solver_object.solve()
    solver_object.result()