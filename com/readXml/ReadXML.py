import xml.etree.cElementTree as xml
from urllib.response import addbase

path = xml.parse(r"C:\Users\ManoKutty\PycharmProjects\APITesting\XML\Booking.xml")
root = path.getroot()

print("*********Booking Dteatils*********")
print("From : " + root[0].text)
print("To : " + root[1].text)
print("TripType :  " + root[2].text)
print("FromDate :  " + root[3].text)
print("Return Date :  " + root[4].text)
print("Flight no :  " + root[5].text)

print("*******Passenger Details*************")
print("Passenger Name: " +root[6][0].text)
print("Passenger DOB: " +root[6][1].text)

print("*********Address************")
address = root[6][2]
print("Street Name: " +address[0].text)
print("City Name: " +address[1].text)
print("District Name: " +address[2].text)
print("State Name: " +address[3].text)
print("Country Name: " +address[4].text)

print("***********Communication Details*************")

print("**Phone**")
phone = address[5][0]
print("Mobile no: " + phone[0].text)
print("Landline  no: " + phone[1].text)

print("**Mail**")
mail = address[5][1]
print("Personal Email: " +mail[0].text);
print("Official Email: " +mail[1].text);

print("*********payment Details********")
payment = root[7]
print("CardName: " + payment[0].text);
print("CardHolderName: " + payment[1].text);
print("Card No: " + payment[2].text);
print("CCV: " + payment[3].text);




