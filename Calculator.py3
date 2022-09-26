#Create Calculator using python and create function itself :

def add(P,Q):
    return P + Q
def sub(P,Q):
    return P - Q
def mul(P,Q):
    return (P * Q)
def div(P,Q):
    return P / Q
print("Please select the operation ")
print('a. additon')
print('b. substraction')
print('c. Multiplications')
print('d. division')

choice = input("Please enter choice(a/b/c/d): ")
num_1 = int(input("Enter The First Number :"))
num_2 = int(input("Second The First Number :"))

if choice == 'a':
    print(num_1, "+",num_2, "=", add(num_1, num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", sub(num_1,num_2))
elif choice =='c':
    print(num_1,"*", num_2, "=", mul(num_1,num_2))
elif choice == 'd':
    print(num_1,"/",num_2, "=", div(num_1,num_2))
    
else:
    print("This is a Invalid Number")
    


