import logging
import json
import StatusCodes

logging.basicConfig(filename="test.txt", 
					format='%(asctime)s %(message)s', 
					filemode='w') 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 
                 
logger.debug('                       log the bytes:')

Global_Responses_Dictionary = {}
                
class MessageHeading():

    def block_or_job_length(self, first_list):
        _block = first_list[0].decode()
        the_byte = _block[1:5]
        return int(the_byte, 16)  
          
    def DomainAddress(self, first_list):
        first_list_decoded = first_list[0].decode()
        the_byte = first_list_decoded[5:7]
        return int(the_byte, 16)
        
    def SiteAddress(self, first_list):
        first_list_decoded = first_list[0].decode()
        the_byte = first_list_decoded[7:9]
        return int(the_byte, 16)

    def HostAddress(self, first_list):
        first_list_decoded = first_list[0].decode()
        the_byte = first_list_decoded[9:11]
        return int(the_byte, 16)
        
    def PanelNumber(self, first_list):
        first_list_decoded = first_list[0].decode()
        the_byte = first_list_decoded[11:13]
        return int(the_byte, 16)        
    
    def MessageID(self,first_list):
        first_list_decoded = first_list[0].decode()        
        the_byte = first_list_decoded[13:17]       
        return int(the_byte, 16)            

    def Priority(self, first_list):
        first_list_decoded = first_list[0].decode()
        the_byte = first_list_decoded[17]
        return the_byte  

class EventTelegram_or_CommsTest():
    
    def GetJobCode(self, n_list):
        _block = n_list.decode()
        the_byte = _block[5]
        return the_byte 

    def GetStatus_Code(self, n_list):
        first_list_decoded = n_list.decode()
        the_byte = first_list_decoded[6:8]
        return int(the_byte, 16)

    def GetPanel_Number(self, n_list):
        first_list_decoded = n_list.decode()
        the_byte = first_list_decoded[8:10]
        return int(the_byte, 16)

    def GetLine_Code(self, n_list):
        first_list_decoded = n_list.decode()
        the_byte = first_list_decoded[10:12]
        return int(the_byte, 16)

    def GetDeviceAddr(self, n_list):
        first_list_decoded = n_list.decode()
        the_byte = first_list_decoded[12:14]
        return int(the_byte, 16)

    def GetInfoCode(self, n_list):
        first_list_decoded = n_list.decode()
        the_byte = first_list_decoded[14:16]
        return int(the_byte, 16)

    def GetSuperZoneCode(self, n_list):
        first_list_decoded = n_list.decode()
        the_byte = first_list_decoded[16:18]
        return int(the_byte, 16)

    def GetDeviceTypeCode(self, n_list):
        first_list_decoded = n_list.decode()
        the_byte = first_list_decoded[18:20]
        return int(the_byte, 16)

    def GetDateYear(self, n_list):
        first_list_decoded = n_list.decode()
        the_byte = first_list_decoded[20:22]
        return int(the_byte, 16)

    def GetDateMonth(self, n_list):
        first_list_decoded = n_list.decode()
        the_byte = first_list_decoded[22:24]
        return int(the_byte, 16)

    def GetDateDay(self, n_list):
        first_list_decoded = n_list.decode()
        the_byte = first_list_decoded[24:26]
        return int(the_byte, 16)

    def GetDateHour(self, n_list):
        first_list_decoded = n_list.decode()
        the_byte = first_list_decoded[26:28]
        return int(the_byte, 16)

    def GetDateMinute(self, n_list):
        first_list_decoded = n_list.decode()
        the_byte = first_list_decoded[28:30]
        return int(the_byte, 16)

    def GetDateSecond(self, n_list):
        first_list_decoded = n_list.decode()
        the_byte = first_list_decoded[30:32]
        return int(the_byte, 16)

class PanelStatusReply():
    
    def GetJobCode(self, msg_block):
        _block = msg_block.decode()
        the_byte = _block[5]
        return the_byte 
        
    def GetDirection4(self, msg_block):
        _block = msg_block.decode()
        the_byte = _block[6]
        return the_byte     

    def GetPanel_num4(self, msg_block):
        first_list_decoded = msg_block.decode()
        the_byte = first_list_decoded[7:9]
        return int(the_byte, 16)

    def GetLine_Num4(self, msg_block):
        first_list_decoded = msg_block.decode()
        the_byte = first_list_decoded[9:11]
        return int(the_byte, 16)
        
    def GetDeviceStatus4(self, msg_block):
        print("untested")
        decoded_msg = msg_block.decode()
        struct = decoded_msg[11:]
        #convert each byte to ASCII-HEX
        struct_msg = self.byte_to_ascii_hex4(struct)
        return struct_msg
        
    def byte_to_ascii_hex4(self,byte_obj):
        hex_list = []
        for byte in byte_obj:
            hex_str = hex(byte)[2:].zfill(2)
            hex_list.append(hex_str)
        return hex_list
        
        
class ExtractionOf_OXFF():
    
    def GetJobCode(self, msg):
        _block = msg.decode()
        the_byte = _block[5]
        return the_byte 

    def GetPanel_Number0XFF(self, msg):
        msg_decoded = msg.decode()
        the_byte = msg_decoded[6:8]
        return int(the_byte, 16)

    def GetRefusedJOb0XFF(self, msg):
        msg_decoded = msg.decode()
        the_byte = msg_decoded[8]
        return the_byte
        
    def GetReasonCode0XFF(self, msg):
        msg_decoded = msg.decode()
        the_byte = msg_decoded[9:11]    
        return self.Reasonforrefusal0XFF(int(the_byte, 16))

    def GetSubCode0XFF(self, msg):
        msg_decoded = msg.decode()
        the_byte = msg_decoded[11:13]    
        return self.RefusalSubCode0XFF(int(the_byte, 16))

    def Reasonforrefusal0XFF(self, code):
        match code:
            case 0:
                return("Code 0: System Busy")
            case 1:
                return("Code 1: Invalid Job / Prohibited Job")
            case 4:
                return("Code 4: Access denied. Invalid access code")
            case 7:
                return("Code 7: Requested Node offline")
            case 8:
                return("Code 8: Requested Node unavailable")
            case _:
                return("Unknown")

    def RefusalSubCode0XFF(self, sub_Code):
        match sub_Code:
            case 0:
                return("Sub_Code 0 - Comms Failed: Panel unavailable")
            case 1:
                return("Sub_Code 1 - Comms Failed: Timed out")
            case 2:
                return("Sub_Code 2 - Comms Failed: Panel offline")
            case _:
                return("Unknown")
            
def find_markers(rx_data):
    markers=[]

    # Iterate through the string
    for i in range(len(rx_data)):
        # Check if the current character is the STX ASCII code
        logger.debug("                       %s:%s",i,rx_data[i])
        if rx_data[i] == 1:
            #SOH found
            logger.debug("                       SOH found at index:%s", i)
            markers.append(i)
        if rx_data[i] == 2:
            # STX found, print the index
            logger.debug("                       STX found at index:%s", i)
            markers.append(i)
        if rx_data[i] == 3:
            #ETX found
            logger.debug("                       ETX found at index:%s", i)
            markers.append(i)        
        if rx_data[i] == 4:
            #EOT found
            logger.debug("                       EOT found at index:%s", i)
            markers.append(i)        
        if rx_data[i] == 6:
            #ACK found
            logger.debug("                       ACK found at index:%s", i)
            markers.append(i)        
        if rx_data[i] == 21:
            #NCK found
            logger.debug("                       NCK found at index:%s", i)        
            markers.append(i)

    logger.debug(markers)
    return markers

def extract_between_markers(rx_data, position_of_markers_list):
    
    list_of_lists = []
    
    #create a list of lists. each list will contain the byte strings between 2 markers
    for marker in range(len(position_of_markers_list)-1):
        data_string_list = []  
        list_of_lists.append(data_string_list)
    
    #extract the byte strings between markers
    for i in range(len(position_of_markers_list)-1):
        list_of_lists[i].append(rx_data[position_of_markers_list[i]:position_of_markers_list[i+1]])
        
    # # Print the arrays
    for i, arr in enumerate(list_of_lists):
        print(f"Array {i+1}: {arr}")
        
    return list_of_lists

def block_or_job_length2(msg):
    _block = msg.decode()
    the_byte = _block[1:5]
    return int(the_byte, 16)  

def GetCheckSum(rx_data):  
    etx_index=0
    eot_index=0
    for i in range(len(rx_data)):
        if rx_data[i] == 3: #ETX found
            etx_index = i
        if rx_data[i] == 4: #EOT found
            eot_index = i
        
        checksum_data = rx_data[etx_index+1:eot_index]
    if(eot_index==0 or etx_index==0):
        return 0
    else:
        return (int(checksum_data,16))
        #return checksum_data #return the bytes so long until we can calculate the actual crc of rx data
            
def R_R_JobCode(block_s_with_stx):
    #get jobcode for fi
    _block = block_s_with_stx.decode()
    the_byte = _block[5]
    print("the returning job code:" ,the_byte) 
    return the_byte                                                   

def Request_or_Reply(rx_data):

    if(rx_data[18] != 2):
        return None    #invalid data
    else:
            
        markers              = find_markers(rx_data)    
        lists_of_blocks      = []
        lists_of_blocks      = extract_between_markers(rx_data, markers)
        _1st_block           = lists_of_blocks[0]
        
        heading              = MessageHeading()    
        
        Global_Responses_Dictionary['Message_Length'] = heading.block_or_job_length(_1st_block)
        Global_Responses_Dictionary['Domain_Address'] = heading.DomainAddress(_1st_block)
        Global_Responses_Dictionary['Site_Address']   = heading.SiteAddress(_1st_block)
        Global_Responses_Dictionary['Host_Address']   = heading.HostAddress(_1st_block)
        Global_Responses_Dictionary['Panel_Number']   = heading.PanelNumber(_1st_block)
        Global_Responses_Dictionary['Message_ID']     = heading.MessageID(_1st_block)
        Global_Responses_Dictionary['Priority']       = heading.Priority(_1st_block)
        Global_Responses_Dictionary['Checksum']       = GetCheckSum(rx_data)
        Global_Responses_Dictionary['Message_Block']  = {}

        print()
        
        message_block_list = []
        messages_starting_with_STX = []
        
        for sub_list in lists_of_blocks:
            block_str = sub_list[0]
            if(block_str[0] == 2): # STX found
                messages_starting_with_STX.append(block_str)
                
        # 1. we get job codes from these msgs
        # 2. we extract the data according to job codes
        
        for message in messages_starting_with_STX:
            jcode = R_R_JobCode(message)

            if jcode != None:
                message_block_list.append(function_per_jcode(jcode,message))
            else:
                print("Invalid data")
        #we now add the extracted data to the global dictionary
        Global_Responses_Dictionary["Message_Block"] = message_block_list
        prety = json.dumps(Global_Responses_Dictionary, indent = 4)
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

def jobcode_1_or_2_extraction(block):
        
    single_message = {} #hold the data of a block found after the first STX
    event_or_test_msg = EventTelegram_or_CommsTest()
    
    year                 = event_or_test_msg.GetDateYear(block)
    month                = "{:02}".format(event_or_test_msg.GetDateMonth(block))
    day                  = "{:02}".format(event_or_test_msg.GetDateDay(block))
    hour                 = "{:02}".format(event_or_test_msg.GetDateHour(block))
    minute               = "{:02}".format(event_or_test_msg.GetDateMinute(block))
    second               = "{:02}".format(event_or_test_msg.GetDateSecond(block))
    
    time = str(hour)+":"+str(minute)+":"+str(second)
    date = str(day)+"/"+str(month)+"/"+str(year)
    
    single_message["Job_Length"]              = block_or_job_length2(block)
    single_message["Job_Code"]                = event_or_test_msg.GetJobCode(block)
    single_message["Job_Status_Code"]         = event_or_test_msg.GetStatus_Code(block)
    single_message["Panel_Number"]            = event_or_test_msg.GetPanel_Number(block)
    single_message["Line_Code"]               = event_or_test_msg.GetLine_Code(block)
    single_message["Device_Address"]          = event_or_test_msg.GetDeviceAddr(block)
    single_message["Info_Code"]               = event_or_test_msg.GetInfoCode(block)
    single_message["Super_ZOne_Code"]         = event_or_test_msg.GetSuperZoneCode(block)
    single_message["Device_Type_Code"]        = event_or_test_msg.GetDeviceTypeCode(block)
    single_message["Date"]                    = date
    single_message["Time"]                    = time
      
    if(len(block)>32):
        text = block[33:]
        single_message["Text"]                = text.decode()
    return single_message

def jobcode_4_extraction(block_msg):
    single_message = {}
    panel_status_reply = PanelStatusReply()
    single_message["Job_Length"]              = block_or_job_length2(block_msg)
    single_message["Job_Code"]                = panel_status_reply.GetJobCode(block_msg)
    single_message["Direction"]               = panel_status_reply.GetDirection4(block_msg)
    single_message["Panel_Number"]            = panel_status_reply.GetPanel_num4(block_msg)
    single_message["Line_NUmber"]             = panel_status_reply.GetLine_Num4(block_msg)
    single_message["Device_Status"]           = panel_status_reply.GetDeviceStatus4(block_msg)    
    return single_message
            
def jobcode_0xFF_extraction(msg_block):
    single_msg = {}
    refusejob = ExtractionOf_OXFF()
    single_msg["Job_Length"]                 = block_or_job_length2(msg_block)
    single_msg["Job_Code"]                   = refusejob.GetJobCode(msg_block)
    single_msg["Panel_Number"]               = refusejob.GetPanel_Number0XFF(msg_block)
    single_msg["Refused_Job"]                = refusejob.GetRefusedJOb0XFF(msg_block)
    single_msg["Reason_Code"]                = refusejob.GetReasonCode0XFF(msg_block)
    single_msg["Sub_Code"]                   = refusejob.GetSubCode0XFF(msg_block)
    return single_msg
    
def function_per_jcode(code, block_msg):
    match code:
        case '0':
            print("Comms test message")
            return(jobcode_1_or_2_extraction(block_msg))
            
        case '1':
            print("Status events")
            return(jobcode_1_or_2_extraction(block_msg))
            
        case '4':
            print("Fetch all events since last reset")
            return(jobcode_4_extraction(block_msg))
        
        case '0xFF':
            print("Response to invalid Access attempt")
            return(jobcode_0xFF_extraction(block_msg))

def main():
        
    #_data = b'\x0100380000000100CE3\x020020000010000000000170B1615062F\x03D2B8\x04\x0100580000000100CC3\x020020000010000000000170B1615062F\x020020000010000000000170B1615062F\x03E858\x04'
    #_data =  b'\x0100780000000100CB3\x020020000010000000000170B16150602\x020020000010000000000170B16150602\x020020000010000000000170B16150602\x03C546\x04'

    data = b'\x0100380000000104025\x02002016E011187010000170B18050107\x038D04\x04'

    # get the data from SOH to EOT
    # if there is more than 1 then we will loop
    
    datas = extract_to_EOT(data)
    
    for data in datas:
        match data[0]: 
            
            #there are 3 block types 
            # 1. Request/Reply
            # 2. Acknoledge
            # 3. Negative Acknolege

            case 1:
                print("Message: Request/Reply.")
                Request_or_Reply(data) # must return job code
            case 6:
                print("Message: Acknoledge.")
                # Perform specific actions for option B
            case 21:
                print("Message: Negative Acknolege.")
                # Perform specific actions for option C
            case _:
                print("Message: Error. Invalid data!")
       
if __name__ == "__main__":
    # Call the main function
    main()

