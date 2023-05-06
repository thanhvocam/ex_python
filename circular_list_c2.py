def circularly_list(l1,l2):
  new_list=[]
  for i in range(len(l2)):
    if l1[0] == l2[i]:
      new_list.append(l2.index(i))
  return new_list
circularly_list([1,4,1,2,1,2,1,2],[1,2,1,4,1,2,1,2])
