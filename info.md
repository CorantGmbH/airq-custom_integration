[![GitHub Release][releases-shield]][releases]

[![License][license-shield]][license]

[![hacs][hacsbadge]][hacs]

[![Community Forum][forum-shield]][forum]

_Component to integrate with [air-Q][airq]._

**This component will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show info from the device sensors

{% if not installed %}
## Installation

1. Click download.
1. In the HA UI, start by navigating to `Settings` -> `Devices & Services`, click `Add integration` and search for `air-Q`.

{% endif %}

## Configuration

The integration is set up entirely in HA UI, as opposed to `configuration.yaml`.

After adding the integration, you will prompted for the IP address of the device or the first 5 characters of the serial number, as well as the device password.

For this integration to communicate with the device, both must be connected to the same WiFi network.

***

[airq]: https://github.com/CorantGmbH/airq-custom_integration
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://forum.air-q.com/
[license]: https://github.com/CorantGmbH/airq-custom_integration/blob/main/LICENSE
[license-shield]: https://img.shields.io/github/license/CorantGmbH/airq-custom_integration.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/CorantGmbH/airq-custom_integration.svg?style=for-the-badge
[releases]: https://github.com/CorantGmbH/airq-custom_integration/releases
