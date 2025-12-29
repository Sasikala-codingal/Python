def dueamount(total, paid):
    due = total - paid
    return due

amount = dueamount(4, 2.5)
print("Due amount is:", amount)