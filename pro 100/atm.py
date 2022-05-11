class atm(object):
    def __init__(self,atm_card_number,pin_number):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number
    def cashwithdrawl(self):
        print("withdraw cash")

    def balanceinquiry(self):
        print("balance")

hdfc = atm("1010","2020")
print(hdfc.cashwithdrawl())
print(hdfc.balanceinquiry())

        