from flask import Flask, render_template
import serial
app = Flask(__name__)
ser = serial.Serial(port='COM3',baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

message= []
@app.route('/')
def index():
    led_off()
    return render_template('index.html', state='OFF')

@app.route('/on/')
def on():
    print ('Switch On')
    message = ''.join(['\x02','on','\x03'])
    ser.write(bytes(message.encode()))
    return render_template('index.html', state='ON')

@app.route('/off/')
def off():
    print ('Switch Off')
    message = ''.join(['\x02','off', '\x03'])
    ser.write(bytes(message.encode()))
    return render_template('index.html', state='OFF')

if __name__=='__main__':
    print('Web Server Starts')
    app.run(debug=True, host='localhost', port=8100)
    print ('Web Server Ends')
