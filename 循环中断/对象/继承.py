class Phone:
    IMEI =None
    producer = "ITCAST"

    def call_by_4g(self):
        print("通话")

class Phone2022(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("5g通话")

phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")

class MyPhone(Phone,NFCReader,RemoteControl):
    pass

phone1 =MyPhone()
phone1.call_by_4g()
phone1.read_card()
phone1.write_card()
phone1.control()
print(phone1.producer)