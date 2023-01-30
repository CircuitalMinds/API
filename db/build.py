from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime


class Table:

    def __init__(self, q):
        self.q = q

    def query_all(self):
        return {
            i.id: {
                arg: getattr(i, arg)
                for arg in self.q.args
            } for i in self.q.query.all()
        }

    def query_filter(self, data_id, first=True):
        data = self.q.filter_by(self.q.id == data_id)
        if first:
            return data.first()
        else:
            return data

    def add(self, db, **data):
        self.q.set_data(**data)
        db.session.add(self.q)
        db.session.commit()
        return {"message": "data added successfully"}

    def update(self, db, old_data, new_data):
        qdata = self.q.query_filter(old_data['id'])
        qdata.__dict__.update(new_data)
        db.session.query(self.q).update(qdata)
        db.session.commit()

    def delete(self, db, data):
        qdata = self.q.query_filter(data['id'])
        db.session.query(self.q).delete(qdata)
        db.session.commit()

