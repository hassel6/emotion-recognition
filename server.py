import socket

#recieved = False

emotions = [ 'KIZGIN', 'TIKSINMIS', 'KORKMUS', 'MUTLU', 'UZGUN', 'SASKIN', 'NOTR' ]

def Main():
   
    recieved = False
    host = '192.168.1.2' # Server ip
    port = 4000
    
    client1 = ( host, port )
    
    s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    s.bind( client1 )

    print( "Server Started" )        
    
    while True:
                                                   
        if recieved == False:            
            sendingData = input( '-> ' )           
            if sendingData == 'checkemo':
                s.sendto( sendingData.encode('utf-8'), client1 )
                recieved = True
         
        data, addr = s.recvfrom( 1024 )
        data = data.decode( 'utf-8' )       
         
        if 'pre-' in data:
            data = data[ 3: ].split( '-' )
            data = data[ 0 ].astype( int )
            print( emotions[ data ] )
            recieved = False                
        
       
    s.close()

if __name__=='__main__':
    Main()