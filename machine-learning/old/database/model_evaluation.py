from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import JSON
from datetime import datetime
import json
from database.database_connection import get_database_url

Base = declarative_base()

class ModelEvaluation(Base):
    __tablename__ = 'model_evaluation'
    
    id = Column(Integer, primary_key=True)
    feature_importance_json = Column(JSON)
    TP = Column(Integer)
    FP = Column(Integer)
    FN = Column(Integer)
    TN = Column(Integer)
    FPR = Column(JSON)
    TPR = Column(JSON)
    AUC = Column(Float)
    memo = Column(Text)
    version = Column(String(255))
    created_date = Column(DateTime, default=datetime.utcnow)

def save_evaluation(evaluation_results):
    engine = create_engine(get_database_url())
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    new_evaluation = ModelEvaluation(
        feature_importance_json=evaluation_results["importances"].to_json(),
        TP=evaluation_results["TP"],
        FP=evaluation_results["FP"],
        FN=evaluation_results["FN"],
        TN=evaluation_results["TN"],
        FPR=json.dumps(evaluation_results["FPR"].tolist()),
        TPR=json.dumps(evaluation_results["TPR"].tolist()),
        AUC=evaluation_results["AUC"],
        memo=evaluation_results["memo"],
        version=evaluation_results["version"],
        created_date=datetime.utcnow()
    )
    
    session.add(new_evaluation)
    session.commit()
    session.close()
