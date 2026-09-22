from __future__ import annotations
class PriceBook:
    def __init__(self, bands):
        self.bands = list(bands)
    def copy(self):
        return PriceBook([(a, b, u) for a, b, u in self.bands])
class Ticket:
    def __init__(self, ticket_id, weight, book: PriceBook):
        self.ticket_id = ticket_id
        self.weight = weight
        self.book = book.copy()
    def charge(self) -> int:
        w = self.weight
        if w is None:
            raise ValueError(f"empty weight ticket={self.ticket_id}")
        if w < 0:
            raise ValueError(f"neg weight ticket={self.ticket_id}")
        if w == 0:
            return 0
        total = 0
        remain = w
        prev = 0
        for start, end, unit in self.book.bands:
            if start != prev:
                raise ValueError("gap/overlap in bands")
            span = remain if end is None else max(0, min(remain, end - start))
            total += span * unit
            remain -= span
            prev = end if end is not None else prev + span
            if remain == 0:
                break
        if remain:
            raise ValueError("weight beyond bands")
        return total
