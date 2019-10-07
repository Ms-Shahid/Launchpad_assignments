qty = float(input("enter the quantity of the item sold:"))
val= float(input(" enter the value of the item:"))
discount= float(input("enter the discount percentage"))
tax=float(input(" enter the tax:"))
amt=qty*val
discount_amt=(amt*discount)/100
sub_amount= amt-discount_amt
tax_amt=(sub_amount*tax)/100
total_amt=sub_amount+tax_amt
print("**********BILL*********")
print("quantity sold: \t",qty)
print("price per item: \t",val)
print("amount\t\t",amt)
print("discount:\t\t-",discount_amt)
print("\n \t ------------------")
print("Discounted Total :\t",sub_amount)
print("tax: \t\t\t" + "tax_amt")
print(" \t  \t------------")
print("total amount to be paid", total_amt)
