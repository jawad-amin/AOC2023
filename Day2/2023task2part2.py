task2=open("task2.txt","r")
wordsToRemove=[" ","Game"]
list_of_sequences=[]
listForID=[]
score=0
blue=[]
green=[]
red=[]
for line in task2:
  for i in wordsToRemove:
    line=line.replace(i,"")
    #removes unnecessary spaces and detail from the line
  listForID=line.split(":")
  #filters ID from rest of line
  list_of_sequences=listForID[1].split(";")
  #filters separate lists of scores
  for sequence in list_of_sequences:
    unfiltered_scores=sequence.split(",")
    #finds individual scores by further filtering
    for sepScores in unfiltered_scores: 
      if sepScores.find("green")!=-1 :
        green.append(int(sepScores[:sepScores.find("green")]))
      elif sepScores.find("red")!=-1 :
        red.append(int(sepScores[:sepScores.find("red")]))
      elif sepScores.find("blue")!=-1:
        blue.append(int(sepScores[:sepScores.find("blue")]))
    unfiltered_scores.clear()
  score+=max(blue)*max(red)*max(green)
  blue.clear()
  red.clear()
  green.clear()
  listForID.clear()
  list_of_sequences.clear()
  #clears lists, ready for next iteration
print(score)