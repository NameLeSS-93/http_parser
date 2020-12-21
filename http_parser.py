import socket

HOST = ''                 
PORT = 50007              


def parse_http(http):
    request, *headers, _, body = http.split('\r\n')
    method, path, protocol = request.split(' ')
    headers = dict(
        line.split(':', maxsplit=1)
        for line in headers
    )
    return method, path, protocol, headers, body
    
    
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            request = ''
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                request += data.decode('UTF-8')
        parsed_http = parse_http(request)
        
        
if __name__ == '__main__':
    main()
