row1 = ['0','0','0']
row2 = ['0','0','0']
row3 = ['0','0','0']

map = [row1,row2,row3]

print(f'{row1}\n{row2}\n{row3}')

position=input('where should we put the treasure? 2 digits: ')
#first [ are rows] secon [are columns]
rowFromTop =int(position[0])-1
ColumnFromLeft = int(position[1])-1
map[rowFromTop][ColumnFromLeft] = 'X'

print(f'{row1}\n{row2}\n{row3}')
2