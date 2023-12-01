String GetData() {
  return Serial.readStringUntil('\n');
}

String ProcessData(String data){
    return "Arduino recieved " + data + " and transmitted this message\n";
}

void SendData(String data) {
  Serial.print(data);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  String data = GetData();
  String processedData = ProcessData(data);
  SendData(processedData);
}
