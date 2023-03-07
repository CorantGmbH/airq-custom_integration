"""The air-Q integration."""
from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS, CONF_PASSWORD, Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

import aioairq

from .const import DOMAIN, MANUFACTURER, TARGET_ROUTE, UPDATE_INTERVAL

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]


class AirQCoordinator(DataUpdateCoordinator):
    """Coordinator is responsible for querying the device at a specified route."""

    def __init__(
        self,
        hass: HomeAssistant,
        entry: ConfigEntry,
    ) -> None:
        """Initialise a custom coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=UPDATE_INTERVAL),
        )
        session = async_get_clientsession(hass)
        self.airq = aioairq.AirQ(
            entry.data[CONF_IP_ADDRESS], entry.data[CONF_PASSWORD], session
        )
        self.device_id = entry.unique_id
        assert self.device_id is not None
        self.device_info = DeviceInfo(
            manufacturer=MANUFACTURER,
            identifiers={(DOMAIN, self.device_id)},
            name=entry.data["device_info"]["name"],
            model=entry.data["device_info"]["model"],
            suggested_area=entry.data["device_info"]["suggested_area"],
            sw_version=entry.data["device_info"]["sw_version"],
            hw_version=entry.data["device_info"]["hw_version"],
        )

    async def _async_update_data(self) -> dict:
        """Fetch the data from the device."""
        try:
            data = await self.airq.get(TARGET_ROUTE)
        except aioairq.InvalidAirQResponse as err:
            raise UpdateFailed(
                f"Failed to retrieve update from AirQ {self.device_id}: {err}"
            ) from err
        except aioairq.InvalidAuth as err:
            raise ConfigEntryAuthFailed(
                f"Invalid password for AirQ {self.device_id}. "
                "If you changed the password, please reauthenicate"
            ) from err
        return self.airq.drop_uncertainties_from_data(data)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up air-Q from a config entry."""

    coordinator = AirQCoordinator(hass, entry)

    # Query the device for the first time and initialise coordinator.data
    await coordinator.async_config_entry_first_refresh()

    # Record the coordinator in a global store
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
