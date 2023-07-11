def Job_Status_Code(code):
    if(code  == 0):
        return("0: Device Tailed Test")
    if(code  == 1): 
        return("1: Device Disabled")
    if(code  == 2):
        return("2: Maintenance Required")
    if(code  == 3):
        return("3: Detector Sensing Faulty (Idle Low)")
    if(code  == 4):
        return("4: Device Comms Faulty")
    if(code  == 5):
        return("5: Open Circuit Fault")
    if(code  == 6):
        return("6: Device Short Circuit")
    if(code  == 7):
        return("7: Device Unaccepted")
    if(code  == 8):
        return("8: Line Relay failed totrigger/Fault")
    if(code  == 9):
        return("9: Detector Removed from Base")
    if(code  == 10):
        return("10: Incorrect Device Type")
    if(code  == 11):
        return("11: Device Offline/No Power")
    if(code  == 12):
        return("12: Unused-obsolete")
    if(code  == 13):
        return("13: Unused-obsolete")
    if(code  == 14):
        return("14: Loop Fault")
    if(code  == 15):
        return("15: Earth Leakage")
    if(code  == 16):
        return("16: Alarm Fault")
    if(code  == 17):
        return("17: Manual Call-point Loop")
    if(code  == 18):
        return("18: Halon Detonator Loop")
    if(code  == 19):
        return("19: Halon Bell Fault")
    if(code  == 20):
        return("20: T-Bar Recommended")
    if(code  == 21):
        return("21: No Sensors")
    if(code  == 22):
        return("22: External Line Fault")
    if(code  == 23):
        return("23: Fire Station Fault")
    if(code  == 24):
        return("24: RAM Fault")
    if(code  == 25):
        return("25: Power Fault")
    if(code  == 26):
        return("26: Battery Fault")
    if(code  == 27):
        return("27: Charger Fault")
    if(code  == 28):
        return("28: RAM Backup Battery Voltage Low")
    if(code  == 29):
        return("29: Panel Offline")
    if(code  == 30):
        return("30: Panel Online")
    if(code  == 31):
        return("31: Zone Disabled")
    if(code  == 32):
        return("32: Zone Enabled")
    if(code  == 33):
        return("33: Bell Fault")
    if(code  == 34):
        return("34: Unused - Obsolete")
    if(code  == 35):
        return("35: Unused - Obsolete")
    if(code  == 36):
        return("36: Panel Reset")
    if(code  == 37):
        return("37: Panel Alarms Accepted")
    if(code  == 38):
        return("38: Panel Sound Alarms")
    if(code  == 39):
        return("39: returner Options Set")
    if(code  == 40):
        return("40: Panel All Clear")
    if(code  == 41):
        return("41: Fire Alarm")
    if(code  == 42):
        return("42: Pre-Alarm")
    if(code  == 43):
        return("43: Service Required")
    if(code  == 44):
        return("44: Alarm / Trigger")
    if(code  == 45):
        return("45: Unused - Obsolete")
    if(code  == 46):
        return("46: Unused - Obsolete")
    if(code  == 47):
        return("47: Unused - Obsolete")
    if(code  == 48):
        return("48: Service Done")
    if(code  == 49):
        return("49: Unused - Obsolete")
    if(code  == 50):
        return("50: Unused - Obsolete")
    if(code  == 51):
        return("51: Unused - Obsolete")
    if(code  == 52):
        return("52: Unused - Obsolete")
    if(code  == 53):
        return("53: Device Enabled")
    if(code  == 54):
        return("54: Panel Data Accessed/Changed")
    if(code  == 55):
        return("55: unused - obsolete")
    if(code  == 56):
        return("56: Unused - Obsolete")
    if(code  == 57):
        return("57: Triggered Pulsed Output")
    if(code  == 58):
        return("58: Normal Pulsed Output")
    if(code  == 59):
        return("59: RDU Online")
    if(code  == 60):
        return("60: RDU Offline")
    if(code  == 61):
        return("61: RDU Alarm Fault")
    if(code  == 62):
        return("62: RDU Battery Fault")
    if(code  == 63):
        return("63: RDU Mains Fault")
    if(code  == 64):
        return("64: Unused - Obsolete")
    if(code  == 65):
        return("65: Unused - Obsolete")
    if(code  == 66):
        return("66: Memory R/W fault")
    if(code  == 67):
        return("67: Checksum Fault")
    if(code  == 68):
        return("68: Gas Control Unit Gas Drop")
    if(code  == 69):
        return("69: Gas Control Unit General Fault")
    if(code  == 70):
        return("70: Gas Control Unit Door Error")        
    if(code  == 71):
        return("71: Gas Control Unit PSU Fault ")
    if(code  == 72):
        return("72: Gas Control Unit Manual Mode ")
    if(code  == 73):
        return("73: Gas Control Unit Auto Mode ")
    if(code  == 74):
        return("74: Gas Control Unit Locked Off ")
    if(code  == 75):
        return("75: Gas Control Unit Relay Triggered ")
    if(code  == 76):
        return("76:  Gas Control Unit Status Normal ")
    if(code  == 77):
        return("77: Unused - Obsolete")
    if(code  == 78):
        return("78: Stack Fault")
    if(code  == 79):
        return("79: Ext. Computer Offline")
    if(code  == 80):
        return("80: Faulty Z-Input ")
    if(code  == 81):
        return("81: Input On")
    if(code  == 82):
        return("82: Input Off")
    if(code  == 83):
        return("83: Offline Board ")
    if(code  == 84):
        return("84: Test Finished ")
    if(code  == 85):
        return("85: System Fault AGV ")
    if(code  == 86):
        return("86: Dual Monitored Loop")
    if(code  == 87):
        return("87: Output Cancelled ")
    if(code  == 88):
        return("88: Unused - Obsolete")
    if(code  == 89):
        return("89: Unused - Obsolete")
    if(code  == 90):
        return("90: High Sensitivity Smoke Fault")
    if(code  == 91):
        return("91: Text Area Full ")
    if(code  == 92):
        return("92: Security Switch Activated ")
    if(code  == 93):
        return("93: Spare")
    if(code  == 94):
        return("94: Lower Service Band ")
    if(code  == 95):
        return("95: Sounders Silenced ")
    if(code  == 96):
        return("96: Detector Fault Restored ")
    if(code  == 97):
        return("97: System Fault Restored ")
    if(code  == 98):
        return("98: EPROM Changed ")
    if(code  == 99):
        return("99: I/O Disabled ")
    if(code  == 100):
        return("100: I/O Enabled ")        
    if(code  == 101):
        return("101: Comms 2 Ext. Computer Responding")
    if(code  == 102):
        return("102: Addressable Comms Board Offline")
    if(code  == 103):
        return("103: Addressable Comms Board Online")
    if(code  == 104):
        return("104: Night Mode")
    if(code  == 105):
        return("105: Day Mode")
    if(code  == 106):
        return("106: Standard Mode")
    if(code  == 107):
        return("107: Line Sounder Unit Fault")
    if(code  == 108):
        return("108: Line Sounder Unit Ext. Charger Fault")
    if(code  == 109):
        return("109: Line Sounder Unit Ext. Supply Fault")
    if(code  == 110):
        return("110: Output Triggered")
    if(code  == 111):
        return("111: Watchdog")
    if(code  == 112):
        return("112: Menu Access Security Code")
    if(code  == 113):
        return("113: EEPROM Write Fault")
    if(code  == 114):
        return("114: Sounder Timeout")
    if(code  == 115):
        return("115: Unused - Obsolete")
    if(code  == 116):
        return("116: Unused - Obsolete")
    if(code  == 117):
        return("117: Master No Slaves Online")
    if(code  == 118):
        return("118: Slave: Address Group Fault")
    if(code  == 119):
        return("119: High Sensitivity Smoke Pre-Alarm")
    if(code  == 120):
        return("120: Silence Disabled")                
    if(code  == 121):
        return("121: Sounders Disabled")
    if(code  == 122):
        return("122: Comms Link Down/Modem No Carrier")
    if(code  == 123):
        return("123: Comms Link Up")
    if(code  == 124):
        return("124: Common Disable")
    if(code  == 125):
        return("125: Fire-station Disable")
    if(code  == 126):
        return("126: GCU Disable")
    if(code  == 127):
        return("127: General (common) de-isolate/enable")
    if(code  == 128):
        return("128: Device tamper fault e.g. radio device")
    if(code  == 129):
        return("129: Device battery fault e.g. radio device")
    if(code  == 130):
        return("130: Processor fault: LD-PIC, etc")
    if(code  == 131):
        return("131: Double-address fault ")                
    else:
        return("UNKNOWN")

