import matplotlib.pyplot as plt

x = [2,4,6,8,10] 
y = [10,20,30,40,50] 
plt.plot(x,y) 
plt.show() 

plt.bar(x,y) 
plt.show()

plt.hist(y) 
plt.show()

plt.scatter(x,y) 
plt.show()

plt.scatter(x,x,label="linear")
plt.scatter(x,x**2,label="quadratic")
plt.scatter(x,x**3,label="cubic")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.title("Practice Graph")
plt.show()

d=pd.read_csv(r"C:\Users\Ankush\Desktop\AI\Scores.csv",encoding='cp1252')
Score_India = d['Score_India']
Score_Pakistan = d['Score_Pakistan']
legend = ['India', 'Pakistan']
plt.hist([Score_India, Score_Pakistan], color=['yellow', 'red'])
plt.xlabel("Runs/Delivery")
plt.ylabel("Frequency")
plt.legend(legend)
plt.xticks(range(0, 7))
plt.yticks(range(1, 20))
plt.title('Champions Trophy 2017 Final\n Runs scored in 4 overs')
plt.show()