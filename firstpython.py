import queue as q

q = q.Queue()

q.put("Raphael")
q.put("Leonardo")
q.put("Donatello")
q.put("Michealango")

print("Items in Queue:")
print(q.get())
print(q.get())
print(q.get())
print(q.get())