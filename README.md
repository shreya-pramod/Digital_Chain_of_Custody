## Overview
This script is designed for managing and securing data interactions from a smartwatch dataset. It automates tasks like Fitbit API authentication, data encryption, data categorization, and custodian assignment.

## Features
- **Fitbit API Authentication**: Sets up and authenticates with the Fitbit API using client credentials.
- **Encryption and Decryption**: Utilizes `cryptography` library to generate a Fernet key for encrypting and decrypting data.
- **Data Categorization and Custodian Assignment**: Categorizes data interaction points and assigns custodians from a predefined list.
- **Data Interaction Log**: Logs and encrypts data interactions, then saves them to a CSV file.

## Requirements
- Python libraries: `pandas`, `random`, `cryptography`, `fitbit`, `tabulate`
- Fitbit client credentials (client_id and client_secret)
- Dataset file: `smartwatch_natural_data.csv`

## Setup and Execution
1. **Install Required Libraries**: Install all the required Python libraries.
2. **Dataset Preparation**: Place the `smartwatch_natural_data.csv` file in the same directory as the script.
3. **Fitbit Credentials**: Enter your Fitbit API client credentials in the script.
4. **Run the Script**: Execute the script. Follow the authorization URL to authenticate with Fitbit if necessary.
5. **Output**: The script processes the data and outputs an encrypted log in `data_interaction_log.csv`.

## Functions
- `generate_cipher()`: Generates an encryption cipher.
- `encrypt_data(cipher, data)`: Encrypts the given data using the cipher.
- `decrypt_data(cipher, encrypted_data)`: Decrypts the encrypted data using the cipher.

## Output Files
- **Report**: Summarizes data interaction points, categories, and assigned custodians.
- **Encrypted Log File**: `data_interaction_log.csv`, containing the logged and encrypted data interactions.
