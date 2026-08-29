from trackers.greenhouse import GreenhouseTracker
from trackers.lever import LeverTracker
from trackers.ashby import AshbyTracker
from trackers.workable import WorkableTracker
from trackers.workday import WorkdayTracker
from trackers.ultipro import UltiproTracker
from trackers.smartrecruiters import SmartRecruitersTracker
from trackers.dayforce import DayforceTracker
from trackers.gem import GemTracker
from trackers.bamboohr import BambooHRTracker


TRACKER_MAP = {
    "greenhouse": GreenhouseTracker, 
    "ashbyhq": AshbyTracker,
    "lever": LeverTracker, 
    "workable": WorkableTracker,
    "workday": WorkdayTracker,
    "ultipro": UltiproTracker,
    "smartrecruiters": SmartRecruitersTracker,
    "dayforce": DayforceTracker,
    "gem": GemTracker,
    "bamboohr": BambooHRTracker
}