#include <WiFi.h>

// Replace with your network credentials
const char* ssid = "Shravani";
const char* password = "Shravni@8046";

void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println("Connecting to Wi-Fi...");
  WiFi.begin(ssid, password);

  // Wait until connected
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWi-Fi connected successfully!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}
void loop() {
  // Nothing to do here
}
