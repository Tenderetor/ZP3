import serial
import select
import sys
import logging
import json
import StatusCodes

# CONFIGURE THE SERIAL PORT
serial_port = '/dev/ttyUSB0'
baud_rate = 9600
timeout = 1

# open the serial port
ser = serial.Serial(serial_port, baud_rate, timeout=timeout)

# sending data
# data_to_send = 'Reset Panel'
# ser.write(data_to_send.encode()) #convert the data bytes

logging.basicConfig(filename="test.txt",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Let us Create an object
logger = logging.getLogger()

# Now we are going to Set the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

logger.debug('                       log the bytes:')

Global_Responses_Dictionary = {}

class MessageHeading():

    def block_or_job_length(self, list):
        decoded_SOH_block= list[0].decode()
        the_byte = decoded_SOH_block[1:5]
        return int(the_byte, 16)  
          
    def DomainAddress(self, list):
        decoded_SOH_block = list[0].decode()
        the_byte = decoded_SOH_block[5:7]
        return int(the_byte, 16)
        
    def SiteAddress(self, list):
        decoded_SOH_block = list[0].decode()
        the_byte = decoded_SOH_block[7:9]
        return int(the_byte, 16)

    def HostAddress(self, list):
        decoded_SOH_block = list[0].decode()
        the_byte = decoded_SOH_block[9:11]
        return int(the_byte, 16)
        
    def PanelNumber(self, list):
        decoded_SOH_block = list[0].decode()
        the_byte = decoded_SOH_block[11:13]
        return int(the_byte, 16)        
    
    def MessageID(self,list):
        decoded_SOH_block = list[0].decode()        
        the_byte = decoded_SOH_block[13:17]       
        return int(the_byte, 16)            

    def Priority(self, list):
        decoded_SOH_block = list[0].decode()
        the_byte = decoded_SOH_block[17]
        return self.PriorityMeaning(the_byte)  
    
    def PriorityMeaning(self, byte):
        print("Priority meaning byte is: ",byte)
        if(byte == "9"):
            return("Level 9: Commands - Evacuate, Silence, Accept, Reset")
        if(byte == "8"):
            return("Level 8: Fire Events")
        if(byte == "7"):
            return("Security Events")
        if(byte == "6"):
            return("Disabled Zones/Devices/IO, Disable/Enable Command")
        if(byte == "5"):
            return("Pre-Alarm Events, Fault Events")
        if(byte == "3"):
            return("Level 3: Service Condition Events")
        if(byte == "1"):
            return("Level 1: Outputs Activated/Deactivated, Other Request Controls")
        if(byte == "0"):
            return("Level 0: All other conditions")
        else:
            # ans = str(byte) + "Level unknown"
            return("Level unknown")

class EventTelegram_or_CommsTest():

    def block_or_job_length(self, STX_block):
        STX_block_decoded = STX_block.decode()
        the_byte = STX_block_decoded[1:5]
        return int(the_byte, 16)

    def GetJobCode(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[5]
        return (the_byte+": Comms Test Message")

    def GetStatus_Code(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[6:8]
        c = int(the_byte,16)
        return(StatusCodes.Job_Status_Code(c))
        #return int(the_byte, 16)

    def GetPanel_Number(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[8:10]
        return int(the_byte, 16)

    def GetLine_Code(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[10:12]
        c = int(the_byte,16)
        return(StatusCodes.LineCodeMeaning(c))
        # return int(the_byte, 16)

    def GetDeviceAddr(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[12:14]
        return int(the_byte, 16)

    def GetInfoCode(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[14:16]
        return int(the_byte, 16)

    def GetSuperZoneCode(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[16:18]
        return int(the_byte, 16)

    def GetDeviceTypeCode(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[18:20]
        return int(the_byte, 16)

    def GetDateYear(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[20:22]
        return int(the_byte, 16)

    def GetDateMonth(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[22:24]
        return int(the_byte, 16)

    def GetDateDay(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[24:26]
        return int(the_byte, 16)

    def GetDateHour(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[26:28]
        return int(the_byte, 16)

    def GetDateMinute(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[28:30]
        return int(the_byte, 16)

    def GetDateSecond(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[30:32]
        return int(the_byte, 16)


class PanelStatusReply():

    def block_or_job_length(self, STX_block):
        STX_block_decoded = STX_block.decode()
        the_byte = STX_block_decoded[1:5]
        return int(the_byte, 16)

    def GetJobCode(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[5]
        return the_byte

    def GetDirection4(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[6]
        return the_byte

    def GetPanel_num4(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[7:9]
        return int(the_byte, 16)

    def GetLine_Num4(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[9:11]
        return int(the_byte, 16)

    def GetDeviceStatus4(self, STX_block):
        print("untested")
        decoded_STX_block = STX_block.decode()
        struct = decoded_STX_block[11:]
        # convert each byte to ASCII-HEX
        struct_msg = self.byte_to_ascii_hex4(struct)
        return struct_msg

    def byte_to_ascii_hex4(self, byte_obj):
        hex_list = []
        for byte in byte_obj:
            hex_str = hex(byte)[2:].zfill(2)
            hex_list.append(hex_str)
        return hex_list


class ExtractionOf_OXFF():

    def block_or_job_length(self, STX_block):
        STX_block_decoded = STX_block.decode()
        the_byte = STX_block_decoded[1:5]
        return int(the_byte, 16)

    def GetJobCode(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[5]
        return the_byte

    def GetPanel_Number0XFF(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[6:8]
        return int(the_byte, 16)

    def GetRefusedJOb0XFF(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[8]
        return the_byte

    def GetReasonCode0XFF(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[9:11]
        return self.Reasonforrefusal0XFF(int(the_byte, 16))

    def GetSubCode0XFF(self, STX_block):
        decoded_STX_block = STX_block.decode()
        the_byte = decoded_STX_block[11:13]
        return self.RefusalSubCode0XFF(int(the_byte, 16))

    def Reasonforrefusal0XFF(self, code):
        if (code == 0):
            return ("Code 0: System Busy")
        if (code == 1):
            return ("Code 1: Invalid Job / Prohibited Job")
        if (code == 4):
            return ("Code 4: Access denied. Invalid access code")
        if (code == 7):
            return ("Code 7: Requested Node offline")
        if (code == 8):
            return ("Code 8: Requested Node unavailable")
        else:
            return ("Unknown")

    def RefusalSubCode0XFF(self, sub_Code):
        if (sub_code == 0):
            return ("Sub_Code 0 - Comms Failed: Panel unavailable")
        if (sub_code == 1):
            return ("Sub_Code 1 - Comms Failed: Timed out")
        if (sub_code == 2):
            return ("Sub_Code 2 - Comms Failed: Panel offline")
        else:
            return ("Unknown")


def find_markers(rx_data):
    markers = []

    # Iterate through the string
    for i in range(len(rx_data)):
        # Check if the current character is the STX ASCII code
        logger.debug("                       %s:%s", i, rx_data[i])
        if rx_data[i] == 1:
            # SOH found
            logger.debug("                       SOH found at index:%s", i)
            markers.append(i)
        if rx_data[i] == 2:
            # STX found, print the index
            logger.debug("                       STX found at index:%s", i)
            markers.append(i)
        if rx_data[i] == 3:
            # ETX found
            logger.debug("                       ETX found at index:%s", i)
            markers.append(i)
        if rx_data[i] == 4:
            # EOT found
            logger.debug("                       EOT found at index:%s", i)
            markers.append(i)
        if rx_data[i] == 6:
            # ACK found
            logger.debug("                       ACK found at index:%s", i)
            markers.append(i)
        if rx_data[i] == 21:
            # NCK found
            logger.debug("                       NCK found at index:%s", i)
            markers.append(i)

    logger.debug(markers)
    return markers


def extract_between_markers(rx_data, position_of_markers_list):

    list_of_lists = []

    # create a list of lists. each list will contain the byte strings between
    # 2 markers
    for marker in range(len(position_of_markers_list) - 1):
        data_string_list = []
        list_of_lists.append(data_string_list)

    # extract the byte strings between markers
    for i in range(len(position_of_markers_list) - 1):
        list_of_lists[i].append(
            rx_data[position_of_markers_list[i]:position_of_markers_list[i + 1]])

    # # Print the arrays
    for i, arr in enumerate(list_of_lists):
        print(f"Array {i+1}: {arr}")

    return list_of_lists


def GetCheckSum(rx_data):
    etx_index = 0
    eot_index = 0
    for i in range(len(rx_data)):
        if rx_data[i] == 3:  # ETX found
            etx_index = i
        if rx_data[i] == 4:  # EOT found
            eot_index = i

        checksum_data = rx_data[etx_index + 1:eot_index]
    if (eot_index == 0 or etx_index == 0):
        return 0
    else:
        return (int(checksum_data, 16))
        # return checksum_data #return the bytes so long until we can calculate
        # the actual crc of rx data


def GetJobCode(stx_block):
    decoded_stx_block = stx_block.decode()
    the_byte = decoded_stx_block[5]
    print("the returning job code:", the_byte)
    return the_byte


def Deal_Panel_Reply(rx_data):

    if (rx_data[18] != 2):
        return None  # invalid data
    else:

        markers = find_markers(rx_data)
        lists_of_blocks = []
        lists_of_blocks = extract_between_markers(rx_data, markers)
        _1st_block = lists_of_blocks[0]

        heading = MessageHeading()

        Global_Responses_Dictionary['Message_Length'] = heading.block_or_job_length(
            _1st_block)
        Global_Responses_Dictionary['Domain_Address'] = heading.DomainAddress(
            _1st_block)
        Global_Responses_Dictionary['Site_Address'] = heading.SiteAddress(
            _1st_block)
        Global_Responses_Dictionary['Host_Address'] = heading.HostAddress(
            _1st_block)
        Global_Responses_Dictionary['Panel_Number'] = heading.PanelNumber(
            _1st_block)
        Global_Responses_Dictionary['Message_ID'] = heading.MessageID(
            _1st_block)
        Global_Responses_Dictionary['Priority'] = heading.Priority(_1st_block)
        Global_Responses_Dictionary['Checksum'] = GetCheckSum(rx_data)
        Global_Responses_Dictionary['Message_Block'] = {}

        print()

        message_block_list = []
        messages_starting_with_STX = []

        for sub_list in lists_of_blocks:
            block_str = sub_list[0]
            if (block_str[0] == 2):  # STX found
                messages_starting_with_STX.append(block_str)

        # 1. we get job codes from these msgs
        # 2. we extract the data according to job codes

        for message in messages_starting_with_STX:
            jcode = GetJobCode(message)

            if jcode is not None:
                message_block_list.append(function_per_jcode(jcode, message))
            else:
                print("Invalid data")
        # we now add the extracted data to the global dictionary
        Global_Responses_Dictionary["Message_Block"] = message_block_list
        prety = json.dumps(Global_Responses_Dictionary, indent=4)
        print(prety)
        return Global_Responses_Dictionary


def extract_to_EOT(byte_obj):
    result = []
    current_bytes = []
    for byte in byte_obj:
        if byte == 4:
            if current_bytes:
                result.append(bytes(current_bytes))
                current_bytes = []
        else:
            current_bytes.append(byte)
    if current_bytes:
        result.append(bytes(current_bytes))
    return result


def Extraction_JobCode_1_or_2(block):

    single_message = {}  # hold the data of a block found after the first STX
    msg = EventTelegram_or_CommsTest()

    year = msg.GetDateYear(block)
    month = "{:02}".format(msg.GetDateMonth(block))
    day = "{:02}".format(msg.GetDateDay(block))
    hour = "{:02}".format(msg.GetDateHour(block))
    minute = "{:02}".format(msg.GetDateMinute(block))
    second = "{:02}".format(msg.GetDateSecond(block))

    time = str(hour) + ":" + str(minute) + ":" + str(second)
    date = str(day) + "/" + str(month) + "/" + str(year)

    single_message["Job_Length"] = msg.block_or_job_length(block)
    single_message["Job_Code"] = msg.GetJobCode(block)
    single_message["Job_Status_Code"] = msg.GetStatus_Code(block)
    single_message["Panel_Number"] = msg.GetPanel_Number(block)
    single_message["Line_Code"] = msg.GetLine_Code(block)
    single_message["Device_Address"] = msg.GetDeviceAddr(block)
    single_message["Info_Code"] = msg.GetInfoCode(block)
    single_message["Super_ZOne_Code"] = msg.GetSuperZoneCode(block)
    single_message["Device_Type_Code"] = msg.GetDeviceTypeCode(block)
    single_message["Date"] = date
    single_message["Time"] = time

    if (len(block) > 32):
        text = block[33:]
        single_message["Text"] = text.decode()
    return single_message


def Extraction_JobCode_4(block_msg):
    single_message = {}
    panel_status_reply = PanelStatusReply()
    single_message["Job_Length"] = panel_status_reply.block_or_job_length(
        block_msg)
    single_message["Job_Code"] = panel_status_reply.GetJobCode(block_msg)
    single_message["Direction"] = panel_status_reply.GetDirection4(block_msg)
    single_message["Panel_Number"] = panel_status_reply.GetPanel_num4(
        block_msg)
    single_message["Line_NUmber"] = panel_status_reply.GetLine_Num4(block_msg)
    single_message["Device_Status"] = panel_status_reply.GetDeviceStatus4(
        block_msg)
    return single_message


def Extraction_JobCode_0xFF(STX_block):
    single_msg = {}
    refusejob = ExtractionOf_OXFF()
    single_msg["Job_Length"] = refusejob.block_or_job_length(STX_block)
    single_msg["Job_Code"] = refusejob.GetJobCode(STX_block)
    single_msg["Panel_Number"] = refusejob.GetPanel_Number0XFF(STX_block)
    single_msg["Refused_Job"] = refusejob.GetRefusedJOb0XFF(STX_block)
    single_msg["Reason_Code"] = refusejob.GetReasonCode0XFF(STX_block)
    single_msg["Sub_Code"] = refusejob.GetSubCode0XFF(STX_block)
    return single_msg


def function_per_jcode(code, block_msg):
    if (code == '0'):
        print("Comms test message")
        return (Extraction_JobCode_1_or_2(block_msg))

    if (code == '1'):
        print("Status events")
        return (Extraction_JobCode_1_or_2(block_msg))

    if (code == '4'):
        print("Fetch all events since last reset")
        return (Extraction_JobCode_4(block_msg))

    if (code == '0xFF'):
        print("Response to invalid Access attempt")
        return (Extraction_JobCode_0xFF(block_msg))

# non blocking keyboard


def process_input():
    if select.select([sys.stdin], [], [], 0)[0]:
        return sys.stdin.readline().strip()
    return None

def create_request():
    null = chr(0).encode().hex()
    soh  = chr(1).encode().hex()
    stx  = chr(2).encode().hex()
    etx  = chr(3).encode().hex()
    eot  = chr(4).encode().hex()
    ack  = chr(6).encode().hex()
    nack = chr(21).encode().hex()

    soh             = bytes. fromhex(soh)                                           # 1
    total_Length    = "{:04X}".format(30)                                            # 4 ASCII digits
    addr1           = "{:02X}".format(0)                                            # 2 chars/byte
    addr2           = "{:02X}".format(0)                                            # 2 chars/byte
    addr3           = "{:02X}".format(0)                                            # 2 chars/byte
    addr4           = "{:02X}".format(1)                                            # 2 chars/byte
    msgID           = "{:04X}".format(1)                                            # 4 ASCII digits
    priori          = chr(9).encode().hex().lstrip('0')                             # 1 char
    # stx             = bytes. fromhex(stx)                                           # 1
    # job_length      = "{:04X}".format(14)                                           # 4 ASCII digits
    # jcode           = 'S'                                                           # 1 char
    # panelnum        = "{:02X}".format(1)                                            # 2 chars/byte
    # acesslevel      = chr(1).encode().hex().lstrip('0')                             # 1 char
    # pword           = "{:04X}".format(2000)                                         # 4 ASCII digits
    # etx             = bytes. fromhex(etx)                                           # 1
    # crcsum          = "{:04X}".format(23560)                                        # 4 ASCII digits
    # eot             = bytes. fromhex(eot)                                           # 1

    #length was 40 here  request = soh+total_Length.encode()+addr1.encode()+addr2.encode()+addr3.encode()+addr4.encode()+msgID.encode()+priori.encode()+stx+job_length.encode()+jcode.encode()+panelnum.encode()+acesslevel.encode()+pword.encode()+etx+crcsum.encode()+eot

    stx = bytes.fromhex(stx)
    jlen = "{:04X}".format(6)
    jcode = '%'
    etx = bytes.fromhex(etx)
    crcsum = "{:04X}".format(30000)
    eot = bytes.fromhex(eot) 

    request = soh+total_Length.encode()+addr1.encode()+addr2.encode()+addr3.encode()+addr4.encode()+msgID.encode()+priori.encode()+stx+jlen.encode()+jcode.encode()+etx+crcsum.encode()+eot 
    print("request len:",len(request))

    by_4 = len(request) % 4

    if(by_4 == 1):
        # append 3 zeros
        pad          = "{:03X}".format(0)
        request = request+pad.encode()
    if(by_4 == 2):
        # append 2 zeros
        pad          = "{:02X}".format(0)
        request = request+pad.encode()
    if(by_4 == 3):
        # append 1 zeros
        pad          = "{:01X}".format(0)
        request = request+pad.encode()

    print()
    print("Here we go:",request) 
    return(request)


def main():

    # _data = b'\x0100380000000100CE3\x020020000010000000000170B1615062F\x03D2B8\x04\x0100580000000100CC3\x020020000010000000000170B1615062F\x020020000010000000000170B1615062F\x03E858\x04'
    # _data =  b'\x0100780000000100CB3\x020020000010000000000170B16150602\x020020000010000000000170B16150602\x020020000010000000000170B16150602\x03C546\x04'

    # data = b'\x0100380000000104025\x02002016E011187010000170B18050107\x038D04\x04'

    # get the data from SOH to EOT
    # if there is more than 1 then we will loop

    while (1):
        # get current time

        input = process_input()

        received_data = ser.readline()  # read lne of data from the serial

        if input is not None:
            #print('Received input of type: ', type(input))
            #hex_input = input.encode().hex()
            #ser.write(bytes.fromhex(hex_input))
            # ser.write(input.encode().hex())
            this_req = create_request()
            ser.write(this_req)

        if (len(received_data) > 0):
            # .decode().strip() #decode the received bytes and remove whitespace
            decoded_data = received_data
            print('Received of type:', type(decoded_data))

            rx_data_len = len(decoded_data)
            print('the length of the received data is', rx_data_len)
            print('rxd:', decoded_data)
            # for i in range(0,rx_data_len):

            # ser.write(bytes.fromhex(ack_msg_hex))
            # print("sent acknowlegement of type: ",type(ack_msg_hex))

            datas = extract_to_EOT(received_data)

            for data in datas:
                # match data[0]:

                # there are 3 block types
                # 1. Request/Reply
                # 2. Acknoledge
                # 3. Negative Acknolege

                if (data[0] == 1):
                    print("Message: Reply.")
                    Deal_Panel_Reply(data)
                if (data[0] == 6):
                    print("Message: Acknoledge.")
                    # Perform specific actions for option B
                if (data[0] == 21):
                    print("Message: Negative Acknolege.")
                    # Perform specific actions for option C
                else:
                    print("Message: Error. Invalid data!")


if __name__ == "__main__":
    # Call the main function
    main()
