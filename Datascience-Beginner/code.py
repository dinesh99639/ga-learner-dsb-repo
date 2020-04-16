# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter=',', skip_header=1)
census = np.concatenate((data, new_record))


# --------------
#Code starts here
age = census[:,0]
max_age = np.max(age)
min_age = np.min(age)
age_mean= np.mean(age)
age_std= np.std(age)


# --------------
#Code starts here
# race_0 = np.array(np.where(census[:,2]==0))
race_0 = np.array([census[census[:,2]==0, 2]])
race_1 = np.array([census[census[:,2]==1, 2]])
race_2 = np.array([census[census[:,2]==2, 2]])
race_3 = np.array([census[census[:,2]==3, 2]])
race_4 = np.array([census[census[:,2]==4, 2]])

len_0 = len(race_0[0])
len_1 = len(race_1[0])
len_2 = len(race_2[0])
len_3 = len(race_3[0])
len_4 = len(race_4[0])

tmp = [len_0, len_1, len_2, len_3, len_4]

minority_race = tmp.index(min(tmp))
# print(minority_race)


# --------------
#Code starts here
# print("tt", census[:,0].size)
senior_citizens = census[census[:, 0]>60,:]
working_hours_sum = np.sum(senior_citizens[:,6])
senior_citizens_len = senior_citizens[:, 0].size
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)
# print(senior_citizens_len)


# --------------
#Code starts here
high = census[census[:,1]>10]
low  = census[census[:,1]<=10]

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

print(avg_pay_high>avg_pay_low)


