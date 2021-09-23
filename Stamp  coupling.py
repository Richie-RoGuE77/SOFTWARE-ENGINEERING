def process1(info):
    if(info['Total marks'] > 400):
        process2(info)
    else:
        print("Fail")

def process2(info):
    percentage = (info['Total marks'] / 600) * 100
    print(f'The student got {format(percentage)} %')

info = {'Name' : 'Arjun',
            'age': 20,
            'Year': 2,
            'Branch' : 'CSE',
            'Total marks': 564
        }
process1(info)
""" Here we are passing the entire data in the dictionary 
                 to the functions process1 and process2, where only the TOTAL MARKS 
                 key-value pair is used.This can be avoided by passing only the required 
                 parameters ito the functions.."""
process1(info['total marks'])
