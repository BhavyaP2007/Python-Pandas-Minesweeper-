import pandas as pd
import numpy as np

#this code generates a random minesweeper grid

x=int(input("Enter the number of rows: "))
y=int(input("Enter the number of columns: "))
x_cords = list(range(x))
y_cords = list(range(y))
df = pd.MultiIndex.from_product([range(x), range(y)])
df = pd.Series(index=df).reset_index().drop([0],axis=1)
df.rename(columns={"level_0":"x","level_1":"y"},inplace=True)
df['mine'] = np.random.choice([0,0,0,0,0,0,1,1,1,1],size=(x*y))
print(df.loc[(df["x"]==0) & (df["y"]==0)]["mine"].to_list()[0])
for x in range(len(x_cords)):
    for y in range(len(y_cords)):
        adjacant_mines = 0
        if x+1 in x_cords and y-1 in y_cords:
            if df.loc[(df["x"]==x+1) & (df["y"]==y-1)]["mine"].tolist()[0]==1:
                adjacant_mines+=1
        if x-1 in x_cords and y-1 in y_cords:
            if df.loc[(df["x"]==x-1) & (df["y"]==y-1)]["mine"].tolist()[0]==1:
                adjacant_mines+=1
        if x+1 in x_cords and y in y_cords:
            if df.loc[(df["x"]==x+1) & (df["y"]==y)]["mine"].tolist()[0]==1:
                adjacant_mines+=1
        if x-1 in x_cords and y in y_cords:
            if df.loc[(df["x"]==x-1) & (df["y"]==y)]["mine"].tolist()[0]==1:
                adjacant_mines+=1
        if x in x_cords and y+1 in y_cords:
            if df.loc[(df["x"]==x) & (df["y"]==y+1)]["mine"].tolist()[0]==1:
                adjacant_mines+=1
        if x in x_cords and y-1 in y_cords:
            if df.loc[(df["x"]==x) & (df["y"]==y-1)]["mine"].tolist()[0]==1:
                adjacant_mines+=1
        if x+1 in x_cords and y+1 in y_cords:
            if df.loc[(df["x"]==x+1) & (df["y"]==y+1)]["mine"].tolist()[0]==1:
                adjacant_mines+=1
        if x-1 in x_cords and y+1 in y_cords:
            if df.loc[(df["x"]==x-1) & (df["y"]==y+1)]["mine"].tolist()[0]==1:
                adjacant_mines+=1  
        df.loc[(df["x"]==x) & (df["y"]==y),"adjacant"]=adjacant_mines
df.loc[df["mine"]==1,"adjacant"]="Mine"      
grid = df.pivot(index="x",columns="y",values="adjacant")
print(grid)        