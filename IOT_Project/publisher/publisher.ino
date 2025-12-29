#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

/* ---------- WIFI CONFIG ---------- */
const char* ssid = "Shravani 2";
const char* password = "Shravni@8046";

/* ---------- MQTT CONFIG ---------- */
const char* mqtt_server = "broker.hivemq.com";
const char* topic = "environment/data";

/* ---------- SENSOR CONFIG ---------- */
#define DHTPIN 4
#define DHTTYPE DHT11
#define MQ2_PIN 34

DHT dht(DHTPIN, DHTTYPE);

WiFiClient espClient;
PubSubClient client(espClient);

/* ---------- WIFI CONNECT ---------- */
void setup_wifi() {
  Serial.print("Connecting to WiFi");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi Connected");
}

/* ---------- MQTT CONNECT ---------- */
void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP32_ENV_PUBLISHER")) {
      Serial.println("Connected");
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();

  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  float temperature = dht.readTemperature();   // °C
  float humidity = dht.readHumidity();         // %
  int gas = analogRead(MQ2_PIN);               // MQ-2 raw value

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor");
    delay(2000);
    return;
  }

  char payload[120];
  snprintf(payload, sizeof(payload),
           "{\"temperature\":%.2f,\"humidity\":%.2f,\"gas\":%d}",
           temperature, humidity, gas);

  client.publish(topic, payload);
  Serial.println("Published: ");
  Serial.println(payload);

  delay(5000);   // publish every 5 seconds
}
s