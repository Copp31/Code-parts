int IN1 = 2; // Pompe1
int IN2 = 3; // Pompe2
int IN3 = 4; // Pompe3
int IN4 = 5; // Pompe4
int INs[] = {IN1,IN2,IN3,IN4};

int pin_ = 0; //
int Pin1 = A0; // MoistureSensor1
int Pin2 = A1; // MoistureSensor2
int Pin3 = A2; // MoistureSensor3
int Pin4 = A3; // MoistureSensor4
int Pin5 = A4; // TemperatureSensor
int Pin6 = A5; // empty

int value1 = 0;
int value2 = 0;
int value3 = 0;
int value4 = 0;
int value5 = 0;
int value6 = 0;

int saisie = 0;


void setup() {
  Serial.begin(9600);
  pinMode(Pin1, INPUT);
  pinMode(Pin2, INPUT);
  pinMode(Pin3, INPUT);
  pinMode(Pin4, INPUT);
  pinMode(Pin5, INPUT);
  pinMode(Pin6, INPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, HIGH);
  delay(500);
//  test_relay();
Serial.println("Setup end");
  delay(100);
}

void loop() {

  while (Serial.available() == 0) {
    publish_states();
    delay(100);
  }

  saisie = Serial.parseInt();
//   Serial.print("Saisie: ");
//   Serial.println(saisie);
  switch (saisie) {
    case 11:
      switchOn(IN1);
      break;
    case 21:
      switchOn(IN2);
      break;
    case 31:
      switchOn(IN3);
      break;
    case 41:
      switchOn(IN4);
      break;
    case 51:
      switchOn(IN1);
      switchOn(IN2);
      switchOn(IN3);
      switchOn(IN4);
      break;
      
    case 10:
      switchOff(IN1);
      break;
    case 20:
      switchOff(IN2);
      break;
    case 30:
      switchOff(IN3);
      break;
    case 40:
      switchOff(IN4);
      break;
    case 50:
      switchOff(IN1);
      switchOff(IN2);
      switchOff(IN3);
      switchOff(IN4);
      break;
    default:
      break;
  }
  publish_states();
}

void switchOn(int pin_) {
  digitalWrite(pin_, LOW);
}

void switchOff(int pin_) {
  digitalWrite(pin_, HIGH);
}

void publish_states() {
  //  Lecture des senseurs
  value1 = analogRead(Pin1);
  value2 = analogRead(Pin2);
  value3 = analogRead(Pin3);
  value4 = analogRead(Pin4);
  value5 = analogRead(Pin5);
  value6 = analogRead(Pin6);
  // Imprimer les valeurs des pompes (0 = OFF, 1 = ON)
  Serial.print("{'pompes':(");
  Serial.print(!digitalRead(IN1));
  Serial.print(", ");
  Serial.print(!digitalRead(IN2));
  Serial.print(", ");
  Serial.print(!digitalRead(IN3));
  Serial.print(", ");
  Serial.print(!digitalRead(IN4));
  Serial.print("), 'sensors': (");
  // Imprimer les valeurs des senseurs
  Serial.print(value1);
  Serial.print(", ");
  Serial.print(value2);
  Serial.print(", ");
  Serial.print(value3);
  Serial.print(", ");
  Serial.print(value4);
  Serial.print(", ");
  Serial.print(value5);
  Serial.print(", ");
  Serial.print(value6);
  Serial.println(")}");
}



void test_relay() {
  Serial.println("TEST POMPES START");
  digitalWrite(IN1, LOW);
  delay(300);
  digitalWrite(IN2, LOW);
  delay(300);
  digitalWrite(IN3, LOW);
  delay(300);
  digitalWrite(IN4, LOW);
  delay(600);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, HIGH);
  Serial.println("TEST POMPES FIN");
}
