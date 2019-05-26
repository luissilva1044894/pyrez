from .APIBase import APIBase
from pyrez.enumerations import Endpoint, Format
from pyrez.models.StatusPage import Incidents, ScheduledMaintenances, StatusPage as SttPage
class StatusPageAPI(APIBase):
    """
    A wrapper for the `Status Page <https://status.hirezstudios.com/>`_ API, exposing convenient actions useful for embedding your status anywhere.
    """
    def __init__(self):
        super().__init__()
    def getComponents(self):
        """
        Get the components for the `Status Page <https://status.hirezstudios.com/>`_.

        Each component is listed along with its status - one of ``operational``, ``degraded_performance``, ``partial_outage``, or ``major_outage``.
        """
        return self._httpRequest(self._getEndpoint("components"))
    @classmethod
    def _getEndpoint(cls, _endpoint=None, _api=True, _format="json"):
        return "{}{}{}{}".format(Endpoint.STATUS_PAGE, "/api/v2" if _api else "", "/{}".format(_endpoint) if _endpoint else "",  ".{}".format(_format) if _format else "")
    def getHistory(self, _format=Format.JSON):
        """
        Get the history for the `Status Page <https://status.hirezstudios.com/>`_.
        
        Parameters
        -------
        _format : Optional :class:`.Format`
            Passing in ``None`` will use the default instead of the passed in value.
        """
        return self._httpRequest(self._getEndpoint("history", _api=False, _format=_format or Format.JSON))
    def getIncidents(self, unresolvedOnly=False):
        """
        Get a list of the 50 most recent incidents. This includes all unresolved incidents (``Investigating``, ``Identified``, ``Monitoring``, ``Resolved``, or ``Postmortem``).

        Parameters
        -------
        unresolvedOnly : Optional :class:`bool`
            Only returns a list of unresolved incidents state (``Investigating``, ``Identified``, or ``Monitoring``).
        """
        _ = self._httpRequest(self._getEndpoint("incidents{}".format("/unresolved" if unresolvedOnly else "")))
        return Incidents(**_) if _ else None
    def getScheduledMaintenances(self, activeOnly=False, upcomingOnly=False):
        """
        Get a list of the 50 most recent scheduled maintenances. This includes all scheduled maintenances (Scheduled, In Progress, Verifying, or Completed).

        Parameters
        -------
        activeOnly : Optional :class:`bool`
            Only returns a list of active maintenances. (``In Progress`` or ``Verifying`` state)
        upcomingOnly : Optional :class:`bool`
            Only returns a list of upcoming maintenances. (scheduled maintenances still in the ``Scheduled`` state)
        """
        _ = self._httpRequest(self._getEndpoint("scheduled-maintenances{}".format("/active" if activeOnly else "/upcoming" if upcomingOnly else "")))
        return ScheduledMaintenances(**_) if _ else None
    def getStatus(self):
        """
        Get the status rollup for the whole `Status Page <https://status.hirezstudios.com/>`_.

        This endpoint includes an indicator - one of none, minor, major, or critical, as well as a human description of the blended component status.

        Examples of the blended status include ``All Systems Operational``, ``Partial System Outage``, and ``Major Service Outage``.
        """
        _ = self._httpRequest(self._getEndpoint("status"))
        return SttPage(**_) if _ else None
    def getSummary(self):
        """
        Get a summary of the `Status Page <https://status.hirezstudios.com/>`_,
        including a status indicator, component statuses, unresolved incidents, and any upcoming or in-progress scheduled maintenances.
        """
        return self._httpRequest(self._getEndpoint("summary"))
