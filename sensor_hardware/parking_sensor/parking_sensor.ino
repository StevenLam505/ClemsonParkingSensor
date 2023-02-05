
// defines pins numbers
const int trigPin = 9;
const int echoPin = 10;
// defines variables
long duration;
int distance, hour, delay2, count;
char received_str[3];
char data;
bool occupied = false;

void setup() {
  hour = 0;
  delay2 = 1;
  count = 0;
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600); // Starts the serial communication
}

void loop() {
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2;
  // Prints the distance on the Serial Monitor
  //Serial.print("Distance: ");
  //Serial.print(distance);
  //Serial.print("\tOccupied?: ");
  Serial.print(occupied);

  delay((unsigned long)1000*delay2); // delay for 1*delay2 seconds

  if(Serial.available() > 0) {
		data = Serial.read();
		received_str[0] = data;
    data = Serial.read();
    received_str[1] = data;
		received_str[2] = '\0';
		//Serial.print("received:");
    //Serial.println(received_str);
	}

  hour = atoi(received_str);  
  if(hour == 0)
    hour = 10;
  if(7 < hour && hour < 19)
    delay2 = 1;
  else
    delay2 = 1;

  if(distance <= 120)
    occupied = true;
  else
    occupied = false;
}