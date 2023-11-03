from radon.visitors import ComplexityVisitor
from radon.visitors import HalsteadVisitor
from radon.raw import analyze
import csv
import os

csvfile = open('humanCodeMetrics.csv', 'w')
header = [
    'File',
    'Category',
    'Subcategory',
    'More Accurate/Less Accurate',
    'Cyclomatic Complexity',
    'SLoC',
    'Halstead Distinct Operators',
    'Halstead Distinct Operands',
    'Comments',
#    'Notes'
]
writer = csv.DictWriter(csvfile, fieldnames=header)
writer.writeheader()
# writer.writerow({'File': 'arst', 'Category': 'arst', ...})

scripts = open('./3.5turbo/scriptsToRun.txt', 'r')
for script in scripts:
    row = {}
    parts = script.split()
    fileParts = parts[0].split('/')
    row['File'] = fileParts[3]
    row['Category'] = fileParts[1]
    row['Subcategory'] = fileParts[2]
    row['More Accurate/Less Accurate'] = 'more' if (parts[2] == 'check') else 'less'
#    row['Notes'] = ' '.join(parts[4:])

    if (not os.path.exists(
        '/home/madram/School/Research/GPT-Competency/humanCode/'
        + '/'.join(fileParts[1:])
    )):
        continue

    codeFile = open(
        '/home/madram/School/Research/GPT-Competency/humanCode/'
        + '/'.join(fileParts[1:]), 'r'
    )
    code = codeFile.read()
    complex = ComplexityVisitor.from_code(code)
    row['Cyclomatic Complexity'] = complex.total_complexity
    analysis = analyze(code)
    row['SLoC'] = analysis.sloc
    row['Comments'] = analysis.comments

    hal = HalsteadVisitor.from_code(code)
    row['Halstead Distinct Operators'] = hal.distinct_operators
    row['Halstead Distinct Operands'] = hal.distinct_operands

    writer.writerow(row)

scripts.close()
csvfile.close()
