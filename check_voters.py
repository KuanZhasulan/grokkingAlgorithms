voters = dict();
def checkvoter(name):
  if voters.get(name):
    print "Kick em out"
  else:
    voters[name] = True
    print "Let em in"

checkvoter("Zhassulan")
checkvoter("Baur")
checkvoter("Adai")
checkvoter("Adai")
print voters
