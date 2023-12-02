task2=open("task2.txt","r")
wordsToRemove=[" ","Game"]
list_of_sequences=[]
listForID=[]
score=0
impossible_score=False
for line in task2:
  for i in wordsToRemove:
    line=line.replace(i,"")
    #removes unnecessary spaces and detail from the line
  listForID=line.split(":")
  #filters ID from rest of line
  list_of_sequences=listForID[1].split(";")
  #filters separate lists of scores
  for sequence in list_of_sequences:
    scores=sequence.split(",")
    #finds individual scores by further filtering
    for sepScores in scores:
      if sepScores.find("green")!=-1 :
        if int(sepScores[:sepScores.find("green")])>13:
          impossible_score=True
          break
      elif sepScores.find("red")!=-1 :
        if int(sepScores[:sepScores.find("red")])>12:
          impossible_score=True
          break
      elif sepScores.find("blue")!=-1:
        if int(sepScores[:sepScores.find("blue")])>14:
          impossible_score=True
          break
  if impossible_score==False:
    score+=int(listForID[0])
  scores.clear() 
  listForID.clear()
  list_of_sequences.clear() 
  impossible_score=False
  #clears lists and resets the boolean value, ready for next iteration
print(score)


    
