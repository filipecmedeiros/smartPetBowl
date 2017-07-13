#include <Servo.h>
#include <SPI.h>
#include <Ethernet.h>

//define
#define SENSOR_1 4 // ração
#define SENSOR_2 5 // ração
#define SENSOR_3 6 // ração
#define SENSOR_4 7 // ração
#define SENSOR_5 8 // presença
#define ENTRADA_PWM 9 //servo (pwm)

//variaveis globais
Servo servo_pote; //Servo instalado no pote
int sensor1 = 0, sensor2 = 0, sensor3 = 0, sensor4 = 0, sensor5 = 0; //Leitura dos sensores
String readString;

//Informacoes de endereco IP, gateway, mascara de rede
byte mac[] = { 0xA4, 0x28, 0x72, 0xCA, 0x55, 0x2F };
byte ip[] = { 192, 168, 0, 160 };
byte gateway[] = { 192, 168, 0, 1 };
byte subnet[] = { 255, 255, 255, 0 };
EthernetServer server(80);

void setup() {
  //Servo
  servo_pote.attach(ENTRADA_PWM);  // Pino 9 (PWM) destinado ao servo
  servo_pote.write(0); //Posição inicial do servo

  //Sensores
  pinMode(SENSOR_1,INPUT); //seta sensores
  pinMode(SENSOR_2,INPUT);
  pinMode(SENSOR_3,INPUT);
  pinMode(SENSOR_4,INPUT);
  pinMode(SENSOR_5,INPUT);
  
  //Inicializa Ethernet Shield
  Ethernet.begin(mac, ip, gateway, subnet);
  server.begin();
  
  delay(2000);
}

//Rotina de acionamento do servo
void aciona_servo(boolean turn){
  if(turn){
    //Rotaciona o pote     
      servo_pote.write(45);
      delay(2000);
      //Para a rotação    
      servo_pote.write(0);
      delay(2000);
  }else{
    //Para a rotação
    servo_pote.write(0);
  }
}

//Rotina do monitoramento de status dos sensores
void sensors_to_servo(){
  int r[5],i;
  r[0] = digitalRead(SENSOR_1);
  r[1] = digitalRead(SENSOR_2);
  r[2] = digitalRead(SENSOR_3);
  r[3] = digitalRead(SENSOR_4);
  r[4] = digitalRead(SENSOR_5);

  for(i=0; i<5; i++){
    if(r[i] = HIGH) aciona_servo(true);
    else aciona_servo(false);
  }
  
}

//Comunicação com Website do SmartPetBowl
void web_client_ethernetShield(){
  EthernetClient client = server.available();
  if (client) {
    while (client.connected())
    {
      if (client.available())
      {
        char c = client.read();
        if (readString.length() < 100) {
          readString += c;
        }
        if (c == '\n')
        {
          //Controle do servo motor do pote
          if (readString.indexOf("?abrir") > 0) aciona_servo(true); //Liga o servo
          
          readString = "";
          
          delay(1);
          client.stop();
        }
      }
    }
  }
}

void loop() {
  //verifica se algum dado foi recebido
  web_client_ethernetShield();
  delay(1000);
  //verifica sensores
  sensors_to_servo();
  delay(1000);
}
