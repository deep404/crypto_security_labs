import os
from pathlib import Path

from pymongo import MongoClient
from pymongo.encryption_options import AutoEncryptionOpts
from pymongo.errors import EncryptionError
from bson import json_util


# Create data for database
data = {"_id" : ['1231', '5213', '4896', '12379', '7891', '4894', '6841',
						'7889', '1238', '6668', '3333', '778333', '6699', '5555',
						'1111', '2355', '9999', '49411', '9741'],
		"full_name" : ['Moglan Mihai', 'Papaluta Vasile', 'Cazacu Constantin', 'Clefos Alexandru',
 						'Trubca Dima', 'Balan Victor', 'Botezat Roman', 'Cerlat Pavel', 'Piciriga Bogdan',
 						 'Danilescu Alexandru', 'Bega Dumitru', 'Morari Gheorghe', 'Astifeni Mihai',
 						 'Pasecinic Nichita', 'Ursu Nicolae', 'Puscas Dumitru', 'Furdui Sandu',
 						 'Dogari Valentin', 'Lupu Mihai'],
 		"ssn" : ['15603790', '59067212', '78109337', '66370666', '32366054', '88567430', '71894498' ,
 				 '28804735', '17066006', '31757018', '20358554', '26492549', '28777437', '71808918',
 				 '75193109', '42139444', '13518874', '70498608', '74096718']}


# Load the master key from 'key_bytes.bin':
key_bin = Path("key_bytes.bin").read_bytes()

# Load the 'person' schema from "json_schema.json":
collection_schema = json_util.loads(Path("json_schema.json").read_text())


# Configure a single, local KMS provider, with the saved key:
kms_providers = {"local": {"key": key_bin}}

# Create a configuration for PyMongo, specifying the local master key,
# the collection used for storing key data, and the json schema specifying
# field encryption:
csfle_opts = AutoEncryptionOpts(
   kms_providers,
   "lab7.__keystore",
   schema_map={"lab7.people": collection_schema},
)

username = 'moglanmihai'
password = 'Zm9I5JR0YKYukEGW'

# Add a new document to the "people" collection, and then read it back out
# to demonstrate that the ssn field is automatically decrypted by PyMongo:
with MongoClient("mongodb+srv://" + username + ":" + password + "@cluster0.quxiy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", auto_encryption_opts=csfle_opts) as client:
	client.lab7.people.delete_many({})

	for index in range(len(data['full_name'])):
		client.lab7.people.insert_one({
				"_id": data['_id'][index],
   			"full_name": data['full_name'][index],
   			"ssn": data['ssn'][index],
			})

