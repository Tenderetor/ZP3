import logging

logging.basicConfig(filename="test.txt", 
					format='%(asctime)s %(message)s', 
					filemode='w') 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 
                 
logger.debug('                       log the bytes:')

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
    # for i, arr in enumerate(list_of_lists):
    #     print(f"Array {i+1}: {arr}")
        
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

def JobCode(n_list):
    _block = n_list[0].decode()
    the_byte = _block[5]
    return the_byte 

def Status_Code(n_list):
    first_list_decoded = n_list[0].decode()
    the_byte = first_list_decoded[5:7]
    return int(the_byte, 16)
    
def Deal(block):
    job_len              = block_or_job_length(block)
    # print("Job length:",job_len)
    
    job_code             = JobCode(block)
    # print("job code:",job_code)

    match job_code:
        case '0':
            print("Comms Test Message")
            print("Status code:",Status_Code(block))
        case '1':
            print("Status Events Message")
        case '4':
            print("Panel Status Request/Reply") #fetch all events since last reset
        case '0xFF':
            print("Refuse Job") #Response to invalid access attempt
                                          
def Request_or_Reply(rx_data):
    
    markers              = find_markers(rx_data)    
    lists_of_blocks      = []
    lists_of_blocks      = extract_between_markers(rx_data, markers)
    _1st_block           = lists_of_blocks[0]
    
    leading_data         = FirstDelimitedData()
    
    msg_len              = block_or_job_length(_1st_block)
    
    #Get the Address and panel number
    domain_addr          = leading_data.DomainAddress(_1st_block)
    site_addr            = leading_data.SiteAddress(_1st_block)
    host_addr            = leading_data.HostAddress(_1st_block)
    panel_num            = leading_data.PanelNumber(_1st_block)
    msg_id               = leading_data.MessageID(_1st_block)
    priority_            = leading_data.Priority(_1st_block)
    
    print("Msg len is:{}".format(msg_len))
    print("Message ID is:{}".format(msg_id))
    print("The IP address is:{}.{}.{}.{}".format(domain_addr, site_addr, host_addr, panel_num))
    print("Message prioroty is:{}".format(priority_))
    
    # stx_cntr = count_occurance(rx_data, 2)
    # print(stx_cntr)
    print()
    
    # deal with strings which have "STX"
    #Since the lists inside the list have only single elements. we will just access them directly 
    for sub_list in lists_of_blocks:
        block_str = sub_list[0]
        if(block_str[0]==2):
            # print("STX FOUND")
            next_block = []
            next_block.append(block_str)
            # print(next_block)
            Deal(next_block)
 
            
def main():
        
    #_data = b'\x0100380000000100CE3\x020020000010000000000170B1615062F\x03D2B8\x04\x0100580000000100CC3\x020020000010000000000170B1615062F\x020020000010000000000170B1615062F\x03E858\x04'
    _data =  b'\x0100780000000100CB3\x020020000010000000000170B16150602\x020020000010000000000170B16150602\x020020000010000000000170B16150602\x03C546\x04'


    
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
