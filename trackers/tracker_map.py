from trackers.greenhouse import GreenhouseTracker
from trackers.lever import LeverTracker
from trackers.ashby import AshbyTracker
from trackers.workable import WorkableTracker
from trackers.workday import WorkdayTracker


TRACKER_MAP = {
    "greenhouse": GreenhouseTracker, 
    "ashbyhq": AshbyTracker,
    "lever": LeverTracker, 
    "workable": WorkableTracker,
    "workday": WorkdayTracker
}