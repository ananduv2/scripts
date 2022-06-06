import requests
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=Hi bb, this is a test message by python app.&language=english&route=p&numbers=8921294138,9633881971"
headers = {
'authorization': "UzxD7dBkhqQcMoVLKjg52sCW8RHS3PENr6mlpAwZFf19iJantGNR3JqE7MLKmgxjDfrcZWvOVnTwuYe4",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)