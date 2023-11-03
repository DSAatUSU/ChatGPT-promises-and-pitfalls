lst = [str(int(i)**2) for i in input().split(',') if int(i) % 2]
print(",".join(lst))
