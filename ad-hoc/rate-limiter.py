"""
"""

from datetime import datetime

class RateLimiter:
    def __init__(self,number_allowed,window):
        self.number_of_allowed = number_allowed
        self.window = window
        self.map = {}
        
    def allow(self, client_id,now_in):
        now = datetime.now() if now_in is None else now_in
        
        if client_id in self.map:
            count,time_created = self.map[client_id]
            if time_created + self.window > now:
                if count >= self.number_of_allowed:
                    return False
                else:
                    self.map[client_id] = (count+1,time_created)
                    return True
        self.map[client_id] = (1,now)
        return True


def test_rate_limiter():
    calls = [(1,1),(1,1),(1,1)]
    r  = RateLimiter(2,2)
    response = [r.allow(id,time) for id,time in calls]
    assert response == [True,True,False]

    calls = [(1,1),(1,1),(2,1)]
    r  = RateLimiter(2,2)
    response = [r.allow(id,time) for id,time in calls]
    assert response == [True,True,True]

    calls = [(1,1),(1,1),(1,2)]
    r  = RateLimiter(2,2)
    response = [r.allow(id,time) for id,time in calls]
    assert response == [True,True,False]

    calls = [(1,1),(1,1),(1,3)]
    r  = RateLimiter(2,2)
    response = [r.allow(id,time) for id,time in calls]
    assert response == [True,True,True]

    calls = [(1,1),(1,2),(1,2),(1,3)]
    r  = RateLimiter(2,2)
    response = [r.allow(id,time) for id,time in calls]
    assert response == [True,True,False,True]

test_rate_limiter()


