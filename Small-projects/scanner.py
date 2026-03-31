# user id
# diff apps

import qrcode

#Taking UPI ID as an input
upi_id = input("Enter your UPI id = ")

#upi://pay?ps=UPI_ID&apn=NAME&am=Amount$cu=CURRENCY&tn=MESSAGE


import qrcode

#Taking UPI ID as an input
upi_id = input("Enter your UPI id = ")

#upi://pay?ps=UPI_ID&apn=NAME&am=Amount$cu=CURRENCY&tn=MESSAGE

# pa = upi id in ehich we have to do payment
#
# pn = recipent name
#
# am = amount
#
# cu = currency
#
# tn = payment message

phone_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create QR code for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the QR code to image file(optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')
