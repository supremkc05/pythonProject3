import phonenumbers
from test import number
from phonenumbers import geocoder, carrier

# Get information about the geographical region
ch_number = phonenumbers.parse(number, "CH")
region_description = geocoder.description_for_number(ch_number, "en")
print("Geographical Region:", region_description)

# Get information about the carrier
service_number = phonenumbers.parse(number, "RO")
carrier_name = carrier.name_for_number(service_number, "en")
print("Carrier:", carrier_name)

#  Get the description for the phone number's geographical region in English
# The 'geocoder.description_for_number' function takes the parsed phone number and a language code
# ("en" for English in this case)