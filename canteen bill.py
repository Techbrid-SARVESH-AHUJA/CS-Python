print ("DPSGV Canteen bill entry")
print ("________________________")
print (" ")

name = input("Enter Name: ")

print (" ") 

product_1 = input("Enter product 1: ")
rate_1 = int(input("Enter Rate: "))
quantity_1 = int(input("Enter quantity: "))

print (" ")

product_2 = input("Enter product 2: ")
rate_2 = int(input("Enter Rate: "))
quantity_2 = int(input("Enter quantity: "))

print (" ") , print (" ") , print (" ")

print ("________________________")
print ("Canteen Bill")
print ("________________________")

print ("Name: " + name)

print(" ")

print ("Product 1: " + product_1)
print ("Rate: " + str(rate_1))
print ("Quantity: " + str(quantity_1))
print ("Total: " + str(rate_1*quantity_1))

print (" ")

print ("Product 2: " + product_2)
print ("Rate: " + str(rate_2))
print ("Quantity: " + str(quantity_2))
print ("Total: " + str(rate_2*quantity_2))

print (" ")

grand_total = (rate_1*quantity_1)+(rate_2*quantity_2)
grand_total_str = str((rate_1*quantity_1)+(rate_2*quantity_2))
gst = (grand_total * 18)/100
discount =  (grand_total * 4)/100

print ("GST: " +  str(gst))
print ("Discount: " + str(discount))

print ("________________________")

print ("Grand total: " + str(float((grand_total+gst)-discount)))

print ("________________________")