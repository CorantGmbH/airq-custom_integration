# air-Q device integration

This custom component allows to integrate the sensors, provided by your [air-Q](https://www.air-q.com/) device, into Home Assistant.

## Notice

This integration has been merged into HA core and is expected to appear in 2022.12 release. This repository provides a possibility to access it until said release.

## Installation

This integration can be installed
1. by manually placing its source code in HA configuration folder, following the steps below,
2. or through HACS, by adding this [GitHub repo](https://github.com/CorantGmbH/airq-custom_integration/) as a [custom repository to HACS](https://hacs.xyz/docs/faq/custom_repositories).

To install it manually:

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `airq`.
4. Download _all_ the files from the `custom_components/airq/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI navigate to `Settings` -> `Devices & Services`, click `Add integration` and search for `air-Q`.

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/airq/__init__.py
custom_components/airq/config_flow.py
custom_components/airq/const.py
custom_components/airq/manifest.json
custom_components/airq/sensor.py
custom_components/airq/translations/en.json
```

## Configuration

The integration is set up entirely in HA UI, as opposed to `configuration.yaml`.

After adding the integration, you will prompted for the IP address of the device or the first 5 characters of the serial number, as well as the device password.

For this integration to communicate with the device, both must be connected to the same WiFi network.

## Sensors

Currently, the integration supports the following sensors:

| Sensor name          | Unit of measurement |
|----------------------|---------------------|
| Ammonia              | µg/m³               |
| Chlorine             | µg/m³               |
| CO                   | mg/m³               |
| CO2                  | ppm                 |
| Dew Point            | °C                  |
| Ethanol              | µg/m³               |
| Formaldehyde         | µg/m³               |
| H2S                  | µg/m³               |
| Health Index         | %                   |
| Humidity[^rel]       | %                   |
| Absolute Humidity    | g/m³                |
| Hydrogen             | µg/m³               |
| Methane              | %                   |
| N2O                  | µg/m³               |
| NO                   | µg/m³               |
| NO2                  | µg/m³               |
| Ozone                | µg/m³               |
| Oxygen               | µg/m³               |
| Performance Index    | %                   |
| PM1, PM25, PM10[^pm] | µg/m³               |
| Pressure             | hPa                 |
| Relative Pressure    | hPa                 |
| Propane              | %                   |
| SO2                  | µg/m³               |
| Noise                | dBa                 |
| Noise (Maxumum)      | dBa                 |
| Radon                | Bq/m³               |
| Temperature          | °C                  |
| VOC[^voc]            | ppb                 |
| VOC (Industrial)     | ppb                 |

[^rel]: Relative

[^pm]: Correspond to concentrations of particulates with diameter less than 1µm, 2.5µm, and 10µm respectively

[^voc]: Volatile organic compounds

After the setup, separate entities will be created for each of the aforementioned sensors, found in your device.
