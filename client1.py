from funcRecognizeEmotion import emo
import numpy as np

import sys
import socket
from socket import AF_INET, SOCK_DGRAM

def Main():

    host='192.168.1.3' # Client ip
    #host='192.168.1.7' # Client ip
    port = 4000
    
    server = ( '192.168.1.4', 4000 )
    
    s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    s.bind( ( host, port ) )
    
    
    while True:
        data, addr = s.recvfrom( 1024 )
        data = data.decode('utf-8')
        
        emotionData = []
        
        if data == "checkemo":
            emotionData = emo.fRecognize( duration=6 ) # 2 saniye analiz
        
            # Değeri En Çok Olan 2 Duygu Server e Gönderilecek
            maxIdx = np.argsort( emotionData )[ -2: ]
            #maxIndexes = maxIndexes[ -2: ]
            
            msgIdx = 'pre-' + maxIdx[ 1 ].astype( 'str' ) + '-' + maxIdx[ 0 ].astype( 'str' )
            
            s.sendto( msgIdx.encode( 'utf-8' ), server )
            print( 'Send to : ', msgIdx )
    
    s.close()
    

if __name__=='__main__':
    Main()