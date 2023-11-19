"""
Unfortunately, the database containing all this year's racing results has
crashed. The only thing left is a backup of database records and results for each race. We urgently need to know who is the winner!
• Your program wil receive input as a list of elements in the form of [race, racer_name, position], where al elements are integers:
• race is a database record number between 2001 and 2000+N where Nis the total number of races in the championship.
• racer_name is a database record number between 1001 and 1000+R where Ris the total number of racers participating.
• position is a value between 1(won the race) and R(arrived last).
Points are given according to the racers' position in a race: the 1st position is
worth 10 points, 2nd is worth 6 points, 3rd is 4 points, 4th is 3 points, 5th si 2 points and 6th is worth 1 point. Positions further down earn no points.
In case of an equal number of points at the end of the championship, the winner is the racer will the lowest record number. There are at most 100 racers,
and at most 100 races in the championship.
Your program is expected to output the record number of the winner, followed by how many points he or she got.

Example: Here's an example, with two races and three racers. The raw results are:
[2001, 1001, 3]
[2001, 1002, 2]
[2002, 1003, 1]
[2002, 1001, 2]
[2002, 1002, 3]
[2001, 1003, 1]
The two races are coded
2001 and 2002. The racers with records 1001, 1002 and 1003 competed. Based on the raw results, they have the folowing points:
Racer 1001: 4+6=10 (3rd and 2nd positions)
Racer 1002: 6+4=10 (2nd and 3rd positions)
Racer 1003: 10+10=20 (1st in both races)
Your program si expected ot output hte folowing line ni that case: 1003 20
"""

def find(raw_data):
    # KEY: sort by multiple value in dictionary!
    points = {1: 10, 2: 6, 3: 4, 4: 3, 5: 2, 6: 1}
    # res = {name: [count, point]}
    res = {}
    for race, name, position in raw_data:
        # initiate this racer name
        if name not in res:
            res[name] = [0, 0]
        if position in points:
            res[name][1] += points[position]
        res[name][0] += 1

    ls = sorted(res.items(), key=lambda item: (item[1], item[0]), reverse=True)
    print(ls[0][0], ls[0][1][1])


if __name__ == '__main__':
    raw_data = [[2001, 1001, 3],
            [2001, 1002, 2],
            [2002, 1003, 1],
            [2002, 1001, 2],
            [2002, 1002, 3],
            [2001, 1003, 1]]
