class Info():
    
    def Job_Code(self, j_code):
        match j_code:
            case '0':
                return("JobCode 0: Comms Test Message")
            case '1':
                return("JobCode 1: Status Events Message")
            case '4':
                return("JobCode 4: Panel Status Request/Reply") #fetch all events since last reset
            case '0xFF':
                return("JobCode 0xFF: Refuse Job") #Response to invalid access attempt
            

    def Job_Status_Code(self, code):
        match code:
            case 0:
                return("StatusCode 0: Device Tailed Test")
            case 1: 
                return("StatusCode 1: Device Disabled")
            case 2:
                return("StatusCode 2: Maintenance Required")
            case 3:
                return("StatusCode 3: Detector Sensing Faulty (Idle Low)")
            case 4:
                return("StatusCode 4: Device Comms Faulty")
            case 5:
                return("StatusCode 5: Open Circuit Fault")
            case 6:
                return("StatusCode 6: Device Short Circuit")
            case 7:
                return("StatusCode 7: Device Unaccepted")
            case 8:
                return("StatusCode 8: Line Relay failed totrigger/Fault")
            case 9:
                return("StatusCode 9: Detector Removed from Base")
            case 10:
                return("StatusCode 10: Incorrect Device Type")
            case 11:
                return("StatusCode 11: Device Offline/No Power")
            case 12:
                return("StatusCode 12: Unused-obsolete")
            case 13:
                return("StatusCode 13: Unused-obsolete")
            case 14:
                return("StatusCode 14: Loop Fault")
            case 15:
                return("StatusCode 15: Earth Leakage")
            case 16:
                return("StatusCode 16: Alarm Fault")
            case 17:
                return("StatusCode 17: Manual Call-point Loop")
            case 18:
                return("StatusCode 18: Halon Detonator Loop")
            case 19:
                return("StatusCode 19: Halon Bell Fault")
            case 20:
                return("StatusCode 20: T-Bar Recommended")
            case 21:
                return("StatusCode 21: No Sensors")
            case 22:
                return("StatusCode 22: External Line Fault")
            case 23:
                return("StatusCode 23: Fire Station Fault")
            case 24:
                return("StatusCode 24: RAM Fault")
            case 25:
                return("StatusCode 25: Power Fault")
            case 26:
                return("StatusCode 26: Battery Fault")
            case 27:
                return("StatusCode 27: Charger Fault")
            case 28:
                return("StatusCode 28: RAM Backup Battery Voltage Low")
            case 29:
                return("StatusCode 29: Panel Offline")
            case 30:
                return("StatusCode 30: Panel Online")
            case 31:
                return("StatusCode 31: Zone Disabled")
            case 32:
                return("StatusCode 32: Zone Enabled")
            case 33:
                return("StatusCode 33: Bell Fault")
            case 34:
                return("StatusCode 34: Unused - Obsolete")
            case 35:
                return("StatusCode 35: Unused - Obsolete")
            case 36:
                return("StatusCode 36: Panel Reset")
            case 37:
                return("StatusCode 37: Panel Alarms Accepted")
            case 38:
                return("StatusCode 38: Panel Sound Alarms")
            case 39:
                return("StatusCode 39: returner Options Set")
            case 40:
                return("StatusCode 40: Panel All Clear")
            case 41:
                return("StatusCode 41: Fire Alarm")
            case 42:
                return("StatusCode 42: Pre-Alarm")
            case 43:
                return("StatusCode 43: Service Required")
            case 44:
                return("StatusCode 44: Alarm / Trigger")
            case 45:
                return("StatusCode 45: Unused - Obsolete")
            case 46:
                return("StatusCode 46: Unused - Obsolete")
            case 47:
                return("StatusCode 47: Unused - Obsolete")
            case 48:
                return("StatusCode 48: Service Done")
            case 49:
                return("StatusCode 49: Unused - Obsolete")
            case 50:
                return("StatusCode 50: Unused - Obsolete")
            case 51:
                return("StatusCode 51: Unused - Obsolete")
            case 52:
                return("StatusCode 52: Unused - Obsolete")
            case 53:
                return("StatusCode 53: Device Enabled")
            case 54:
                return("StatusCode 54: Panel Data Accessed/Changed")
            case 55:
                return("StatusCode 55: unused - obsolete")
            case 56:
                return("StatusCode 56: Unused - Obsolete")
            case 57:
                return("StatusCode 57: Triggered Pulsed Output")
            case 58:
                return("StatusCode 58: Normal Pulsed Output")
            case 59:
                return("StatusCode 59: RDU Online")
            case 60:
                return("StatusCode 60: RDU Offline")
            case 61:
                return("StatusCode 61: RDU Alarm Fault")
            case 62:
                return("StatusCode 62: RDU Battery Fault")
            case 63:
                return("StatusCode 63: RDU Mains Fault")
            case 64:
                return("StatusCode 64: Unused - Obsolete")
            case 65:
                return("StatusCode 65: Unused - Obsolete")
            case 66:
                return("StatusCode 66: Memory R/W fault")
            case 67:
                return("StatusCode 67: Checksum Fault")
            case 68:
                return("StatusCode 68: Gas Control Unit Gas Drop")
            case 69:
                return("StatusCode 69: Gas Control Unit General Fault")
            case 70:
                return("StatusCode 70: Gas Control Unit Door Error")        
            case 71:
                return("StatusCode 71: Gas Control Unit PSU Fault ")
            case 72:
                return("StatusCode 72: Gas Control Unit Manual Mode ")
            case 73:
                return("StatusCode 73: Gas Control Unit Auto Mode ")
            case 74:
                return("StatusCode 74: Gas Control Unit Locked Off ")
            case 75:
                return("StatusCode 75: Gas Control Unit Relay Triggered ")
            case 76:
                return("StatusCode 76:  Gas Control Unit Status Normal ")
            case 77:
                return("StatusCode 77: Unused - Obsolete")
            case 78:
                return("StatusCode 78: Stack Fault")
            case 79:
                return("StatusCode 79: Ext. Computer Offline")
            case 80:
                return("StatusCode 80: Faulty Z-Input ")
            case 81:
                return("StatusCode 81: Input On")
            case 82:
                return("StatusCode 82: Input Off")
            case 83:
                return("StatusCode 83: Offline Board ")
            case 84:
                return("StatusCode 84: Test Finished ")
            case 85:
                return("StatusCode 85: System Fault AGV ")
            case 86:
                return("StatusCode 86: Dual Monitored Loop")
            case 87:
                return("StatusCode 87: Output Cancelled ")
            case 88:
                return("StatusCode 88: Unused - Obsolete")
            case 89:
                return("StatusCode 89: Unused - Obsolete")
            case 90:
                return("StatusCode 90: High Sensitivity Smoke Fault")
            case 91:
                return("StatusCode 91: Text Area Full ")
            case 92:
                return("StatusCode 92: Security Switch Activated ")
            case 93:
                return("StatusCode 93: Spare")
            case 94:
                return("StatusCode 94: Lower Service Band ")
            case 95:
                return("StatusCode 95: Sounders Silenced ")
            case 96:
                return("StatusCode 96: Detector Fault Restored ")
            case 97:
                return("StatusCode 97: System Fault Restored ")
            case 98:
                return("StatusCode 98: EPROM Changed ")
            case 99:
                return("StatusCode 99: I/O Disabled ")
            case 100:
                return("StatusCode 100: I/O Enabled ")        
            case 101:
                return("StatusCode 101: Comms 2 Ext. Computer Responding")
            case 102:
                return("StatusCode 102: Addressable Comms Board Offline")
            case 103:
                return("StatusCode 103: Addressable Comms Board Online")
            case 104:
                return("StatusCode 104: Night Mode")
            case 105:
                return("StatusCode 105: Day Mode")
            case 106:
                return("StatusCode 106: Standard Mode")
            case 107:
                return("StatusCode 107: Line Sounder Unit Fault")
            case 108:
                return("StatusCode 108: Line Sounder Unit Ext. Charger Fault")
            case 109:
                return("StatusCode 109: Line Sounder Unit Ext. Supply Fault")
            case 110:
                return("StatusCode 110: Output Triggered")
            case 111:
                return("StatusCode 111: Watchdog")
            case 112:
                return("StatusCode 112: Menu Access Security Code")
            case 113:
                return("StatusCode 113: EEPROM Write Fault")
            case 114:
                return("StatusCode 114: Sounder Timeout")
            case 115:
                return("StatusCode 115: Unused - Obsolete")
            case 116:
                return("StatusCode 116: Unused - Obsolete")
            case 117:
                return("StatusCode 117: Master No Slaves Online")
            case 118:
                return("StatusCode 118: Slave: Address Group Fault")
            case 119:
                return("StatusCode 119: High Sensitivity Smoke Pre-Alarm")
            case 120:
                return("StatusCode 120: Silence Disabled")                
            case 121:
                return("StatusCode 121: Sounders Disabled")
            case 122:
                return("StatusCode 122: Comms Link Down/Modem No Carrier")
            case 123:
                return("StatusCode 123: Comms Link Up")
            case 124:
                return("StatusCode 124: Common Disable")
            case 125:
                return("StatusCode 125: Fire-station Disable")
            case 126:
                return("StatusCode 126: GCU Disable")
            case 127:
                return("StatusCode 127: General (common) de-isolate/enable")
            case 128:
                return("StatusCode 128: Device tamper fault e.g. radio device")
            case 129:
                return("StatusCode 129: Device battery fault e.g. radio device")
            case 130:
                return("StatusCode 130: Processor fault: LD-PIC, etc")
            case 131:
                return("StatusCode 131: Double-address fault ")                
            case _:
                return("StatusCode UNKNOWN")
