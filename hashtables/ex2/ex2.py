
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    route = [None] * length
    loc = {}
    for ticket in tickets:
        loc[ticket.source] = ticket.destination
    next = loc["NONE"]

    for i in range(0, length):
        route[i] = next
        next = loc[next]

    return route
