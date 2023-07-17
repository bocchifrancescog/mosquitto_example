
import paho.mqtt.client as mqtt

# a callback function
def on_message_temperature(client, userdata, msg):
    # Message is an object and the payload property contains the message data which is binary data.
    # The actual message payload is a binary buffer. 
    # In order to decode this payload you need to know what type of data was sent.
    # If it is JSON formatted data then you decode it as a string and then decode the JSON string as follows:
    # decoded_message=str(message.payload.decode("utf-8")))
    # msg=json.loads(decoded_message)
    print('Received a new temperature data ', str(msg.payload.decode('utf-8')))
    print('message topic=', msg.topic)
    print('message qos=', msg.qos)


def on_message_humidity(client, userdata, msg):
    print('Received a new humidity data ', str(msg.payload.decode('utf-8')))


print('Hello')
# Give a name to this MQTT client
client = mqtt.Client('greenhouse_server')
client.message_callback_add('greenhouse/temperature', on_message_temperature)
client.message_callback_add('greenhouse/humidity', on_message_humidity)

# IP address of your MQTT broker, using ipconfig to look up it  
# client.connect('192.168.1.109', 1883)
client.connect('localhost', 20121)
# 'greenhouse/#' means subscribe all topic under greenhouse
client.subscribe('greenhouse/#')

client.loop_forever()
print('Hello')