import pandas as pd
import random
from cryptography.fernet import Fernet
import fitbit
from tabulate import tabulate

client_id = '23RG84'
client_secret = '33176108a867f4b91259cbe9fcf805e2'
redirect_uri = 'http://localhost'
auth_client = fitbit.Fitbit(client_id, client_secret, redirect_uri=redirect_uri, timeout=10)

auth_url = 'https://www.fitbit.com/oauth2/authorize'
print("Authorization URL:", auth_url)

def generate_cipher():
    key = Fernet.generate_key()
    cipher = Fernet(key)
    return cipher

def encrypt_data(cipher, data):
    if isinstance(data, str):
        data = data.encode()
    encrypted_data = cipher.encrypt(data)
    return encrypted_data


def decrypt_data(cipher, encrypted_data):
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data.decode()

cipher = generate_cipher()

df = pd.read_csv('smartwatch_natural_data.csv')
interaction_points = df['source'].unique()

categories = {
    'accelerometer': 'Medical IoT device',
    'gyroscope': 'Wearable health monitor',
    'audio': 'Cloud storage solution',
    'step_detect': 'Wearable health monitor',
    'battery': 'Device System Info',
    'activity': 'User Activity Tracker',
    'orientation': 'Device Sensor Data',
    'magnetometer': 'Device Sensor Data',
    'light': 'Ambient Sensor Data',
    'gravity': 'Device Sensor Data',
    'pressure': 'Ambient Sensor Data',
    'wifi': 'Device Connectivity Info',
    'linear_acceleration': 'Medical IoT device',
    'heart_rate': 'Ambient Sensor Data',
    'step_counter': 'Ambient Sensor Data',
    'step_detector': 'Ambient Sensor Data',
    'rotation_vector': 'Device Sensor Data'
}

for point in interaction_points:
    if point not in categories:
        categories[point] = 'Unknown'

custodians_list = ["Custodian A", "Custodian B", "Custodian C", "Custodian D", "Custodian E"]

assigned_custodians = {point: random.choice(custodians_list) for point in interaction_points}

df['Category'] = df['source'].map(categories)
df['Assigned Custodian'] = df['source'].map(assigned_custodians)

report = pd.DataFrame({
    'Data Interaction Point': interaction_points,
    'Category': [categories[point] for point in interaction_points],
    'Responsible Custodian': [assigned_custodians[point] for point in interaction_points]
})

print(report)

log_columns = ['index', 'source', 'timestamp', 'values', 'Category', 'Assigned Custodian']
log_df = pd.DataFrame(columns=log_columns)

for idx, row in df.iterrows():
    log_entry = pd.DataFrame({
        'index': [row['index']],
        'source': [row['source']],
        'timestamp': [row['timestamp']],
        'values': [encrypt_data(cipher, str(row['values']))],
        'Category': [row['Category']],
        'Assigned Custodian': [row['Assigned Custodian']]
    })
    log_df = pd.concat([log_df, log_entry], ignore_index=True)

log_df['values'] = log_df['values'].apply(lambda x: decrypt_data(cipher, x))
log_df.to_csv('data_interaction_log.csv', index=False)


#
print("Data interactions have been logged and encrypted!")