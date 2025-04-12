#define out_5v 2 
#define in_5v 3 
#define CHRG 4 
#define STBY 6
#define Led_Pin 5
#define batt_pin A0

void setup() {

pinMode(Led_Pin, OUTPUT);
pinMode(out_5v, INPUT);
pinMode(in_5v, INPUT);
pinMode(CHRG, INPUT);
pinMode(STBY, INPUT);
pinMode(batt_pin, INPUT);

Serial.begin(9600);
//Serial.print("OK!");

}

void smooth_light() {
  for (int i = 0; i < 255; i++) {
    analogWrite(Led_Pin, i);
    delay(5);
  }
  for (int i = 255; i >= 0; i--) {
   analogWrite(Led_Pin, i);
    delay(5);
  }
}

void loop() {

  float batt_voltage = analogRead(batt_pin) * (3.3 / 1023.0) * 2;  // делитель 1:1
  //float batt_voltage = 3.4;
  bool Sys_Active = digitalRead(out_5v);
  //bool Sys_Active = 0;
  bool Ext_power = digitalRead(in_5v);
  //bool Ext_power = 1;
  bool Charging_process = !digitalRead(CHRG);  // CRG активен по низкому уровню
  //bool Charging_process = 1;
  bool Charge_finish = !digitalRead(STBY);
  //bool Charge_finish = 0;

  if (Sys_Active) {
  Serial.print(batt_voltage);
  Serial.print(", ");
  Serial.print(Sys_Active);
  Serial.print(", ");
  Serial.print(Ext_power);
  Serial.print(", ");
  Serial.print(Charging_process);
  Serial.print(", ");
  Serial.print(Charge_finish);
  Serial.println("\n");

 delay(1000);
  }

 if (Ext_power && Charging_process && !Charge_finish && !Sys_Active){
    //Serial.println("Charging");
    smooth_light();

 } else if(Ext_power && !Charging_process && Charge_finish && !Sys_Active){
    //Serial.println("Charging finish");
    analogWrite(Led_Pin, 25);
} 

 if (Sys_Active && batt_voltage > 3.3){
    //Serial.println("SYS ON");
    analogWrite(Led_Pin, 255);

 } else if (Sys_Active && batt_voltage <= 3.3 and batt_voltage > 3.0){
    //Serial.println("Batt is 3.3");
    analogWrite(Led_Pin, 255);
    delay(300);
    analogWrite(Led_Pin, 0);

 } else if (Sys_Active && batt_voltage <= 3.0){
    //Serial.println("batt is 3.0");
    analogWrite(Led_Pin, 255);
    delay(50);
    analogWrite(Led_Pin, 0);
    
 } else if(!Sys_Active && !Ext_power){
    //Serial.println("SYS OFF");
    analogWrite(Led_Pin, 0);
}
//smooth_light();
}