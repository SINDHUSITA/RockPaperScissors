# Rock Paper Scissors
A simple game which a user plays with computer. There are both console application and GUI(Tkinter) versions for this game.

How it works:
1. User throws his choice (among Rock, Paper, Scissors)
2. The computer program throws a counter to the user randomly.
3. These are taken as input and point is added to the player accorinding to priority.

Game Rules:

-> Rock beats Scissors

-> Scissors beats Paper

-> Paper beats Rock

Same choice is a draw.

Game Modes:

Mode 1: Unlimited

Here, players keep playing and scores are accordingly added. When the user decides to stop, The one with higher score is declared a winner.

Mode 2: Limited

Here, User can choose the number of rounds(preferebly odd) he wants to play. For example, If the user chooses 5 rounds, the first one to reach 3 points wins.(Best of few type)

Future Scope: Currently this GUI project is just an initial step for the actual future project. I am looking forward to building a computer vision model that works by Hand Gesture Recognition.



match_types = {'int64':'int', 'float64':'FLOAT','object':'varchar(100)','datetime64[ns]':'varchar(20)'}
data = pd.read_excel('sample2.xls')
types = [str(i) for i in data.dtypes]
names_c = [str(i).replace(' ', '_') for i in data.columns]
names = [str(i) for i in data.columns]

create_query = 'create table sampleTable2 ('
for i in range(len(names)):
    create_query += names_c[i] + ' ' + match_types[types[i]] + ','
create_query = create_query[:-1]
create_query += ');'
print(create_query)
cursor.execute(create_query)
connection.commit()

data.fillna('NULL', inplace=True)
for i in range(len(names)):
    if(types[i]=='object'):
        data[names[i]] = data[names[i]].str.replace("'","''")
        data[names[i]] = data[names[i]].apply(lambda x: "'"+x+"'")
for i in range(len(names)):
    if(types[i] not in ['object','int64','float64']):
        data[names[i]] = data[names[i]].apply(lambda x: "'"+str(x)+"'")
print('total rows: ', data.shape[0])

fc = []
for i in range(data.shape[0]):
    insert_query = 'insert into sampleTable2 values('
    for j in data.values[i]:
        insert_query += str(j) + ','
    insert_query = insert_query[:-1]
    insert_query += ');'
    try:
        cursor.execute(insert_query)
        connection.commit()
    except:
        fc.append(insert_query)
print('number of failed queries  :',len(fc))
