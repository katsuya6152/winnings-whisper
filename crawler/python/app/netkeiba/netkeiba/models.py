import sys
from sqlalchemy import Column, Integer, Text
from . database import ENGINE, Base


class Race(Base):
    __tablename__ = 'races'
    id = Column('id', Text, primary_key=True)
    race_name = Column('race_name', Text)
    race_place = Column('race_place', Text)
    number_of_entries = Column('number_of_entries', Integer)
    race_state = Column('race_state', Text)
    date = Column('date', Text)
    # race_type = Column('race_type', Text)
    # distance = Column('distance', Integer)
    # track_condition = Column('track_condition', Text)
    # course = Column('course', Text)
    # starting_time = Column('starting_time', Text)
    # created_at = Column(DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    # updated_at = Column(DateTime(timezone=True), nullable=False, server_default=current_timestamp())

class RaceResult(Base):
    __tablename__ = 'race_results'
    id = Column('id', Text)
    horse_id = Column('horse_id', Text, primary_key=True)
    rank = Column('rank', Text)
    box = Column('box', Text)
    horse_order = Column('horse_order', Text)
    horse_name = Column('horse_name', Text)
    sex_and_age = Column('sex_and_age', Text)
    burden_weight = Column('burden_weight', Text)
    jockey = Column('jockey', Text)
    time = Column('time', Text)
    difference = Column('difference', Text)
    transit = Column('transit', Text)
    climb = Column('climb', Text)
    odds = Column('odds', Text)
    popularity = Column('popularity', Text)
    horse_weight = Column('horse_weight', Text)
    horse_trainer = Column('horse_trainer', Text)
    horse_owner = Column('horse_owner', Text)
    prize = Column('prize', Text)

def main(args):
    Base.metadata.create_all(bind=ENGINE)


if __name__ == '__main__':
    main(sys.argv)