# M5TelloSDK

## Improvments over the previously used Tello blocks
1: Compatible with all M5Stack devices (Using UiFlow 1.0) instead of just BASIC

2: Has the full feature set of Tello SDK 1.3

3: Better Tello state reporting

### Notes
1: Spaces *ARE* required between the commands and values, please do not remove them

2: WifiCfg and Socket are imported inside of "Tello Connect" and "Tello Init SDK" respectivley

3: "Tello Update State" must be run for any "get" functions to return new values

4: "Tello Keepalive" *Must* be run in a loop less than every 15 seconds, or else a saftey fature will activate and emergency land the drone
