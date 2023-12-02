task2=open("task2.txt","r")
words_to_remove=[" ","Game"]
score=0
impossible_score=False
for line in task2:
  for i in words_to_remove:
    line=line.replace(i,"")
    #removes unnecessary spaces and detail from the line
  list_for_ID=line.split(":")
  #filters ID from rest of line
  list_of_sequences=list_for_ID[1].split(";")
  #filters separate lists of scores
  for sequence in list_of_sequences:
    scores=sequence.split(",")
    #finds individual scores by further filtering
    for separate_scores in scores:
      if separate_scores.find("green")!=-1 :
        if int(separate_scores[:separate_scores.find("green")])>13:
          impossible_score=True
          break
      elif separate_scores.find("red")!=-1 :
        if int(separate_scores[:separate_scores.find("red")])>12:
          impossible_score=True
          break
      elif separate_scores.find("blue")!=-1:
        if int(separate_scores[:separate_scores.find("blue")])>14:
          impossible_score=True
          break
  if impossible_score==False:
    score+=int(list_for_ID[0])
  scores.clear() 
  list_for_ID.clear()
  list_of_sequences.clear() 
  impossible_score=False
  #clears lists and resets the boolean value, ready for next iteration
print(score)
task2.close()


    
