from abc import ABC, abstractmethod

class BaseTracker(ABC):

    @abstractmethod
    def fetch_jobs(self, company):
        '''Returns a list of dictionaries with:
        - job_id
        - company
        - priority
        - title
        - location
        - url
        '''
        pass