transactions=[]
total_credit=0
total_debit=0
amount_list=[]
cat_amt={}
cat=''
amt=0.0
#COLLECTING INPUTS FROM THE USER
n=int(input("ENTER THE NUMBER OF TRANSACTIONS: "))
for userno in range(1,n+1):
    user_data={}
    user_data['id']=float(input(f"ENTER USER {userno} ID: "))
    user_data['amount']=float(input("ENTER AMOUNT : "))
    user_data['type']=input("ENTER TYPE OF TRANSACTION ACCOUNT TYPE[CREDIT OR DEBIT]: ").upper()
    user_data['cateogary']=input("ENTER TRANSACTION  CATEGORY:")
    transactions.append(user_data)
print('\n')
print(transactions)
#CALCULATING TOTAL CREDIT AND DEBIT AMOUNT
for i in range(0,n):
    if transactions[i]['type']=='CREDIT':
        total_credit+=transactions[i]['amount']
    elif transactions[i]['type']=='DEBIT':
        total_debit+=transactions[i]['amount']
    #storing every transacton amount in this list for filtering the maximum amount
    amount_list.append(transactions[i]['amount'])




#printin the total credit and debit amount

print("\nTOTAL CREDIT AMOUNT IS :",total_credit)
print("\nTOTAL DEBIT AMOUNT IS :",total_debit)
#MAXIMUM AND MINIMUM AMOUNT

max_amount=max(amount_list)
min_amount=min(amount_list)
#displaying the transaction with LOWEST AMOUNT AND HIGHEST AMOUNT(i could have done this in the above for looop itelf but for readability i used seperate one)
a=0
for j in range(0,n):
    if transactions[j]['amount']==max_amount:
        print("-"*100)
        print(f"THE TRANSACTION WITH HIGHEST AMOUNT IS  :{transactions[j]}")
        print("-"*100)
    if transactions[j]['amount']==min_amount:
        print("-"*100)
        print(f"THE TRANSACTION WITH LOWEST AMOUNT IS :{transactions[j]}")
        print("-"*100)


for i in range(0,n):
    cat=transactions[i]['cateogary']
    amt=transactions[i]['amount']
    if cat in cat_amt:
        cat_amt[cat]+=amt
    else:
        cat_amt[cat]=amt
    
    
print("CATEGORY AND THEIR AMOUNT:")
for key,val in cat_amt.items():
    print("*"*100)
    print(f"CATEGORY:{key} || AMOUNT:{val}")
   





    










