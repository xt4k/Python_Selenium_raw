items_in_cart = 2

try:
    pass
    with open('text.txt', 'r') as reader:
        reader.read()
# except:
  #  print("I reach this block because of failure in 'try' block")

except Exception as e:
    print("I reach this block because of failure in 'try' block")
    print("exception is: ",e)
finally:
    print('This block will printed in any case')