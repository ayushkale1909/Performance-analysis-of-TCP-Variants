#Add Description to tracefiles 

import pandas as pd

input_file_path = r'C:\Users\AyushKale\Desktop\reno.txt'
output_file_path = r'C:\Users\AyushKale\Desktop\output_data7.csv'

cols = ['Event_Type', 'Time', 'Source_Node', 
        'Destination_Node', 'Protocol', 'Packet_Size',
        'Flags', 'Flow_ID', 'Source_Address', 
        'Destination_Address', 'Sequence_Number',
        'Packet_ID']

df = pd.read_csv(input_file_path, sep =' ' ,header = None)
df.columns = cols 
print(df.head())
df.to_csv(output_file_path, index=False)


