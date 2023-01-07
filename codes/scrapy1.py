import json
import pandas as pd
with open('1.json') as f:
    jd=json.load(f)

#0
postions=[]
team_names=[]
playeds=[]
wins=[]
losts=[]
tieds=[]
points=[]
score_diffs=[]

for i in range(0,6):
    postion=jd["standings"]["groups"][0]['teams']['team'][i]['position']
    team_name=jd["standings"]["groups"][0]['teams']['team'][i]['team_name']
    played=jd["standings"]["groups"][0]['teams']['team'][i]['played']
    win=jd["standings"]["groups"][0]['teams']['team'][i]['wins']
    lost=jd["standings"]["groups"][0]['teams']['team'][i]['lost']
    tied=jd["standings"]["groups"][0]['teams']['team'][i]['tied']
    score_diff=jd["standings"]["groups"][0]['teams']['team'][i]["score_diff"]
    point=jd["standings"]["groups"][0]['teams']['team'][i]['points']

    postions.append(postion)
    team_names.append(team_name)
    playeds.append(played)
    wins.append(win)
    losts.append(lost)
    tieds.append(tied)
    points.append(point)
    score_diffs.append(score_diff)



season7={
   'rank':postions,
    'Team_Names':team_names,
    'Matches_Played':playeds,
    'Wins':wins,
    'Losses':losts,
    'Ties':tieds,
    'Score_Diff':score_diffs,
    'Points':points}

#1
postions1=[]
team_names1=[]
playeds1=[]
wins1=[]
losts1=[]
tieds1=[]
points1=[]
score_diffs1=[]

for i in range(0,6):
    postion=jd["standings"]["groups"][1]['teams']['team'][i]['position']
    team_name=jd["standings"]["groups"][1]['teams']['team'][i]['team_name']
    played=jd["standings"]["groups"][1]['teams']['team'][i]['played']
    win=jd["standings"]["groups"][1]['teams']['team'][i]['wins']
    lost=jd["standings"]["groups"][1]['teams']['team'][i]['lost']
    tied=jd["standings"]["groups"][1]['teams']['team'][i]['tied']
    score_diff=jd["standings"]["groups"][1]['teams']['team'][i]["score_diff"]
    point=jd["standings"]["groups"][1]['teams']['team'][i]['points']

    postions1.append(postion)
    team_names1.append(team_name)
    playeds1.append(played)
    wins1.append(win)
    losts1.append(lost)
    tieds1.append(tied)
    points1.append(point)
    score_diffs1.append(score_diff)



season71={
   'rank':postions1,
    'Team_Names':team_names1,
    'Matches_Played':playeds1,
    'Wins':wins,
    'Losses':losts1,
    'Ties':tieds1,
    'Score_Diff':score_diffs1,
    'Points':points1}

season7_df=pd.DataFrame(season7)
season71_df=pd.DataFrame(season71)
print(season7_df)
print(season71_df)
final_df=pd.concat([season7_df,season71_df],axis=0)
final_df.to_csv('Season5.csv',index=False)

