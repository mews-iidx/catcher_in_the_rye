# coding: utf-8
import random

#TODO fix csv to df
#import pandas as pd

#df = pd.read_csv("data/test_data.csv")
#
#names = df["Unnamed: 1"]
#story = df["Unnamed: 9"]
#df2 = pd.DataFrame(names, story)
#
#df2

def csv2dict(csv_file="data/test_data.csv", ignore_header=True):
    with open(csv_file, "r") as f:
        lines = f.readlines()

    member_dict = {}
    for i, l in enumerate(lines):
        if ignore_header and i == 0:
            continue

        sp = l.split(",")
        name = sp[0]
        cat1 = sp[2]
        member_dict[name] = cat1

    return member_dict

def get_teams(members, num=4):
    # members = random.shuffle(members)
    random.shuffle(members)
    d = len(members) // num
    s = len(members) % num

    team_map = [chr(i) for i in range(65, 65 + 26)]
    teams= {}

    tmp = []
    for i, member in enumerate(members):
        team_index = i // num
        team = team_map[team_index]
        members[i]
        tmp.append(member)

        if (i % num) == num - 1:
            teams[team] = tmp
            tmp = []

    teams[team] = tmp
    for t in teams:
        if not len(teams[t]) == num:
            for i, tt in enumerate(teams[t]):
                teams[team_map[i]].append(tt)
    del teams[t]
    return teams



if __name__ == "__main__":
    d = csv2dict()
    members = list(d.keys())
    teams = get_teams(members, 4)


    for key in teams:
        print(key, teams[key])
        print("")
