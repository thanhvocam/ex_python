def circularly_list(l1,l2):
  new_list=[]
  for i in range(len(l2)):
    if l2[i] == l1[0]:
      new_list.append(i)
  return new_list
circularly_list([1,4,1,2,1,2,1,2],[1,2,1,4,1,2,1,2])
