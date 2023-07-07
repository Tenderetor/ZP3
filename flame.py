import logging
import json

logging.basicConfig(filename="test.txt", 
					format='%(asctime)s %(message)s', 
					filemode='w') 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 
                 
logger.debug('                       log the bytes:')

Global_Responses_Dictionary = {}
                
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

def block_or_job_length(first_list):
    _block = first_list[0].decode()
    the_byte = _block[1:5]
    return int(the_byte, 16)  

class FirstDelimitedData():
          
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

#count the frequency of a val
def count_occurance(rx_data, val):
    val_count = 0
    for byte in rx_data:
        if byte == val:
            val_count += 1

    print("STX count:", val_count)
    return val_count    

def GetJobCode(n_list):
    _block = n_list[0].decode()
    the_byte = _block[5]
    return the_byte 

def GetStatus_Code(n_list):
    first_list_decoded = n_list[0].decode()
    the_byte = first_list_decoded[6:8]
    return int(the_byte, 16)

def GetPanel_Number(n_list):
    first_list_decoded = n_list[0].decode()
    the_byte = first_list_decoded[8:10]
    return int(the_byte, 16)

def GetLine_Code(n_list):
    first_list_decoded = n_list[0].decode()
    the_byte = first_list_decoded[10:12]
    return int(the_byte, 16)

def GetDeviceAddr(n_list):
    first_list_decoded = n_list[0].decode()
    the_byte = first_list_decoded[12:14]
    return int(the_byte, 16)

def GetInfoCode(n_list):
    first_list_decoded = n_list[0].decode()
    the_byte = first_list_decoded[14:16]
    return int(the_byte, 16)

def GetSuperZoneCode(n_list):
    first_list_decoded = n_list[0].decode()
    the_byte = first_list_decoded[16:18]
    return int(the_byte, 16)

def GetDeviceTypeCode(n_list):
    first_list_decoded = n_list[0].decode()
    the_byte = first_list_decoded[18:20]
    return int(the_byte, 16)

def GetDateYear(n_list):
    first_list_decoded = n_list[0].decode()
    the_byte = first_list_decoded[20:22]
    return int(the_byte, 16)

def GetDateMonth(n_list):
    first_list_decoded = n_list[0].decode()
    the_byte = first_list_decoded[22:24]
    return int(the_byte, 16)

def GetDateDay(n_list):
    first_list_decoded = n_list[0].decode()
    the_byte = first_list_decoded[24:26]
    return int(the_byte, 16)

def GetDateHour(n_list):
    first_list_decoded = n_list[0].decode()
    the_byte = first_list_decoded[26:28]
    return int(the_byte, 16)

def GetDateMinute(n_list):
    first_list_decoded = n_list[0].decode()
    the_byte = first_list_decoded[28:30]
    return int(the_byte, 16)

def GetDateSecond(n_list):
    first_list_decoded = n_list[0].decode()
    the_byte = first_list_decoded[30:32]
    return int(the_byte, 16)

def Deal(block):
    
    single_message = {} #hold the data of a block found after the first STX
        
    year                 = GetDateYear(block)
    month                = "{:02}".format(GetDateMonth(block))
    day                  = "{:02}".format(GetDateDay(block))
    hour                 = "{:02}".format(GetDateHour(block))
    minute               = "{:02}".format(GetDateMinute(block))
    second               = "{:02}".format(GetDateSecond(block))
    
    time = str(hour)+":"+str(minute)+":"+str(second)
    date = str(day)+"/"+str(month)+"/"+str(year)
    
    single_message["Job_Length"]              = block_or_job_length(block)
    single_message["Job_Code"]                = GetJobCode(block)
    single_message["Job_Status_Code"]         = GetStatus_Code(block)
    single_message["Panel_Number"]            = GetPanel_Number(block)
    single_message["Line_Code"]               = GetLine_Code(block)
    single_message["Device_Address"]          = GetDeviceAddr(block)
    single_message["Info_Code"]               = GetInfoCode(block)
    single_message["Super_ZOne_Code"]         = GetSuperZoneCode(block)
    single_message["Device_Type_Code"]        = GetDeviceTypeCode(block)
    single_message["Date"]                    = date
    single_message["Time"]                    = time
        
    
    # match job_code:
    #     case '0':
    #         print("Comms Test Message")
    #     case '1':
    #         print("Status Events Message")
    #     case '4':
    #         print("Panel Status Request/Reply") #fetch all events since last reset
    #     case '0xFF':
    #         print("Refuse Job") #Response to invalid access attempt
        
    #return an object with a block's extracted data 
    return single_message

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
            
            
                                              
def Request_or_Reply(rx_data):
    
    markers              = find_markers(rx_data)    
    lists_of_blocks      = []
    lists_of_blocks      = extract_between_markers(rx_data, markers)
    _1st_block           = lists_of_blocks[0]
    
    leading_data         = FirstDelimitedData()    
 
    
    Global_Responses_Dictionary['Message_Length'] = block_or_job_length(_1st_block)
    Global_Responses_Dictionary['Domain_Address'] = leading_data.DomainAddress(_1st_block)
    Global_Responses_Dictionary['Site_Address']   = leading_data.SiteAddress(_1st_block)
    Global_Responses_Dictionary['Host_Address']   = leading_data.HostAddress(_1st_block)
    Global_Responses_Dictionary['Panel_Number']   = leading_data.PanelNumber(_1st_block)
    Global_Responses_Dictionary['Message_ID']     = leading_data.MessageID(_1st_block)
    Global_Responses_Dictionary['Priority']       = leading_data.Priority(_1st_block)
    Global_Responses_Dictionary['Checksum']       = GetCheckSum(rx_data)
    Global_Responses_Dictionary['Message_Block']  = {}
 
    print()
    
    message_block_list = []
    # deal with strings which have "STX"
    #Since the lists inside the list have only single elements. we will just access them directly 
    for sub_list in lists_of_blocks:
        block_str = sub_list[0]
        if(block_str[0]==2):
            # print("STX FOUND")
            next_block = []
            next_block.append(block_str)
            # print(next_block)
            message_block_list.append(Deal(next_block))
    Global_Responses_Dictionary["Message_Block"] = message_block_list
    prety = json.dumps(Global_Responses_Dictionary, indent = 4)
    print(prety)
            
def main():
        
    _data = b'\x0100380000000100CE3\x020020000010000000000170B1615062F\x03D2B8\x04\x0100580000000100CC3\x020020000010000000000170B1615062F\x020020000010000000000170B1615062F\x03E858\x04'
    #_data =  b'\x0100780000000100CB3\x020020000010000000000170B16150602\x020020000010000000000170B16150602\x020020000010000000000170B16150602\x03C546\x04'

    match _data[0]: 
        
        #there are 3 block types 
        # 1. Request/Reply
        # 2. Acknoledge
        # 3. Negative Acknolege

        case 1:
            print("Message: Request/Reply.")
            Request_or_Reply(_data)
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

