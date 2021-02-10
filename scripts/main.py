from datetime import datetime
import sys

print("PRINT FROM PYTHON: ACTION 1.2 - STARTED")

first_arg = sys.argv[1]
second_arg = sys.argv[2]

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('log.md', 'w') as f:
    f.write(f'# {timestamp}')
    f.write("\n1st arg: {}\n".format(first_arg))
    f.write("2nd arg: {}\n".format(second_arg))
    
print("PRINT FROM PYTHON: ACTION 1.2 - COMPLETED")
