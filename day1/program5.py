s1=int(input("enter run scored by 1st player in 60 balls:"))
s2=int(input("enter run scored by 2nd player in 60 balls:"))
s3=int(input("enter run scored by 3rd player in 60 balls:"))
sr1=s1*100/60
sr2=s2*100/60
sr3=s3*100/60
print("strike rate of 1st player is:",sr1)
print("strike rate of 2nd player is:",sr2)
print("strike rate of 3rd player is:",sr3)
sn1=sr1*60/100
sn2=sr2*60/100
sn3=sr3*60/100
print("score by 1st player, if he had played 60 balls more:",sn1)
print("score by 2nd player, if he had played 60 balls more:",sn2)
print("score by 3rd player, if he had played 60 balls more:",sn3)
print("max number of six 1st player could hit:",s1//6)
print("max number of six 2nd player could hit:",s2//6)
print("max number of six 3rd player could hit:",s3//6)
