import json
import pandas as pd
with open('1.json') as f:
    jd=json.load(f)
postions=[]
team_names=[]
playeds=[]
wins=[]
losts=[]
tieds=[]
points=[]
score_diffs=[]

for i in range(0,8):
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

season7_df=pd.DataFrame(season7)
print(season7_df)
season7_df.to_csv('Season1.csv',index=False)