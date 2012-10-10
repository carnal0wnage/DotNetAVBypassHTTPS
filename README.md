### Added after Fork ####
Alphanumeric payload is now downloaded over HTTPS, you'll have to modify the source code with the URL of your server e.g. https://www.google.com.

httshellcode.py is a payload generation script using msfpayload and msfencode, once it has generated a payload it will host it over a HTTPS server. You'll need a .pem file.
python httpshellcode.py -h
usage: httpshellcode.py [-h] --cert CERT --payload PAYLOAD --lhost LHOST
                        --lport LPORT [--msfroot MSFROOT]

optional arguments:
  -h, --help         show this help message and exit
  --cert CERT        pem location
  --payload PAYLOAD  msf payload
  --lhost LHOST      Connectback IP
  --lport LPORT      Connectback Port
  --msfroot MSFROOT

### ORIGINAL WORK BY Matt Andreko ####
### DotNetAVBypassHTTPS
This application was written in an attempt to be able to use penetration testing tools in an environment where Antivirus Systems may pick up your tools/payloads.  The Proof of Concept included, runs a Metasploit Meterpreter payload on the remote host, in a hidden window (can be called from the command line).

This solution was made with Visual Studio 2010, but should compile on anything as low as 2005 at least.  There are no special "unsafe" flags or anything required.  

### Original Blog Post By Matt
http://www.mattandreko.com/2012/02/using-net-to-bypass-av.html