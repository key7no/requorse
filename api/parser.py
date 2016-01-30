from ast import literal_eval

class Course:
    def __init__(self, subject="", number="", title="", units="", prereqs="", concurrent="", coreqs=""):
        self.subject = subject
        self.number = number
        self.title = title
        self.units = units
        self.prereqs = prereqs
        self.concurrent = concurrent
        self.coreqs = coreqs
        pass

class CourseTuple:
    def __init__(self, num="", courses = [], coursetuples = []):
        self.num = num
        self.courses = courses
        self.coursetuples = coursetuples
        
courselist = []
tuplelist = []

def parse(file):
    # Open file and read first line
    f = open(file, 'r')
    line = f.readline()
    while line:
            
        # If line is commented out, ignore it
        if line[0] == '#':
            line = f.readline()
            continue

        # Create new Course object
        x = Course()
        x.subject = line.split(';')[0]
        x.number = line.split(';')[1]      
        x.title = line.split(';')[2]
        x.units = line.split(';')[3]
        x.prereqs = line.split(';')[4]
        x.concurrent = line.split(';')[5]
        x.coreqs = line.split(';')[6]

    for i in courselist:
        i.prereqs = parseTuple(i.prereqs)
        i.concurrent = parseTuple(i.concurrent)
        i.coreqs = parseTuple(i.coreqs)

def parseTuple(tup):
    assert type(tup) == tuple
    x = CourseTuple()
    assert type(tup[0]) == int
    x.num = tup[0]
    assert type(tup[1]) == list
    x.courses = tup[1]
    assert type(tup[2]) == list
    y = []
    for item in tup[2]:
        y.append(parseTuple(item))
    x.coursetuples = y
    tuplelist.append(x)
    return x
    
