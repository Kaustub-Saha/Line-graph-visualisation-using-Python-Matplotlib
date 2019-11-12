import pandas as pd
import matplotlib.pyplot as plt

def Utilisation():
     Util = pd.read_csv("C:\\Users\\ksaha029\\Documents\\data set\\time\\part-00000-54e4bc04-7b3a-4a5d-83c7-0584e7d32ef5-c000.csv").fillna(0)
     Util.rename(columns={'Staff Name':'Staff_Name','SDC Staff Number':'SDC_Staff_Number'},inplace = True)
     for i, row in Util.iterrows():
          val=row['SDC_Staff_Number'][2::]
          Util.set_value(i,'SDC_Staff_Number',val)
     Util[["SDC_Staff_Number"]] = Util[["SDC_Staff_Number"]].astype(int)
     Emp = pd.read_csv("C:\\Users\\ksaha029\\Documents\\data set\\time\\Automation CoE team roster - Sheet1.csv").fillna(0)
     Emp = Emp[['Name','Designation','Employee ID']]
     Emp.rename(columns={'Name':'Name','Designation':'Designation','Employee ID':'Employee_ID'},inplace = True)
     Emp[["Employee_ID"]] = Emp[["Employee_ID"]].astype(int)
     Joined = Util.merge(Emp, how='inner', left_on='SDC_Staff_Number', right_on='Employee_ID')
     Joined = Joined[['Staff_Name','SDC_Staff_Number','Utilisation','Chargeable_hours','Non_chargeable_hours','Designation']]
     Associate = pd.DataFrame(columns = {'Staff_Name','SDC_Staff_Number','Utilisation','Chargeable_hours','Non_chargeable_hours','Designation'})
     Above_Associate = pd.DataFrame(columns = {'Staff_Name','SDC_Staff_Number','Utilisation','Chargeable_hours','Non_chargeable_hours','Designation'})
     for index,row in Joined.iterrows():
          if row['Designation'].startswith('A'):
               Associate = Associate.append(row)
          else:
               Above_Associate = Above_Associate.append(row)
     Associate = Associate.sort_values(by=['Utilisation'])
     Above_Associate = Above_Associate.sort_values(by=['Utilisation'])
     plt.figure(figsize=[15,8])
     plt.plot(Associate['Staff_Name'],Associate['Utilisation'],marker='o',label='Utilisation')
     plt.grid(True)
     plt.title('Utilization graph for Associates')
     plt.xlabel('Staff Name')
     plt.ylabel('Utilization')
     plt.xticks(rotation='vertical')
     plt.savefig('C:\\Users\\ksaha029\\Documents\\Associate.png',dpi=300,bbox_inches='tight')
     plt.figure(figsize=[15,8])
     plt.plot(Above_Associate['Staff_Name'],Above_Associate['Utilisation'],color='green',marker='o',label='Utilisation')
     plt.grid(True)
     plt.title('Utilization graph for Senior Associate and above')
     plt.xlabel('Staff Name')
     plt.ylabel('Utilization')
     plt.xticks(rotation='vertical')
     plt.savefig('C:\\Users\\ksaha029\\Documents\\Senior Associate and above.png',dpi=300,bbox_inches = 'tight')

if __name__=='__main__':
     print('processing in process')
     Utilisation()
     print('processing ended')
