def both_ends(s):
  userinput = input
  s = userinput("Choose a name: ")
  if len(s) < 2:
    print("")
  else:
    print(s[0:1]+s[-2:])